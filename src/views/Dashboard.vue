<template>
  <div class="section is-fluid">
    <div class="columns is-multiline">
      <div class="column content-left">
            <welcome-card/>
        <dashboard-nav />
        <div class="dashboard-consents">
        <div v-for="i in 3" :key="i" >
          <consent-card-component
            title="Performance"
            icon="finance"
          >
            <div class="rows">
              <div class="row columns is-mobile is-vcentered">
                <div class="logo column" align="left">
                  <img src="@/assets/FIU_Logo/quickbooks.jpg" />
                </div>
                <div class="column is-gray" align="right">
                  Verified
                  <b-icon icon="shield-check" custom-size="default" />
                </div>
              </div>
              <div class="row">
                <h2
                  class="title is-6"
                >Intuit quickbooks is requesting for access to your banking data</h2>
              </div>
               <div class="row columns my-1">
                <div class="column is-gray" align="left">
                  <h2 class="is-7">Valid till 20 Oct 2020</h2>
                </div>
              </div>
              <div class="row columns is-mobile">
                <div @click="isImageModalActive = true" class="play-video-trigger column" align="left">
                  <b-icon icon="play-circle" size="is-small" />
                  <a class="is-6">How does it work?</a>
                </div>
                 <div class="column is-gray is-two-fifths" align="right">
                  <h2 class="is-8">Report Fraud</h2>
                </div>
              </div>
            </div>
          </consent-card-component>
          <p></p>
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
                :number="3"
                label="ConsentsPending"
              />
              <card-widget
                class="column tile is-child active-consent"
                type="is-info"
                icon="cart-outline"
                :number="2"
                label="ConsentsActive"
              />
            </tiles>
          </div>
          <div class="row" style="padding-top: 5%">
            <BankList :line1="line1" :line2="line2" :haveCheckBox="false"/>
          </div>
          <div style="margin-top: 10vh" class="row">
            <Chat style="padding: 4% 4% 4% 0%"/>
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
import ConsentCardComponent from '@/components/ConsentCardComponent'
import Tiles from '@/components/Tiles'
import CardWidget from '@/components/CardWidget'
import BankList from '@/components/BankList'
import Video from '@/components/Video'
import WelcomeCard from '@/components/WelcomeCard'
import Chat from '@/components/Chat'

export default {
  components: {
    DashboardNav,
    ConsentCardComponent,
    Tiles,
    CardWidget,
    BankList,
    Video,
    WelcomeCard,
    Chat
  },
  data () {
    return {
      isImageModalActive: false,
      haveCheckBox: false,
      line1: 'Your',
      line2: 'Accounts'
    }
  }
}
</script>

<style scoped>
.content-right {
  /* border-left: 1px solid red; */
  height: 100%;
  margin-left: 2rem;
}
.content-left {
  /* border-right: 1px solid red; */
  height: 100%;
  /* margin-right: 2rem; */
}
.pending-consent {
  background-color: #f26c63;
}
.active-consent {
  background-color: #acacac;
}
.is-gray {
  color: #acacac !important;
}
.play-video-trigger,
.play-video-trigger a {
  color: #f26c63;
  font-weight: bold;
}

.video {
  text-align: center;
}

.dashboard-consents{
  overflow-y: scroll;
  height:50vh;
}

</style>
