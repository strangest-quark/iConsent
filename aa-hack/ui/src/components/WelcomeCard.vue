<template>
  <div class="card">
    <div class="row">
      <div class="left">
        <div class="container">
          <h1>
            <b>Hi Ikram!</b>
          </h1>
          <p>Good to see you again.</p>
        </div>
      </div>
      <div class="right">
        <img src="@/assets/Mask Group.png" alt="Avatar" style="width:100%" />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'WelcomeCard'
}
</script>

<style scoped>
.card {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  background-color: #c7ee9d;
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

.left {
  flex: 70%;
  margin-top: auto;
  margin-bottom: auto;
}

.right {
  width: 30%;
}

h1 {
  font-size: 2rem;
}

p {
  font-size: 1rem;
}

img {
  max-width: 100%;
  height: 100%;
}
</style>
