<template>
  <div class="account columns is-vcentered">
    <div class="accountLogo column">
      <b-checkbox v-if="haveCheckBox" class="checkbox"  :value="true" type="is-success"></b-checkbox>
      <img :src="require('@/assets/' + bank.imgName)" />
    </div>
    <div class="accountDetails column">
      <h1>
        <strong>{{bank.name}}</strong>
      </h1>
      <small><strong>{{bank.accType}}</strong></small><br/>
      <small>XX{{bank.accNo}}</small>
    </div>
    <div class="accountConsents column">
      <h1>
        <strong>2</strong>
      </h1>
      <small><strong>Linked Consents</strong></small><br/>
    </div>
    <div class="column">
      <b-button class="delink-button" type="is-text"> Delink </b-button>
    </div>
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

<style scoped>
.delink-button{
  color: #079AFF !important
}
</style>
