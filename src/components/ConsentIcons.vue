<template>
  <div class="row">
    <div class="column">
      <div class="hvrbox">
        <a class="card1" href="#">
          <img src="@/assets/periodic.png"/>
          <h1>Periodic</h1>
          <div class="hvrbox-layer_top">
            <h2 class="hvrbox-text"><b>Periodic fetch of data</b></h2>
          </div>
        </a>
      </div>
    </div>
    <div class="column">
      <div class="hvrbox">
        <a class="card1" href="#">
          <img src="@/assets/stream.png"/>
          <h1>View</h1>
          <div class="hvrbox-layer_top">
            <h2 class="hvrbox-text"><b>View your data</b></h2>
          </div>
        </a>
      </div>
    </div>
    <div class="column">
      <div class="hvrbox">
        <a class="card1" href="#">
          <img src="@/assets/summary.png"/>
          <h1>Summary</h1>
          <div class="hvrbox-layer_top">
            <h2 class="hvrbox-text"><b>Summary data view</b></h2>
          </div>
        </a>
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
.column {
  float: center;
  width: 33.33%;
  padding: 0.1em;
}

/* Clear floats after the columns */
.row:after {
  content: "";
  display: table;
  clear: both;
}
h1{
  font-size: large;
  text-align: center;
  color: black;
}
h2{
  font-size: medium;
  text-align: center;
  color: black;
}
img{
  width: 50%;
}
.card1 {
  text-align: center;
  display: block;
  position: relative;
  max-width: auto;
  background-color: white;
  border-radius: 8px;
  padding: 10% 5%;
  margin: 12px;
  text-decoration: none;
  z-index: 0;
  overflow: hidden;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}
.hvrbox,
.hvrbox * {
  box-sizing: border-box;
}
.hvrbox {
  position: relative;
  display: inline-block;
  overflow: hidden;
  max-width: 100%;
  height: auto;
}
.hvrbox img {
  max-width: 100%;
}
.hvrbox .hvrbox-layer_bottom {
  display: block;
}
.hvrbox .hvrbox-layer_top {
  opacity: 0;
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  width: 100%;
  height: 100%;
  background: #D9DEE8;
  color: #000000;
  padding: 15px;
  -moz-transition: all 0.4s ease-in-out 0s;
  -webkit-transition: all 0.4s ease-in-out 0s;
  -ms-transition: all 0.4s ease-in-out 0s;
  transition: all 0.4s ease-in-out 0s;
}
.hvrbox:hover .hvrbox-layer_top,
.hvrbox.active .hvrbox-layer_top {
  opacity: 1;
}
.hvrbox .hvrbox-text {
  text-align: center;
  font-size: 16px;
  display: inline-block;
  position: absolute;
  text-emphasis: bold;
  top: 50%;
  left: 50%;
  -moz-transform: translate(-50%, -50%);
  -webkit-transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
}
.hvrbox .hvrbox-text_mobile {
  font-size: 15px;
  border-top: 1px solid rgb(179, 179, 179); /* for old browsers */
  border-top: 1px solid rgba(179, 179, 179, 0.7);
  margin-top: 5px;
  padding-top: 2px;
  display: none;
}
.hvrbox.active .hvrbox-text_mobile {
  display: block;
}
</style>
