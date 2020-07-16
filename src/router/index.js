import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import SignIn from '../views/SignIn.vue'
import PendingConsents from '../views/PendingConsents.vue'
import ActiveConsents from '../views/ActiveConsents.vue'
import PausedConsents from '../views/PausedConsents.vue'
import InactiveConsents from '../views/InactiveConsents.vue'
import LinkedAccounts from '../views/LinkedAccounts.vue'
import DelinkedAccounts from '../views/DelinkedAccounts.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/sign-in',
    name: 'sign-in',
    component: SignIn
  },
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/pending-consents',
    name: 'pending-consents',
    component: PendingConsents
  },
  {
    path: '/active-consents',
    name: 'active-consents',
    component: ActiveConsents
  },
  {
    path: '/paused-consents',
    name: 'paused-consents',
    component: PausedConsents
  },
  {
    path: '/inactive-consents',
    name: 'inactive-consents',
    component: InactiveConsents
  },
  {
    path: '/linked-accounts',
    name: 'linked-accounts',
    component: LinkedAccounts
  },
  {
    path: '/delinked-accounts',
    name: 'delinked-accounts',
    component: DelinkedAccounts
  }
]

const router = new VueRouter({
  base: process.env.BASE_URL,
  mode: 'history',
  routes,
  scrollBehavior (to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else {
      return { x: 0, y: 0 }
    }
  }
})

function getUser () {
  return sessionStorage.getItem('user-phonenumber') !== null && sessionStorage.getItem('user-sessionId') !== null
}

router.beforeResolve(async (to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    const user = await getUser()
    if (!user) {
      return next({
        path: '/sign-in',
        query: {
          redirect: to.fullPath
        }
      })
    }
    return next()
  }
  return next()
})

export default router
