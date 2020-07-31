<template>
  <div @click="clickPendingConsent" class="card">
    <div class="card-content">
      <slot />
    </div>
    <footer class="card-footer">
      <!-- <span @click="rejectConsent" class="card-footer-item reject">
        <b-icon icon="close-circle-outline" custom-size="default" />Reject
      </span>
      <span @click="acceptConsent" class="card-footer-item approve">
        <b-icon icon="check-circle-outline" custom-size="default" />Approve
      </span> -->
      <span class="card-footer-item more">
        {{$t('buttonViewMore')}} <b-icon icon="arrow-right-circle-outline" custom-size="default" />
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
    },
    rejectConsent () {
      if (this.forceUserAction) {
        alert('API CALL')
      } else {
        this.isComponentModalActive = true
        this.forceUserAction = true
      }
    },
    startAnimation () {
      this.$confetti.start({
        particles: [
          {
            type: 'circle'
          }
        ],
        defaultColors: ['#079AFF', '#F26C63', '#99D25C', '#FAB909']
      })
    },
    stopAnimation () {
      this.$confetti.stop()
    },
    acceptConsent () {
      if (this.userReadFully) {
        this.isFullyReadModalActive = true
        this.startAnimation()
        const here = this
        setInterval(function () {
          here.stopAnimation()
        }, 4000)
        // this.isComponentModalActive = false
      } else if (this.forceUserAction) {
        // call api
      } else {
        this.isComponentModalActive = true
        this.forceUserAction = true
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
  color: #079AFF;
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
