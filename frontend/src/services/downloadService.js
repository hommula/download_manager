import axios from "axios";
const BASE_URL = "httpL//localhost:8000"

export async function refreshDirectory()
{
    const res = await axios.get(`${BASE_URL}`); // to be finished
    return res.data // expects ["folder1", "folder2", "folder3"]
}


export async function queueDownload(link, media_type, destination, provider)
{
    const res = await axios.post(`${BASE_URL}`, {
        url: link, // Download link
        mediaType: media_type, // Video or Autio
        destination: destination, // location to download the file
        provider: provider // debrid, google, direct, maybe more
    })
    return res.data
    /* expect a list of objects containing queue result
    [
        {
            queueID: queueID
            status: queued || failed || downloading || finished
            file_name:  video.mp4
            fileDestination: /home/Desktop
            size:   5GB
        }
    ]
    */
}