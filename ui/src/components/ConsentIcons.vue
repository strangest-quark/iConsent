<template>
<div>
  <div style="width: 100%">
    <div class="row">
      <div class="column"><img src="@/assets/periodic.png" /></div>
      <div class="column"><img src="@/assets/view.png" /></div>
      <div class="column"><img src="@/assets/summary.png" /></div>
    </div>
    <div class="row" style="display: table; padding-top: 5%">
      <h1>Quickbooks will periodically fetch your transactions data every week.This data will be stored only for 1 month</h1>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: 'ConsentIcons'
}
</script>

<style scoped>
* {
  box-sizing: border-box;
}
.row{
    width: 100%;
    height: 100%;
    text-align: center;
}
.column {
  float: center;
  width: 33.33%;
  padding: 0.1em;
}

h1{
  font-size: 2vmax;
  text-align: center;
  color: black;
  display: table-cell;
}
h2{
  font-size: medium;
  text-align: center;
  color: black;
}
img{
  width: 60%;
}
</style>
