<script setup>
import SearchComponent from './components/LinkInputComponent.vue';
import DownloadQueueComponent from './components/DownloadQueueComponent.vue';
</script>

<template>
  <div id="frontPage">
    <SearchComponent />
    <DownloadQueueComponent />
  </div>
</template>


<style>
#frontPage{
  display: flex;
  flex-direction: column;
  gap: 15px;
}
</style>
