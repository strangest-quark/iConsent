<template>
  <div class="videojs">
    <!-- <h1>{{ title }}</h1> -->

    <div class="video-inner-container">
      <video
        controls
        responsive="true"
        autoplay="true"
      ><source src="@/assets/sample_video.mp4" type="video/mp4"></video>
    </div>
  </div>
</template>

<script>
import 'video.js/dist/video-js.min.css'
import 'video.js/dist/video.min.js'

export default {

}
</script>

<style scoped>
.video-js.vjs-fluid{
    height: 80vh;
}
</style>
