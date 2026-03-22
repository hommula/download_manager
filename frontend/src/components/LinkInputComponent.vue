<script setup>
import { onMounted, ref } from 'vue';
import { reactive } from 'vue';
import axios from 'axios';
import addIcon from '../assets/add.jpg'
import '../styles/global.css'

const download_link = ref('');
const storage_directory = ref([]);
const fileDestination = ref('');
const media_type = ref('');

onMounted(() =>
{
    storage_directory.value.push("testing1", "testing2")
})

function onDownloadQueued()
{

}

function refreshDirectory()
{

}

</script>

<template>
    <div id="searchComponent">
        <div id="titleHeader">
            <h1>
                Download Manager
            </h1>
        </div>
        <p>This is your path: {{ media_type }}/{{ fileDestination }}</p>
        <div id="linkInputBox">
            <select name="linkProviderOption" id="linkProviderOption">
                <option value="debridDownload">Debrid</option>
                <option value="directDownload">Direct</option>
                <option value="googleDownload">Google</option>
            </select>
            <input v-model="download_link" placeholder="Type your download link here" id="downloadLinkInputBox"> 
            <button @click="onDownloadQueued" id="queueDownloadBtn">Queue Download</button>
        </div>
        <div id="linkOptions">
            <div class="optionAttributes">
                <label for="mediaType">Media Type</label>
                <select name="mediaType" id="mediaTypeSelection" v-model="media_type">
                    <option value="" disabled>select media type</option>
                    <option value="audio">audio</option>
                    <option value="video">video</option>
                </select>
                <label for="fileDestination">Destination</label>
                <select name="fileDestination" id="fileDestination" v-model="fileDestination">
                    <option value="" disabled>select a folder</option>
                    <option v-for="dir in storage_directory" :key="dir" :value="dir">
                        {{ dir }}
                    </option>
                </select>
                <input type="image" :src="addIcon" id="addSubDir"/>
                <button @click="refreshDirectory">Refresh Directory</button>
            </div>
        </div>
    </div>
</template>



<style>
.optionAttributes{
    display: flex;
    gap: 10px;
    justify-content: center;
}

#mediaTypeSelection{
    width: fit-content;
}

#downloadLinkInputBox{
    width: 60%;
    height: 2.0em;
}

#fileDestination{
    width: fit-content;
}

#searchComponent{
    display: flex;
    flex-direction: column;
}

#titleHeader{
    margin: 10px;
}

#linkInputBox{
    display: flex;
    margin: 10px;
    justify-content: center;
    gap: 10px;
    align-items: baseline;
}

#linkOptions{
    display: flex;
    flex-direction: row;
    justify-content: center;
    margin: 20px;
    gap: 10px;
    align-items: baseline;

}

#queueDownloadBtn{
    background-color: white;
    color: black;
    width: 10em;
    height: 3em;
    font-size: large;
}

#addSubDir{
    width:20px;
    height: 20px;
    background-color: azure;
    border-radius: 2px;
}

</style>