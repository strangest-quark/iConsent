<template>
  <div class="item">
    <b-checkbox v-if="haveCheckBox" class="checkbox"  :value="true" type="is-success"></b-checkbox>
    <img :src="require('@/assets/' + bank.imgName)" style="height:45px; margin-bottom: 10px;" />
    <h1>
      <strong>{{bank.name}}</strong>
    </h1>
    <small>{{bank.accType}}</small>
    <small>
      <i>Ending {{bank.accNo}}</i>
    </small>
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
