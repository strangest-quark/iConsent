<template>
    <div class="center">
       <h1 class="subtitle is-5"> No {{consentType}} consents left </h1>
    </div>
</template>

<script>
export default {
  props: {
    consentType: {
      type: String,
      default: null
    }
  }
}
</script>

<style scoped>
.center{
  margin : 0 auto;
  text-align : center;
}
</style>
