import math, re, os, asyncio, httpx
from dotenv import load_dotenv
load_dotenv()

DEBRID_DOWNLOAD_API = os.getenv('DEBRID_DOWNLOAD_API')
JELLYFIN_PATH = os.getenv('JELLYFIN_PATH')

async def debrid_download(req):
    try:
        stored_location = req.data.get("storedLocation")
        media_type = req.data.get("mediaType")
        url = req.data.get("url")
        payload = {"url": url}
        async with httpx.AsyncClient() as client:
            r = await client.post(DEBRID_DOWNLOAD_API, json=payload)
        data = r.json()

        if data["success"] and data["value"]:
            files_to_download = [file for file in data["value"]]
            queued_downloads = []
            for file in files_to_download:
                download_result = await download_handler(file, media_type, stored_location)
                queued_downloads.append(download_result)
            return {
                "status": "Success",
                "status_code": 201,
                "downloads": queued_downloads
            }
        return {
            "status": "Failed",
            "status_code": 500,
            "downloads": []
        }

    except Exception as e:
        print("Error caught in debrid_download: ", e)
        return {
            "status": "Failed",
            "status_code": 500,
            "error_message": e,
            "downloads": []
        }


async def download_handler(file, media_type, stored_location):
    try:
        # modify file name to linux-safe format
        safe_file_name = re.sub(r"[^a-zA-Z0-9._-]", "", file["name"])
        download_dir_path = os.path.join(JELLYFIN_PATH, media_type, stored_location)
        try:
            os.mkdir(download_dir_path)
        except OSError as e:
            print(e)
        full_path = os.path.join(download_dir_path, safe_file_name)
        file_name, ext_name = os.path.splitext(safe_file_name)
        final_file_name = safe_file_name
        if os.path.isfile(full_path):
            counter = 0
            while os.path.isfile(full_path):
                full_path = os.path.join(download_dir_path, file_name + str(counter) + ext_name)
                counter += 1
            final_file_name = file_name + str(counter) + ext_name
        aria_download_command = f"aria2c -c -k 10M -o {final_file_name} {file['downloadUrl']}"
        proc = await asyncio.create_subprocess_shell(
            aria_download_command,
            cwd=download_dir_path,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await proc.communicate()
        if proc.returncode != 0:
            raise Exception(f"aria2c failed: {stderr.decode()}")
        converted_file_size = file_size_helper(file["size"])

        return {
            "status": "success",
            "queueID": file["id"], 
            "fileName": final_file_name,
            "mediaType": media_type,
            "storedLocation": download_dir_path,
            "fileSize": converted_file_size
        }
        
    except Exception as e:
        print(f"Error caught in download_handler: {e}")
        return {
            "status": "failed",
            "queueID": file["id"], 
            "error_message": str(e)
        }


def file_size_helper(raw_byte):
    if raw_byte == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB")
    i = int(math.floor(math.log(raw_byte, 1024)))
    p = math.pow(1024, i)
    s = round(raw_byte / p, 2)
    return "%s %s" % (s, size_name[i])