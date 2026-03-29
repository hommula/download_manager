import pytest
from rest_framework import status
from rest_framework.test import APIClient


@pytest.fixture
def client():
    return APIClient()

# helper function to verify the download records are in correct format
def assert_download_fields(record):
    assert 'queueID' in record
    assert 'fileName' in record
    assert 'mediaType' in record
    assert 'storedLocation' in record
    assert 'fileSize' in record

# test on queuing direct download 
def test_queue_direct_download_return_201(client):
    res = client.post('/queue_downloads',{
        "url": "https://file-examples.com/storage/feb22885ff69bf452995602/2017/04/file_example_MP4_480_1_5MG.mp4",
        "mediaType": "Video",
        "linkProvider": "direct",
        "storedLocation": "/home/Desktop",
    }, format="json")
    assert res.status_code == 201 # the download queue is created successfully
    first_record = res.data[0] # get the first download record from the response 
    assert isinstance(res.data, list) # the response contains a list of data describing the downloads
    assert_download_fields(first_record)
    
# test on fetching for sub directories under the specified dir
def test_refresh_directory(client):
    res = client.get('/dir_structure', {
        "currentDir": "/home/Desktop"
    })
    assert res.status_code == 200 # successfully fetched for subDir under the current directory
    assert isinstance(res.data, list) # the response returns a list containing child dirs in string
# test on fetching for no sub directory 
def test_refresh_directory_no_child(client):
    res = client.get('/dir_structure',{
        "currentDir": "/home/Desktop"                     
    })
    assert res.status_code == 200
    assert isinstance(res.data, list)
    assert not len(res.data)

# test on fetching for invalid directory name
def test_refresh_directory_invalid_name(client):
    res = client.get('/dir_structure',{
        "currentDir": ""
    })
    assert res.status_code == 400
    

# test on fetching for the current download queue
def test_refresh_download_queue(client):
    res = client.get("/queue")
    assert res.status_code == 200 # successfully fetched for the curretn download queue
    assert isinstance(res.data, list)# the response data contains a list of downloads that is downloading || queued. No finished
    if len(res.data) > 0:
        first_record = res.data[0]
        assert_download_fields(first_record)

# test on fetching for empty download queue, expect empty queue returned
def test_refresh_empty_download_queue(client):
    res = client.get("/queue")
    assert res.status_code == 200
    assert isinstance(res.data, list)
    assert len(res.data) == 0
 
# test on fetching for the current download queue's progress
def test_get_progress(client):
    res = client.get('/download_progress') 
    assert res.status_code == 200
    assert isinstance(res.data, list) # the result contains a list of downloading downloads. Containing their queueID, progress in float

