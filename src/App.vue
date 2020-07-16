<template>
  <div id="app">
    <nav-bar />
    <aside-menu />
    <router-view />
  </div>
</template>

<script>
// @ is an alias to /src
import NavBar from '@/components/NavBar'
import AsideMenu from '@/components/AsideMenu'

export default {
  name: 'home',
  components: {
    AsideMenu,
    NavBar
  },
  beforeCreate () {
    if (
      sessionStorage.getItem('user-phonenumber') === null &&
      sessionStorage.getItem('user-sessionId') === null
    ) {
      this.$router.push('/sign-in').catch(() => {})
    }
  }
}
</script>
