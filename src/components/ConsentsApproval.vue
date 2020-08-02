<template>
  <div>
    <div v-if="isLoading" class="is-center">
      <bounce :loading="true"></bounce>
    </div>
    <div class="section is-fluid">
      <div v-if="consentData" class="columns is-multiline">
        <div class="column">
          <b-button
            @click="$router.go(-1)"
            class="pending-button"
            icon-left="chevron-left"
            type="is-text"
          >{{$t('buttonPending')}}</b-button>
          <div>
            <div class="rows">
              <div class="row columns is-mobile is-vcentered">
                <div class="logo column" align="left">
                  <img :src="consentData.fiu_logo" />
                </div>
                <div v-if="consentData.isVerified" class="column is-green" align="right">
                  {{$t('labelVerified')}}
                  <b-icon icon="shield-check" custom-size="default" />
                </div>
              </div>
              <div>
                <div class="row">
                  <h2 class="title is-5">{{consentData.tagline}}</h2>
                </div>
                <hr />
                <div style="width: 100%; padding-top: 2%">
                  <step-progress
                    :steps="progressSteps"
                    :active-color="progressColor"
                    :active-thickness="3"
                    :passive-thickness="3"
                    :line-thickness="3"
                    :current-step="currentStep"
                    icon-class="fa fa-check"
                  ></step-progress>
                </div>
                <div>
                  <div class="card">
                    <div class="card-content">
                      <!-- why -->
                      <div v-if="currentStep==0" class="rows">
                        <span class="row">
                          <h2 class="question subtitle is-6">{{consentData.q1}}</h2>
                        </span>
                        <span class="row">
                          <p class="answer">{{consentData.ans1}}</p>
                        </span>
                      </div>
                      <!-- how long -->
                      <div v-if="currentStep==1" class="rows">
                        <span class="row">
                          <h2 class="question subtitle is-6">{{consentData.q2}}</h2>
                        </span>
                        <span class="row">
                          <span class>
                            <span class="column">
                              <p class="answer">{{consentData.from}}</p>
                              <p class="answer">
                                <strong>{{consentData.fromDate}}</strong>
                              </p>
                            </span>
                            <span class="column">
                              <p class="answer">{{consentData.to}}</p>
                              <p class="answer">
                                <strong>{{consentData.toDate}}</strong>
                              </p>
                            </span>
                          </span>
                        </span>
                      </div>
                      <!-- for -->
                      <div v-if="currentStep==2" class="rows">
                        <span class="row">
                          <h2 class="question subtitle is-6">{{consentData.bank_ques}}</h2>
                        </span>
                        <div class="row">
                          <BankList
                            :line1="line1"
                            :line2="line2"
                            :accounts="consentData.accounts"
                            :haveCheckBox="haveCheckBox"
                          />
                        </div>
                      </div>
                      <!-- what -->
                      <div v-if="currentStep==3" class="rows">
                        <span class="row">
                          <h2 class="question subtitle is-6">{{consentData.q4}}</h2>
                        </span>
                        <div class="row">
                          <div class="column" style="text-align: center; width: 100%">
                            <img
                              style="padding-left: 25%; padding-right: 25%; text-align: center"
                              :src="consentData.card1_icon"
                            />
                          </div>
                          <div class="column" style="text-align: center; width: 100%">
                            <img
                              style="padding-left: 25%; padding-right: 25%; text-align: center"
                              :src="consentData.card2_icon"
                            />
                          </div>
                          <div class="column" style="text-align: center; width: 100%">
                            <img
                              style="padding-left: 25%; padding-right: 25%; text-align: center"
                              :src="consentData.card3_icon"
                            />
                          </div>
                        </div>
                        <div class="row" style="display: table;">
                          <h1 style="font-size: font-size: 1vmax">{{consentData.ans4}}</h1>
                        </div>
                      </div>
                      <!-- till when -->
                      <div v-if="currentStep==4" class="rows">
                        <span class="row">
                          <h2 class="question subtitle is-6">{{consentData.q3}}</h2>
                        </span>
                        <span class="row">
                          <p class="answer">{{consentData.validTill}}</p>
                        </span>
                      </div>
                      <!-- video -->
                      <!-- <div v-if="currentStep==4" class="rows">
                      <span class="row">
                        <h2 class="question subtitle is-6">What range of my data will be accessed?</h2>
                      </span>
                      <span class="row">
                        <span class="columns">
                          <span class="column">
                            <p class="answer">From</p>
                            <p class="answer">
                              <strong>06 July 2020</strong>
                            </p>
                          </span>
                          <span class="column">
                            <p class="answer">To</p>
                            <p class="answer">
                              <strong>06 July 2021</strong>
                            </p>
                          </span>
                        </span>
                      </span>
                      </div>-->
                    </div>
                  </div>

                  <div class="columns is-mobile is-vcentered">
                    <div class="column" align="left">
                      <b-button v-if="isBackButtonDisabled" disabled>{{$t('buttonBack')}}</b-button>
                      <b-button v-else @click="previousCard">{{$t('buttonBack')}}</b-button>
                    </div>
                    <div class="column" align="right">
                      <b-button
                        v-if="isNextButtonDisabled"
                        disabled
                        type="is-primary"
                      >{{$t('buttonNext')}}</b-button>
                      <b-button v-else @click="nextCard" type="is-primary">{{$t('buttonNext')}}</b-button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div
          class="column video-placement is-half content-right is-hidden-mobile"
          style="padding-left: 5%"
        >
          <div class="rows">
            <div class="row video">
              <Video :url="consentData.video" />
            </div>
          </div>
        </div>
      </div>
      <div v-if="consentData" class="columns is-left">
        <div class="column card-content is-half" align="left">
          <div class="columns is-mobile">
            <div class="column" align="right">
              <b-button
                type="is-rounded"
                class="reject"
                size="is-medium"
                @click="rejectConsent"
                icon-left="close-circle-outline"
              >{{$t('buttonReject')}}</b-button>
            </div>
            <div class="column" align="left">
              <b-button
                type="is-rounded"
                class="approve"
                size="is-medium"
                @click="acceptConsent1"
                icon-left="check-circle-outline"
              >{{$t('buttonApprove')}}</b-button>
            </div>
          </div>
        </div>
      </div>
      <b-modal
        v-if="consentData"
        :active.sync="isComponentModalActive"
        has-modal-card
        trap-focus
        :destroy-on-hide="false"
        aria-role="dialog"
        aria-modal
      >
        <div class="not-read-consent modal-card">
          <section class="modal-card-body">
            <h4 class="title is-6">{{consentData.warn_1}}</h4>
            <h4 class="subtitle is-6">{{consentData.warn_2}}</h4>
            <h2 class="title proceed-title is-5">{{consentData.warn_3}}</h2>
            <div class="columns is-mobile">
              <div class="column" align="right">
                <b-button
                  type="is-rounded"
                  class="reject"
                  @click="rejectConsent"
                  icon-left="close-circle-outline"
                >{{$t('buttonReject')}}</b-button>
              </div>
              <div class="column" align="left">
                <b-button
                  type="is-rounded"
                  class="approve"
                  @click="acceptConsent2"
                  icon-left="check-circle-outline"
                >{{$t('buttonApprove')}}</b-button>
              </div>
            </div>
          </section>
        </div>
      </b-modal>
      <b-modal
        v-if="consentData"
        :active.sync="isFullyReadModalActive"
        has-modal-card
        trap-focus
        :destroy-on-hide="false"
        aria-role="dialog"
        aria-modal
      >
        <div class="modal-card">
          <section class="modal-card-body">
            <h4 class="title is-6">{{consentData.hurray_1}}</h4>
            <h4 class="subtitle is-6">
              <div>{{consentData.hurray_2}}</div>
              <div>{{consentData.hurray_3}}</div>
            </h4>
            <div class="congragulations-model">
              <div class="columns is-mobile is-centered">
                <div class="logo column" align="center">
                  <img :src="consentData.fiu_logo" />
                </div>
              </div>

              <h4 class="title is-6">{{consentData.hurray_4}}</h4>
            </div>
          </section>
        </div>
      </b-modal>
      <b-modal
        v-if="consentData"
        :active.sync="isAcceptModalActive"
        has-modal-card
        trap-focus
        :destroy-on-hide="false"
        aria-role="dialog"
        aria-modal
      >
        <div class="modal-card">
          <section class="modal-card-body">
            <div class="congragulations-model">
              <div class="columns is-mobile is-centered">
                <div class="logo column" align="center">
                  <img :src="consentData.fiu_logo" />
                </div>
              </div>

              <h4 class="title is-6">{{consentData.hurray_4}}</h4>
            </div>
          </section>
        </div>
      </b-modal>
    </div>
  </div>
