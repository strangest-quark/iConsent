<template>
  <div id="app">
    <nav-bar />
    <aside-menu :menu="menu" />
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
  computed: {
    menu () {
      return [
        {
          id: 1,
          label: 'Pending',
          icon: 'clock',
          path: '/pending-consents',
          class: 'active',
          type: 'consent'
        },
        {
          id: 2,
          label: 'Active',
          icon: 'file',
          path: '/active-consents',
          class: '',
          type: 'consent'
        },
        {
          id: 3,
          label: 'Paused',
          icon: 'pause',
          path: '/paused-consents',
          class: '',
          type: 'consent'
        },
        {
          id: 4,
          label: 'Inactive',
          icon: 'stop',
          path: '/inactive-consents',
          class: '',
          type: 'consent'
        },
        {
          id: 5,
          label: 'Linked',
          icon: 'link',
          path: '/linked-accounts',
          class: '',
          type: 'account'
        },
        {
          id: 6,
          label: 'Active',
          icon: 'layers-off',
          path: '/delinked-accounts',
          class: '',
          type: 'account'
        }
      ]
    }
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
