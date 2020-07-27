<template>
  <div>
    <consents-approval :artifactId="$route.params.id" />
  </div>
</template>

<script>
import ConsentsApproval from '@/components/ConsentsApproval.vue'
export default {
  components: {
    ConsentsApproval
  }
}
</script>
