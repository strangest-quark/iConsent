<template>
  <div @click="clickPendingConsent" class="card">
    <div class="card-content">
      <slot />
    </div>
    <footer v-if="status=='pending'" class="card-footer">
      <span class="card-footer-item more">
        {{$t('buttonViewMore')}}
        <b-icon icon="arrow-right-circle-outline" custom-size="default" />
      </span>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'CardComponent',
  props: {
    status: {
      type: String,
      default: null
    },
    artifactId: {
      type: String,
      default: null
    }
  },
  data () {
    return {
      isComponentModalActive: false,
      isFullyReadModalActive: false,
      forceUserAction: false
    }
  },
  methods: {
    clickPendingConsent () {
      if (this.status === 'pending') {
        this.$router.push(`/consents/pending/${this.artifactId}`)
      }
    }
  }
}
</script>

<style scoped>
.logo {
  max-width: 10rem;
}
.card {
  /* cursor: pointer; */
  box-shadow: 0px 0px 10px rgba(0.2, 0.2, 0.2, 0.2);
}
.card:hover {
  cursor: pointer;
  box-shadow: 5px 5px 5px rgba(0.2, 0.2, 0.2, 0.2);
}
.card-header-end {
  text-align: right;
}
.card-footer-item.reject {
  font-weight: bold;
  color: #e11a50;
}
.card-footer-item.approve {
  font-weight: bold;
  color: #03b072;
}

.card-footer-item.more {
  font-weight: bold;
  color: #079aff;
  cursor: pointer;
}
.proceed-title {
  margin-top: 1rem !important;
  text-align: center;
}
.modal-card {
  width: auto;
  border-radius: 1rem;
}
.congragulations-model {
  text-align: center;
}
.reject {
  font-weight: bold;
  color: #e11a50;
}
.approve {
  font-weight: bold;
  color: #03b072;
}
</style>
