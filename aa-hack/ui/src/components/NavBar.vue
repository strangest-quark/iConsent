<template>
  <nav v-if="isNavBarVisible" id="navbar-main" class="navbar is-fixed-top">
    <div class="navbar-brand">
      <a class="navbar-item is-hidden-desktop" @click.prevent="menuToggleMobile">
        <b-icon :icon="menuToggleMobileIcon" />
      </a>
      <div class="navbar-item has-control no-left-space-touch">
        <!-- <div class="control">
          <input class="input" placeholder="Search everywhere..." />
        </div> -->
      </div>
    </div>
    <div class="navbar-brand is-right">
      <a
        class="navbar-item navbar-item-menu-toggle is-hidden-desktop"
        @click.prevent="menuNavBarToggle"
      >
        <b-icon :icon="menuNavBarToggleIcon" custom-size="default" />
      </a>
    </div>
    <div class="navbar-menu fadeIn animated faster" :class="{'is-active':isMenuNavBarActive}">
      <div class="navbar-end">
        <!-- <div class="navbar-brand">
          <a class="navbar-item navbar-item-menu-toggle" @click.prevent="menuNavBarToggle">
            <b-icon icon="bell" size="is-default" />
          </a>
        </div>-->
        <nav-bar-menu class="has-divider has-user-avatar">
          <user-avatar />
          <div class="is-user-name">
            <span>{{ userName }}</span>
          </div>

          <div slot="dropdown" class="navbar-dropdown">
            <router-link to="/profile" class="navbar-item" exact-active-class="is-active">
              <b-icon icon="account" custom-size="default" />
              <span>My Profile</span>
            </router-link>
            <a disabled class="navbar-item">
              <b-icon icon="settings" custom-size="default"></b-icon>
              <span>Settings</span>
            </a>
            <!-- <a class="navbar-item">
              <b-icon icon="email" custom-size="default"></b-icon>
              <span>Messages</span>
            </a> -->
            <hr class="navbar-divider" />
            <a @click="signOut" class="navbar-item">
              <b-icon icon="logout" custom-size="default"></b-icon>
              <span>Sign Out</span>
            </a>
          </div>
        </nav-bar-menu>
      </div>
    </div>
  </nav>
</template>

<script>
import { mapState } from 'vuex'
import NavBarMenu from '@/components/NavBarMenu'
import UserAvatar from '@/components/UserAvatar'

export default {
  name: 'NavBar',
  components: {
    UserAvatar,
    NavBarMenu
  },
  props: {
    userName: String
  },
  data () {
    return {
      isMenuNavBarActive: false
    }
  },
  computed: {
    menuNavBarToggleIcon () {
      return this.isMenuNavBarActive ? 'close' : 'dots-vertical'
    },
    menuToggleMobileIcon () {
      return this.isAsideMobileExpanded ? 'backburger' : 'forwardburger'
    },
    ...mapState(['isNavBarVisible', 'isAsideMobileExpanded'])
  },
  methods: {
    // userName () {
    //   return sessionStorage.getItem('user-name')
    // },
    menuToggleMobile () {
      this.$store.commit('asideMobileStateToggle')
    },
    menuNavBarToggle () {
      this.isMenuNavBarActive = !this.isMenuNavBarActive
    },
    signOut () {
      sessionStorage.removeItem('user-phonenumber')
      sessionStorage.removeItem('user-sessionId')
      this.$router.push('/sign-in').catch(() => {})
    }
  }
}
</script>
