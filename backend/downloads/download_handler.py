import requests, math, re, os
from subprocess import call
DEBRID_DOWNLOAD_API = "https://debrid-link.com/api/v2/downloader/add"
JELLYFIN_PATH = "/home/hommula/jellyfin_media"




def debrid_download(req):
    try:
        stored_location = req.data.get("storedLocation")
        file_type = req.data.get("fileType")
        url = req.data.get("url")
        payload = {"url": url}
        r = requests.post(DEBRID_DOWNLOAD_API, json=payload)
        data = r.json()

        if data.success and data.value:
            files_to_download = [file for file in data.value]
            queued_downloads = []
            for file in files_to_download:
                download_result = download_handler(file, file_type, stored_location)
                queued_downloads.append(download_result)



    except:
        print("huh")


def download_handler(file, file_type, stored_location):
    try:
        safe_file_name = re.sub(r"[^a-zA-Z0-9._-]", "", file["name"])
        full_path = JELLYFIN_PATH + file_type + stored_location
        os.mkdir()
    except Exception as e:
        print(f"Error caught in download_handler: {e}")


def file_size_helper(raw_byte):
    if raw_byte == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB")
    i = int(math.floor(math.log(raw_byte, 1024)))
    p = math.pow(1024, i)
    s = round(raw_byte / p, 2)
    return "%s %s" % (s, size_name[i])