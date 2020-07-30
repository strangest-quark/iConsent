<template>
  <div class="accountList">
    <b-button icon-left="chevron-left" type="is-light">Add Account</b-button>
    <div>
      <div>
        <div>
          <ul class="vs full">
            <Account v-for="bank in banks" :bank="bank" :haveCheckBox="haveCheckBox" :key="bank.id" />
          </ul>
        </div>
      </div>
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
  },
  data () {
    return {
      banks: [
        {
          id: 1,
          name: 'Citibank',
          imgName: 'citi.png',
          accType: 'Savings',
          accNo: 4545
        },
        {
          id: 2,
          name: 'HDFC Bank',
          imgName: 'hdfc.png',
          accType: 'Loan',
          accNo: 3455
        },
        {
          id: 3,
          name: 'Axis Bank',
          imgName: 'axis.png',
          accType: 'Savings',
          accNo: 9545
        }
      ]
    }
  }
}
</script>
