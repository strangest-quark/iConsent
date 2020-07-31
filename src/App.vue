<template>
  <div id="app">
    <nav-bar :userName="userName()" />
    <aside-menu />
    <router-view />
  </div>
</template>

<script>
// @ is an alias to /src
import NavBar from '@/components/NavBar'
import AsideMenu from '@/components/AsideMenu'
import i18n from '@/plugins/i18n'

/* EventBus */
import EventBus from '@/eventBus'

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
    if (localStorage.getItem('user-language') === null) {
      const language = navigator.userLanguage || navigator.language
      localStorage.setItem('user-language', language)
      EventBus.$emit('current_user_language', language)
      i18n.locale = language
    }
  },
  methods: {
    userName () {
      return sessionStorage.getItem('user-name')
    }
  }
}
</script>
