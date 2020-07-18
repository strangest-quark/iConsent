<template>
  <div class="item">
    <input type="checkbox" id="checkbox" v-model="checked" />
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
    bank: Object
  }
}
</script>
