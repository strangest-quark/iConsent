<template>
  <div class="card">
    <div class="row">
      <div class="left">
        <div class="container">
          <h1>
            <b>{{$t('chatNeedHelp')}}</b>
          </h1>
          <p>
            {{$t('chatSubtitle')}}
          </p>
          <b-button type="is-link" style="margin-top: 5%">{{$t('buttonChat')}}</b-button>
        </div>
      </div>
      <div class="right">
        <img src="@/assets/chat-icon.png" alt="Avatar" />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Chat'
}
</script>

<style scoped>
.card {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  background-color: #f5f5f7;
  transition: 0.3s;
  width: 100%;
  height: 30%;
}
.card:hover {
  box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
}
.container {
  padding-left: 10%;
}
.row {
  display: flex;
}

img {
  width: 100%;
}

.left {
  flex: 60%;
  margin-top: auto;
  margin-bottom: auto;
}

.right {
  width: 30%;
}

h1 {
  font-size: large;
}

p {
  font-size: medium;
  padding-top: 1%;
}
</style>
