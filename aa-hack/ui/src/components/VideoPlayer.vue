<template>
  <div class="videojs">
    <!-- <h1>{{ title }}</h1> -->

    <div class="video-inner-container">
      <video
        controls
        responsive="true"
      ><source :src="url" type="video/mp4"></video>
    </div>
  </div>
</template>

<script>
import 'video.js/dist/video-js.min.css'
import 'video.js/dist/video.min.js'

export default {
  props: {
    url: {
      type: String,
      default: null
    }
  }
}
</script>

<style scoped>
.video-js.vjs-fluid{
    height: 80vh;
}
video {
  border-radius: 0.5rem
}
</style>
