<template>
    <div class="accounts">
        <!-- <h1> Accounts </h1> -->
        <div class="row" style="padding-top: 5%">
            <AccountList :line1="line1" :line2="line2" :haveCheckBox="false" />
        </div>
    </div>
</template>

<script>
import AccountList from '@/components/AccountList'

export default {
  components: {
    AccountList
  },
  data () {
    return {
      isImageModalActive: false,
      haveCheckBox: false,
      line1: 'scrollTitleYour',
      line2: 'scrollTitleAccounts',
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
  }
}
</script>

<style scoped>
.accounts h1 {
    position: fixed;
    left: 50%;
    transform: translate(-50%, 0);
    font-size: x-large;
}
</style>
