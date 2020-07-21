<template>
  <div class="row">
    <div class="left">
      <h1>
        Select
        <br />Accounts
      </h1>
    </div>
    <div class="right">
      <div class="banklist">
        <ul class="hs full">
          <Bank v-for="bank in banks" :bank="bank" :haveCheckBox="haveCheckBox" :key="bank.id" />
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import Bank from '@/components/Bank'
export default {
  name: 'BankList',
  components: {
    Bank
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
      ],
      haveCheckBox: false
    }
  }
}
</script>
