<template>
  <card-component>
    <div class="level is-mobile">
      <div class="level-item">
        <div class="is-widget-label columns is-vcentered">
          <div class="">
          <h1 class="title is-2">
            <growing-number :value="number" :prefix="prefix" :suffix="suffix" />
          </h1>
          </div>
          <div class="column">
          <h3 v-html="getLabelSplitted(label)" class="subtitle is-spaced"></h3>
          </div>
        </div>
      </div>
    </div>
  </card-component>
</template>

<script>
import CardComponent from '@/components/CardComponent'
import GrowingNumber from '@/components/GrowingNumber'
export default {
  name: 'CardWidget',
  components: { GrowingNumber, CardComponent },
  methods: {
    getLabelSplitted (label) {
      return label.replace(' ', '<br>')
    }
  },
  props: {
    icon: {
      type: String,
      default: null
    },
    number: {
      type: Number,
      default: 0
    },
    prefix: {
      type: String,
      default: null
    },
    suffix: {
      type: String,
      default: null
    },
    label: {
      type: String,
      default: null
    },
    type: {
      type: String,
      default: null
    }
  }
}
</script>

<style scoped>
.subtitle{
  color: rgba(0, 0, 0, 0.900) !important;
}
.title {
  color: rgba(0, 0, 0, 0.800)
}
</style>
