<template>
  <div class="section is-fluid">
    <div v-if="isLoading" class="is-center">
      <bounce :loading="isLoading"></bounce>
    </div>
    <div v-if="!isLoading" class="columns is-multiline">
      <div class="column content-left">
        <!-- <welcome-card /> -->
        <dashboard-nav pending=true active=true inactive=true @tabChanged="dashboardTabChanged" />
        <div class="dashboard-consents">
          <div v-if="isActiveTab === 0">
            <pending-consents :data="dashboardData.pending" />
          </div>
          <div v-else-if="isActiveTab === 1">
            <active-consents :data="dashboardData.active" />
          </div>
          <div v-else-if="isActiveTab === 2">
            <inactive-consents :data="dashboardData.inactive" />
          </div>
        </div>
      </div>
      <div class="column is-two-fifths content-right is-hidden-mobile">
        <div class="rows">
          <div class="row">
            <tiles>
              <card-widget
                class="column tile is-child pending-consent"
                type="is-primary"
                icon="account-multiple"
                :number="dashboardData.pending.length"
                label="ConsentsPending"
              />
              <card-widget
                class="column tile is-child active-consent"
                type="is-info"
                icon="cart-outline"
                :number="dashboardData.active.length"
                label="ConsentsActive"
              />
            </tiles>
          </div>
          <div class="row" style="padding-top: 5%">
            <BankList :line1="line1" :line2="line2" :haveCheckBox="false" />
          </div>
          <div style="margin-top: 12vh" class="row">
            <Chat style="padding: 4% 4% 4% 0%" />
          </div>
        </div>
      </div>
      <b-modal class="video" :active.sync="isImageModalActive">
        <Video />
      </b-modal>
    </div>
  </div>
</template>

<script>
import DashboardNav from '@/components/DashboardNav'
import Tiles from '@/components/Tiles'
import CardWidget from '@/components/CardWidget'
import BankList from '@/components/BankList'
import Video from '@/components/Video'
// import WelcomeCard from '@/components/WelcomeCard'
import Chat from '@/components/Chat'

// Consents
import PendingConsents from '@/components/Consents/PendingConsents.vue'
import ActiveConsents from '@/components/Consents/ActiveConsents.vue'
import InactiveConsents from '@/components/Consents/InactiveConsents.vue'

// APIs
import DashboardAPI from '@/assets/api/dashboard'

export default {
  components: {
    DashboardNav,
    // ConsentCardComponent,
    Tiles,
    CardWidget,
    BankList,
    Video,
    // WelcomeCard,
    Chat,
    PendingConsents,
    ActiveConsents,
    InactiveConsents
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
  margin-left: 2rem;
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
  height: 73vh;
}
</style>
