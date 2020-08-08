<template>
  <div class="row">
    <div v-if="haveSide" class="left" style="padding-right: 5%">
      <h1>
        {{$t(line1)}}
        <br />
        {{$t(line2)}}
      </h1>
    </div>
    <div class="right">
      <div class="banklist">
        <ul :style="dynamicHorizontalContent" class="hs full">
          <Bank
            v-for="(bank, index) in accounts"
            :bank="bank"
            :haveCheckBox="haveCheckBox"
            :haveType="haveType"
            :key="`bank-${index}`"
          />
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
  computed: {
    dynamicHorizontalContent () {
      return {
        display: 'grid',
        'grid-gap': 'calc(var(--gutter) / 2)',
        'grid-template-columns':
          `20px repeat(${this.accounts.length}, calc(50% - var(--gutter) * 2)) 10px`,
        'grid-template-rows': 'minmax(150px, 1fr)',
        'overflow-x': scroll,
        'scroll-snap-type': 'x proximity',
        'padding-bottom': 'calc(0.75 * var(--gutter))',
        'margin-bottom': 'calc(-0.5 * var(--gutter))'
      }
    }
  },
  props: {
    line1: String,
    line2: String,
    haveCheckBox: Boolean,
    haveType: Boolean,
    accounts: Array,
    haveSide: Boolean
  },
  data () {
    return {
      banks: [
        {
          id: 1,
          name: 'Citibank',
          imgName: 'citi.png',
          accType: 'Savings',
          accNo: 'xx4545'
        },
        {
          id: 2,
          name: 'HDFC',
          imgName: 'hdfc.png',
          accType: 'Loan',
          accNo: 'xx3455'
        },
        {
          id: 3,
          name: 'Axis',
          imgName: 'axis.png',
          accType: 'Savings',
          accNo: 'xx9545'
        }
      ]
    }
  }
}
</script>

<style scoped>
.hs:before,
.hs:after {
  content: "";
}
</style>
