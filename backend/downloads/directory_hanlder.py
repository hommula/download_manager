import os, asyncio
from dotenv import load_dotenv
load_dotenv()
JELLYFIN_PATH = os.getenv('JELLYFIN_PATH')

async def sub_directory_list(req):  
    try:
        parent_dir_path = req.data.get("storedLocation")
        if parent_dir_path is None or not isinstance(parent_dir_path, str):
            raise RuntimeError("parent_dir_path is invalid")
        media_path = req.data.get("mediaType")
        full_parent_dir_path = os.path.join(JELLYFIN_PATH, media_path, parent_dir_path)
        proc = await asyncio.create_subprocess_exec(
            "find", ".", "-type", "d",
            cwd=full_parent_dir_path,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await proc.communicate()
        if proc.returncode != 0:
            raise RuntimeError(stderr.decode().strip())
        result = stdout.decode().splitlines()
        return {
            "status": "success",
            "status_code": 200,
            "sub_directories": result,
        }
    except Exception as e:
        print(f"Error caught when trying to get the sub directories: {e}")
        return {
            "status": "Failed",
            "status_code": 500,
            "error_message": str(e)
        }