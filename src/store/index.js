import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    /* User */
    userName: null,
    userEmail: null,
    userAvatar: null,

    /* NavBar */
    isNavBarVisible: true,

    /* Aside */
    isAsideVisible: true,
    isAsideMobileExpanded: false
  },
  mutations: {
    /* A fit-them-all commit */
    basic (state, payload) {
      state[payload.key] = payload.value
    },

    /* User */
    user (state, payload) {
      if (payload.name) {
        state.userName = payload.name
      }
      if (payload.email) {
        state.userEmail = payload.email
      }
      if (payload.avatar) {
        state.userAvatar = payload.avatar
      }
    },

    /* Aside Mobile */
    asideMobileStateToggle (state, payload = null) {
      const htmlClassName = 'has-aside-mobile-expanded'

      let isShow

      if (payload !== null) {
        isShow = payload
      } else {
        isShow = !state.isAsideMobileExpanded
      }

      if (isShow) {
        document.documentElement.classList.add(htmlClassName)
      } else {
        document.documentElement.classList.remove(htmlClassName)
      }

      state.isAsideMobileExpanded = isShow
    },

    // login page hide left
    asideHolderHide (state, payload = null) {
      const htmlClassName1 = 'has-aside-left'
      const htmlClassName2 = 'has-aside-expanded'
      const htmlClassName3 = 'has-navbar-fixed-top'
      const htmlClassName4 = 'has-aside-mobile-transition'

      let isShow

      if (payload !== null) {
        isShow = payload
      } else {
        isShow = !state.isAsideVisible
      }

      if (isShow) {
        document.documentElement.classList.add(htmlClassName1, htmlClassName2, htmlClassName3, htmlClassName4)
      } else {
        document.documentElement.classList.remove(htmlClassName1, htmlClassName2, htmlClassName3, htmlClassName4)
      }

      state.isAsideVisible = isShow
      state.isNavBarVisible = isShow
    }
  },
  actions: {

  }
})
