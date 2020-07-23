<template>
  <div class="columns is-multiline">
      <div class="column is-two-fifths content-left">
        <h1> Consents </h1>
        <ConsentIcons/>
    </div>
      <div class="column content-right is-hidden-mobile">
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