</template>
<script>
import Video from '@/components/Video'
import BankList from '@/components/BankList'
import StepProgress from 'vue-step-progress'
import '@/css/step-progress.css'

// APIs
import ConsentAPI from '@/assets/api/consent'

export default {
  components: {
    Video,
    BankList,
    'step-progress': StepProgress
  },
  data () {
    return {
      value: 0,
      maxProgress: 0,
      cardsChecked: [],
      isImageModalActive: false,
      haveCheckBox: true,
      line1: 'Select',
      line2: 'Accounts',
      isActiveTab: 0,
      consentData: null,
      isLoading: false,
      progressSteps: [
        this.$t('stepProgressWhy'),
        this.$t('stepProgressBanks'),
        this.$t('stepProgressWhat'),
        this.$t('stepProgressHowLong'),
        this.$t('stepProgressTillWhen')
      ],
      progressColor: '#03b072',
      currentStep: 0,
      isCardsDone: false,
      isBackButtonDisabled: false,
      isNextButtonDisabled: false,
      userReadFully: false,
      forceUserAction: false,
      isComponentModalActive: false,
      isFullyReadModalActive: false,
      isAcceptModalActive: false
    }
  },
  mounted () {
    this.checkButtonActiveState()
    this.getConsentData(this.$route.params)
  },
  methods: {
    openLoading () {
      console.log('Open Loading', this.isLoading)
      this.isLoading = true
      console.log('Open Loading', this.isLoading)
    },
    closeLoading () {
      console.log('Close Loading', this.isLoading)
      this.isLoading = false
      console.log('Close Loading', this.isLoading)
    },
    dashboardTabChanged (index) {
      this.isActiveTab = index
    },
    checkButtonActiveState () {
      this.isNextButtonDisabled = false
      this.isBackButtonDisabled = false
      if (this.currentStep === 4) {
        this.isNextButtonDisabled = true
      }
      if (this.currentStep === 0) {
        this.isBackButtonDisabled = true
      }
    },
    nextCard () {
      this.currentStep += 1
      this.checkButtonActiveState()
      if (this.currentStep === 4) {
        this.userReadFully = true
      }
    },
    previousCard () {
      this.currentStep -= 1
      this.checkButtonActiveState()
    },
    checkUserProgress () {},
    rejectConsent () {
      if (this.userReadFully || this.forceUserAction) {
        this.$router.go(-1)
        this.$buefy.snackbar.open({
          type: 'is-warning',
          message: 'Consent has been rejected successfully',
          queue: false
        })
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
    acceptConsent1 () {
      if (this.userReadFully) {
        this.isComponentModalActive = false
        this.isFullyReadModalActive = true
        this.startAnimation()
        const here = this
        setTimeout(function () {
          here.stopAnimation()
          here.$buefy.snackbar.open({
            type: 'is-success',
            message: 'Consent has been accepted successfully',
            queue: false
          })
          here.$router.go(-1)
        }, 3000)
      } else {
        this.isComponentModalActive = true
        this.forceUserAction = true
      }
    },
    acceptConsent2 () {
      this.isComponentModalActive = false
      this.isAcceptModalActive = true
      const here = this
      setTimeout(function () {
        here.$router.go(-1)
        here.$buefy.snackbar.open({
          type: 'is-success',
          message: 'Consent has been accepted successfully',
          queue: false
        })
      }, 3000)
    },
    onHover (card) {
      if (!this.cardsChecked.includes(card)) {
        this.cardsChecked.push(card)
      }
      if (this.cardsChecked.length === 3) {
        this.currentStep = 2
        this.isCardsDone = true
        if (this.maxProgress > 75) {
          this.currentStep = 3
        }
      }
    },
    getConsentData (params) {
      const here = this
      const payload = {}
      here.openLoading()
      ConsentAPI.postItem(payload, params.id)
        .then(function (response) {
          here.consentData = response.data
          here.closeLoading()
        })
        .catch((error) => {
          console.log(error)
          here.closeLoading()
          here.$buefy.snackbar.open({
            type: 'is-danger',
            message: 'Failed. Please Retry..',
            queue: false
          })
        })
    }
  }
}
</script>
<style scoped>
.content-right {
  height: 100%;
}
.content-left {
  height: 100%;
}
.pending-consent {
  background-color: #f26c63;
}
.active-consent {
  background-color: #99d25c;
}
.video {
  text-align: center;
}
.logo {
  max-width: 10rem;
}
.is-green {
  color: #03b072 !important;
  font-weight: bold;
}
.rows {
  margin: 0.5rem;
}
hr {
  display: block;
  height: 1px;
  border: 0;
  border-top: 1px solid #ccc;
  margin: 1em 0;
  padding: 0;
  opacity: 0.5;
}
.question {
  color: #f26c63;
  font-weight: bold;
  margin-bottom: 0.5rem;
}
.answer {
  color: #222222;
}
.reject {
  font-weight: bold;
  color: #666666;
}
.approve {
  font-weight: bold;
  color: #03b072;
}

.column1 {
  float: center;
  width: 33.33%;
  padding: 0.1em;
}
/* Clear floats after the columns */
.row:after {
  content: "";
  display: table;
  clear: both;
}
h1 {
  font-size: large;
  text-align: center;
  color: black;
}
h2 {
  font-size: medium;
  color: black;
}
.card1 {
  text-align: center;
  display: block;
  position: relative;
  max-width: auto;
  background-color: white;
  border-radius: 8px;
  padding: 10% 5%;
  margin: 12px;
  text-decoration: none;
  z-index: 0;
  overflow: hidden;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}
.hvrbox,
.hvrbox * {
  box-sizing: border-box;
}
.hvrbox {
  position: relative;
  display: inline-block;
  overflow: hidden;
  max-width: 100%;
  height: auto;
}
.hvrbox img {
  max-width: 50%;
}
.hvrbox .hvrbox-layer_bottom {
  display: block;
}
.hvrbox .hvrbox-layer_top {
  opacity: 0;
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  width: 100%;
  height: 100%;
  background: #d9dee8;
  font-size: 1vmin;
  color: #000000;
  padding: 15px;
  -moz-transition: all 0.4s ease-in-out 0s;
  -webkit-transition: all 0.4s ease-in-out 0s;
  -ms-transition: all 0.4s ease-in-out 0s;
  transition: all 0.4s ease-in-out 0s;
}
.hvrbox:hover .hvrbox-layer_top,
.hvrbox.active .hvrbox-layer_top {
  opacity: 1;
}
.hvrbox .hvrbox-text {
  text-align: center;
  font-size: 2.5vmin;
  display: inline-block;
  position: absolute;
  text-emphasis: bold;
  top: 50%;
  left: 50%;
  -moz-transform: translate(-50%, -50%);
  -webkit-transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
}
.hvrbox .hvrbox-text_mobile {
  font-size: 2.5vmin;
  border-top: 1px solid rgb(179, 179, 179); /* for old browsers */
  border-top: 1px solid rgba(179, 179, 179, 0.7);
  margin-top: 5px;
  padding-top: 2px;
  display: none;
}
.card-text {
  font-size: 2.5vmin;
}
.hvrbox.active .hvrbox-text_mobile {
  display: block;
}

.pending-button {
  text-decoration: none;
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
.not-read-consent {
  animation: shake 0.82s cubic-bezier(0.36, 0.07, 0.19, 0.97) both;
  transform: translate3d(0, 0, 0);
  backface-visibility: hidden;
  perspective: 1000px;
}
@keyframes shake {
  10%,
  90% {
    transform: translate3d(-1px, 0, 0);
  }

  20%,
  80% {
    transform: translate3d(2px, 0, 0);
  }

  30%,
  50%,
  70% {
    transform: translate3d(-4px, 0, 0);
  }

  40%,
  60% {
    transform: translate3d(4px, 0, 0);
  }
}
</style>
