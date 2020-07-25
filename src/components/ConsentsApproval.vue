<template>
  <div class="section is-fluid">
    <div v-if="isLoading" class="is-center">
      <bounce :loading="isLoading"></bounce>
    </div>
    <div v-if="!isLoading" class="columns is-multiline">
      <div class="column">
        <b-button icon-left="chevron-left" type="is-light">Pending</b-button>
        <div>
          <div class="rows">
            <div class="row columns is-mobile is-vcentered">
              <div class="logo column" align="left">
                <img src="@/assets/FIU_Logo/quickbooks.jpg" />
              </div>
              <div class="column is-green" align="right">
                Verified
                <b-icon icon="shield-check" custom-size="default" />
              </div>
            </div>
            <div class="row">
              <h2 class="title is-5">Quickbooks wants to access your something</h2>
            </div>
            <hr />
            <div class="row">
              <div class="rows">
                <span class="row">
                  <h2 class="question subtitle is-6">Why does quickbook needs this data?</h2>
                </span>
                <span class="row">
                  <p class="answer">Explicit consent for something</p>
                </span>
              </div>
            </div>
            <hr />
            <div class="row">
              <div class="rows">
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
              </div>
            </div>
            <hr />
            <div class="row">
              <BankList :line1="line1" :line2="line2" :haveCheckBox="false" />
            </div>

            <hr />
            <div class="row">
              <div class="rows">
                <span class="row">
                  <h2 class="question subtitle is-6">Till when this consent is valid?</h2>
                </span>
                <span class="row">
                  <p class="answer">
                    Valid till
                    <strong>06 July 2021</strong>
                  </p>
                </span>
              </div>
            </div>
            <hr />
          </div>
        </div>
      </div>
      <div class="column is-half content-right is-hidden-mobile">
        <div class="rows">
          <div class="row">
            <consent-icons style="padding: 4% 4% 4% 0%" />
          </div>
          <div class="row">
            <Video />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Video from '@/components/Video'
import ConsentIcons from '@/components/ConsentIcons'
import BankList from '@/components/BankList'

// APIs
import DashboardAPI from '@/assets/api/dashboard'

export default {
  components: {
    Video,
    ConsentIcons,
    BankList
  },
  data () {
    return {
      isImageModalActive: false,
      haveCheckBox: false,
      line1: 'Your',
      line2: 'Accounts',
      isActiveTab: 0,
      dashboardData: null,
      isLoading: false
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
    }
  },
  mounted () {
    const here = this
    here.openLoading()
    const payload = {}
    DashboardAPI.postItem(payload)
      .then(function (response) {
        here.dashboardData = response.data
        here.closeLoading()
      })
      .catch(error => {
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
</script>

<style scoped>
.content-right {
  height: 100%;
  /* margin-left: 2rem; */
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

.dashboard-consents {
  overflow-y: scroll;
  height: 74vh;
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
</style>
