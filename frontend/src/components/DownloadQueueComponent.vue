<script setup>
import { ref } from 'vue';
import { onMounted } from 'vue';
import { refreshDirectory, queueDownload} from '../services/downloadService.js';
const dummyTableData = ref([]);
onMounted(() => 
{
    dummyTableData.value.push({
        "queueID": 1,
        "fileName": "testFile1",
        "fileType": "Media",
        "fileDestination": "/home/Desktop/testFile1",
        "Status": "Queued",
        "fileSize": "5GB",
        "progress": 0.71
    })
    dummyTableData.value.push({
        "queueID": 2,
        "fileName": "testFile2",
        "fileType": "Video",
        "fileDestination": "/home/Desktop/testFile2",
        "Status": "Queued",
        "fileSize": "5GB",
        "progress": 0.51
    })
    dummyTableData.value.push({
        "queueID": 3,
        "fileName": "testFile3",
        "fileType": "Video",
        "fileDestination": "/home/Desktop/testFile3",
        "Status": "Downloading",
        "fileSize": "5GB",
        "progress": 0.8
    })
})
</script>

<template>
    <table id="donwloadQueueTable">
        <thead> <!--table head for the queue-->
            <tr>
                <th>Queue ID</th>
                <th>File Name</th>
                <th>File Type</th>
                <th>File Destination</th>
                <th>Status</th>
                <th>File Size</th>
                <th>Progress</th>
            </tr>
        </thead>
        <tbody> <!--table body for the queue-->
            <tr v-for="download in dummyTableData">
                <td>{{ download.queueID }}</td>
                <td>{{ download.fileName }}</td>
                <td>{{ download.fileType }}</td>
                <td>{{ download.fileDestination }}</td>
                <td>{{ download.Status }}</td>
                <td>{{ download.fileSize }}</td>
                <td>{{ download.progress * 100 }}%</td>
            </tr>
        </tbody>
    </table>
</template>


<style>
tr{
    background-color: rgb(49, 49, 49);
    color: rgb(238, 247, 255);
}

#donwloadQueueTable{
    width: 80%;
    margin: 0 auto;
}
</style>