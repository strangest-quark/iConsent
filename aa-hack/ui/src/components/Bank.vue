<template>
  <div class="item">
    <b-checkbox v-if="haveCheckBox" class="checkbox"  :value="true" type="is-success"></b-checkbox>
    <img :src="bank.fip_logo" style="height:10vh" />
    <h1>
      <strong>{{bank.fip_name}}</strong>
    </h1>
    <small v-if="haveType">{{bank.fip_accType}}</small>
    <small>{{bank.endingNumber}}</small>
  </div>
</template>

<script>
export default {
  props: {
    bank: Object,
    haveCheckBox: Boolean,
    haveType: Boolean
  }
}
</script>
