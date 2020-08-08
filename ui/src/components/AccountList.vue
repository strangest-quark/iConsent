<template>
  <div class="accountList">
    <div class="add-account-button">
    <b-button icon-left="plus" type="is-text">{{$t('buttonAddAccount')}}</b-button>
    </div>
    <div>
      <ul class="vs full">
        <Account v-for="bank in $t('banks')" :bank="bank" :haveCheckBox="haveCheckBox" :key="bank.id" />
      </ul>
    </div>
  </div>
</template>

<script>
import Account from '@/components/Account'
export default {
  name: 'AccountList',
  components: {
    Account
  },
  props: {
    haveCheckBox: Boolean
  }
}
</script>

<style scoped>
.add-account-button{
  text-align: center !important;
}
.button{
    text-decoration: none;
}
</style>
