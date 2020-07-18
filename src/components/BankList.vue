<template>
  <div class="banklist">
    <ul class="hs full">
      <div class="item-one">
        <h2>
          Select
          <br />Accounts
        </h2>
      </div>
      <Bank v-for="bank in banks" :bank="bank" :key="bank.id" />
    </ul>
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
      ]
    }
  }
}
</script>
