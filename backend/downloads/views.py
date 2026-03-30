from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from subprocess import call
from .download_handler import debrid_download
from .directory_hanlder import sub_directory_list

@api_view(["POST"])
async def add_download_queue(req):
    # req.body format:
    # url: download link
    # storedLocation: directory to store
    # mediaType: audio or video
    # linkProvider: debrid or google or direct
    link_provider = req.data.get("linkProvider")
    if link_provider == "debridDownload":
        download_result = await debrid_download(req)
   
    return Response(
        download_result["downloads"],
        status=download_result["status_code"])

@api_view(["GET"])
async def get_directory_structure(req):
    sub_dir_result = await sub_directory_list(req)

    return Response(
        sub_dir_result,
        status=sub_dir_result["status_code"]
    )

@api_view(["GET"])
def get_current_queue(req):
    pass

@api_view(["GET"])
def get_current_download_progress(req):
    pass

