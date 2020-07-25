/* Styles */
import '@/scss/main.scss'
import '@/css/bank.css'

/* Core */
import Vue from 'vue'
import Buefy from 'buefy'

/* Router & Store */
import router from './router'
import store from './store'

/* Service Worker */
import './registerServiceWorker'

/* Vue. Main component */
import App from './App.vue'

// Language Support
import i18n from '@/plugins/i18n'

import FlagIcon from 'vue-flag-icon'

Vue.use(FlagIcon)

/* Default title tag */
const defaultDocumentTitle = 'iConsent - oneMoney AA'

/* Collapse mobile aside menu on route change & set document title from route meta */
router.afterEach(to => {
  store.commit('asideMobileStateToggle', false)

  if (to.meta && to.meta.title) {
    document.title = `${to.meta.title} — ${defaultDocumentTitle}`
  } else {
    document.title = defaultDocumentTitle
  }
})

Vue.config.productionTip = false

Vue.use(Buefy)

new Vue({
  router,
  store,
  i18n,
  watch: {
    $route: () => {
      window.Appcues.page()
      window.Appcues.anonymous()
    }
  },
  render: h => h(App)
}).$mount('#app')
