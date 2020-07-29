<template>
  <div class="card">
    <div @click="clickPendingConsent" class="card-content">
      <slot />
    </div>
    <footer class="card-footer">
      <span @click="rejectConsent" class="card-footer-item reject">
        <b-icon icon="close-circle-outline" custom-size="default" />Reject
      </span>
      <span @click="acceptConsent" class="card-footer-item approve">
        <b-icon icon="check-circle-outline" custom-size="default" />Approve
      </span>
      <span class="card-footer-item more">
        <b-icon icon="arrow-right-circle-outline" custom-size="default" />More
      </span>
    </footer>

    <b-modal
      :active.sync="isComponentModalActive"
      has-modal-card
      trap-focus
      :destroy-on-hide="false"
      aria-role="dialog"
      aria-modal
    >
      <div class="modal-card">
        <section class="modal-card-body">
          <h4 class="title is-6">Uh oh...</h4>
          <h4 class="subtitle is-6">Looks like you haven’t read the consent details completely!</h4>
          <h2 class="title proceed-title is-5">Sure you want to proceed?</h2>
          <div class="columns is-mobile">
            <div class="column" align="right">
              <b-button
                type="is-rounded"
                class="reject"
                @click="rejectConsent"
                icon-left="close-circle-outline"
              >Reject</b-button>
            </div>
            <div class="column" align="left">
              <b-button
                type="is-rounded"
                class="approve"
                @click="acceptConsent"
                icon-left="check-circle-outline"
              >Approve</b-button>
            </div>
          </div>
        </section>
      </div>
    </b-modal>
    <b-modal
      :active.sync="isFullyReadModalActive"
      has-modal-card
      trap-focus
      :destroy-on-hide="false"
      aria-role="dialog"
      aria-modal
    >
      <div class="modal-card">
        <section class="modal-card-body">
          <h4 class="title is-6">Awesome!!</h4>
          <h4 class="subtitle is-6">
            <div>You have read this consent details fully.</div>
            <div>Kudos to keeping yourself informed of your data/privacy rights.</div>
          </h4>
          <div class="congragulations-model">
            <div class="columns is-mobile is-centered">
              <!-- <div class="logo column" align="center">
                <img :src="consentData.fiu_logo" />
              </div>-->
            </div>

            <h4 class="title is-6">Quickbooks can now access your savings accounts!</h4>
          </div>
        </section>
      </div>
    </b-modal>
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
.card:hover {
  cursor: pointer;
  box-shadow: 0px 0px 10px rgba(0.2, 0.2, 0.2, 0.2);
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
  color: #666666;
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
