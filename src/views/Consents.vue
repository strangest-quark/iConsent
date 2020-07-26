<template>
  <div class="section is-fluid">
    <div v-if="isLoading" class="is-center">
      <bounce :loading="isLoading"></bounce>
    </div>
    <div v-if="!isLoading" class="columns is-multiline">
      <div class="column">
        <!-- <welcome-card /> -->
        <dashboard-nav pending=true active=true inactive=true paused=true revoked=true rejected=true @tabChanged="dashboardTabChanged" />
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
          <div v-else-if="isActiveTab === 3">
            <paused-consents :data="dashboardData.paused" />
          </div>
          <div v-else-if="isActiveTab === 4">
            <revoked-consents :data="dashboardData.revoked" />
          </div>
          <div v-else-if="isActiveTab === 5">
            <rejected-consents :data="dashboardData.rejected" />
          </div>
        </div>
      </div>
      <div class="column is-two-fifths content-right is-hidden-mobile">
        <div class="rows">
          <div class="row">
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
import Video from '@/components/Video'
// import WelcomeCard from '@/components/WelcomeCard'
import Chat from '@/components/Chat'

// Consents
import PendingConsents from '@/components/Consents/PendingConsents.vue'
import ActiveConsents from '@/components/Consents/ActiveConsents.vue'
import InactiveConsents from '@/components/Consents/InactiveConsents.vue'
import PausedConsents from '@/components/Consents/PausedConsents.vue'
import RejectedConsents from '@/components/Consents/RejectedConsents.vue'
import RevokedConsents from '@/components/Consents/RevokedConsents.vue'

// APIs
import DashboardAPI from '@/assets/api/dashboard'

export default {
  components: {
    DashboardNav,
    // ConsentCardComponent,
    Video,
    // WelcomeCard,
    Chat,
    PendingConsents,
    ActiveConsents,
    InactiveConsents,
    PausedConsents,
    RejectedConsents,
    RevokedConsents
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
  height: 74vh;
}
</style>
