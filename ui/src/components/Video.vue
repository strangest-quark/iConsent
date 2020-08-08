<template>
  <div id="app">
    <VideoJS :url="url" />
  </div>
</template>

<script>
import VideoJS from '@/components/VideoPlayer'

export default {
  props: {
    url: {
      type: String,
      default: null
    }
  },
  components: {
    VideoJS
  }
}
</script>
