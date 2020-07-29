<template>
  <div class="section is-fluid">
    <div v-if="isLoading" class="is-center">
      <bounce :loading="isLoading"></bounce>
    </div>
    <div v-if="!isLoading" class="columns is-multiline">
      <div class="column">
        <b-button
          @click="$router.go(-1)"
          class="pending-button"
          icon-left="chevron-left"
          type="is-text"
        >Pending</b-button>
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
                    <!-- what -->
                    <div v-if="currentStep==2" class="rows">
                      <span class="row">
                        <h2 class="question subtitle is-6">{{consentData.q3}}</h2>
                      </span>
                      <div class="row" style="width: 100%">
                        <div style="padding: 1% 4% 0% 0%">
                          <div class="row">
                            <div class="column1">
                              <div class="hvrbox">
                                <a @mouseover="onHover('card1')" class="card1" href="#">
                                  <img :src="consentData.card1_icon" />
                                  <h2 class="card-text">
                                    <b>{{consentData.card1}}</b>
                                  </h2>
                                  <div class="hvrbox-layer_top">
                                    <h2 class="hvrbox-text">
                                      <b>{{consentData.hover1}}</b>
                                    </h2>
                                  </div>
                                </a>
                              </div>
                            </div>
                            <div class="column1">
                              <div class="hvrbox">
                                <a @mouseover="onHover('card2')" class="card1" href="#">
                                  <img :src="consentData.card2_icon" />
                                  <h2 class="card-text">
                                    <b>{{consentData.card2}}</b>
                                  </h2>
                                  <div class="hvrbox-layer_top">
                                    <h2 class="hvrbox-text">
                                      <b>{{consentData.hover2}}</b>
                                    </h2>
                                  </div>
                                </a>
                              </div>
                            </div>
                            <div @mouseover="onHover('card3')" class="column1">
                              <div class="hvrbox">
                                <a @mouseover="onHover" class="card1" href="#">
                                  <img :src="consentData.card3_icon" />
                                  <h2 class="card-text">
                                    <b>{{consentData.card3}}</b>
                                  </h2>
                                  <div class="hvrbox-layer_top">
                                    <h2 class="hvrbox-text">
                                      <b>{{consentData.hover3}}</b>
                                    </h2>
                                  </div>
                                </a>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                    <!-- till when -->
                    <div v-if="currentStep==3" class="rows">
                      <span class="row">
                        <h2 class="question subtitle is-6">{{consentData.q4}}</h2>
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
                    <b-button v-if="isBackButtonDisabled" disabled>Back</b-button>
                    <b-button v-else @click="previousCard">Back</b-button>
                  </div>
                  <div class="column" align="right">
                    <b-button v-if="isNextButtonDisabled" disabled type="is-primary">Next</b-button>
                    <b-button v-else @click="nextCard" type="is-primary">Next</b-button>
                  </div>
                </div>
              </div>
              <div class="row is-hidden-desktop is-hidden-tablet">
                <BankList :line1="line1" :line2="line2" :haveCheckBox="haveCheckBox" />
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="column is-half content-right is-hidden-mobile" style="padding-left: 5%">
        <div class="rows">
          <div class="row">
            <BankList :line1="line1" :line2="line2" :haveCheckBox="haveCheckBox" />
          </div>
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
            >Reject</b-button>
          </div>
          <div class="column" align="left">
            <b-button
              type="is-rounded"
              class="approve"
              size="is-medium"
              @click="acceptConsent"
              icon-left="check-circle-outline"
            >Approve</b-button>
          </div>
        </div>
      </div>
    </div>
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
              <div class="logo column" align="center">
                <img :src="consentData.fiu_logo" />
              </div>
            </div>

            <h4 class="title is-6">Quickbooks can now access your savings accounts!</h4>
          </div>
        </section>
      </div>
    </b-modal>
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
        this.$t('stepProgressHowLong'),
        this.$t('stepProgressWhat'),
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
      isFullyReadModalActive: false
    }
  },
  methods: {
    openLoading () {
      this.isLoading = true
    },
    closeLoading () {
      this.isLoading = false
    },
    dashboardTabChanged (index) {
      this.isActiveTab = index
    },
    checkButtonActiveState () {
      this.isNextButtonDisabled = false
      this.isBackButtonDisabled = false
      if (this.currentStep === 3) {
        this.isNextButtonDisabled = true
      }
      if (this.currentStep === 0) {
        this.isBackButtonDisabled = true
      }
    },
    nextCard () {
      this.currentStep += 1
      this.checkButtonActiveState()
      if (this.currentStep === 3) {
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
      ConsentAPI.postItem(payload, params.id, params.fiu)
        .then(function (response) {
          console.log(response)
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
  },
  mounted () {
    const here = this
    here.openLoading()
    here.checkButtonActiveState()
    here.getConsentData(this.$route.params)
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
  color: #079aff;
  font-weight: bold;
  margin-bottom: 0.5rem;
}
.answer {
  color: #222222;
}
.reject {
  font-weight: bold;
  color: #e11a50;
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
</style>
