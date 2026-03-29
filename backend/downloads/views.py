from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from subprocess import call

# Create your views here.
@api_view(["POST"])
def add_download_queue(req):
    link_provider = req.data.get("linkProvider")
    if link_provider == "debridDownload":
        download_result = debrid_download(req)




    downloads = [
        {"queueID": 1,
         "fileName": "test_name",
         "fileType": file_type,
         "storedLocation": stored_location,
         "fileSize": "5GB"}
    ]
    return Response(downloads, status=201)
    pass


@api_view(["GET"])
def get_directory_structure(req):
    
    pass

@api_view(["GET"])
def get_current_queue(req):
    pass

@api_view(["GET"])
def get_current_download_progress(req):
    pass

