<template>
  <div class="account">
    <div class="accountLogo">
      <b-checkbox v-if="haveCheckBox" class="checkbox"  :value="true" type="is-success"></b-checkbox>
      <img :src="require('@/assets/' + bank.imgName)" />
    </div>
    <div class="accountDetails">
      <h1>
        <strong>{{bank.name}}</strong>
      </h1>
      <small><strong>{{bank.accType}}</strong></small><br/>
      <small>ending {{bank.accNo}}</small>
    </div>
    <div class="accountConsents">
      <h1>
        <strong>2</strong>
      </h1>
      <small><strong>Linked Consents</strong></small><br/>
    </div>
    <a href="https://www.google.com">Delink</a>
  </div>
</template>

<script>
export default {
  props: {
    bank: Object,
    haveCheckBox: Boolean
  }
}
</script>
