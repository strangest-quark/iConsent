<template>
<div class="row">
    <div class="left">
        <h1> Consents </h1>
        <ConsentIcons style="width: 70%;"/>
    </div>
      <div class="right">
      </div>
</div>
</template>

<script>
import ConsentIcons from '@/components/ConsentIcons'

export default {
  components: {
    ConsentIcons
  }
}
</script>

<style scoped>
.row {
  display: flex;
  width: 100%;
}

.left {
  flex: 50%;
  margin-top: auto;
  margin-bottom: auto;
}

.right {
  width: 50%;
  text-align: center;
}
</style>
