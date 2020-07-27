import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import SignIn from '../views/SignIn.vue'
import Language from '../views/Languages.vue'
import Dashboard from '../views/Dashboard.vue'
import Consents from '../views/Consents.vue'
import Accounts from '../views/Accounts.vue'
import ConsentDecision from '../views/ConsentDecision.vue'

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
    path: '/language',
    name: 'language',
    component: Language
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: Dashboard
  },
  {
    path: '/consents',
    name: 'consents',
    component: Consents
  },
  {
    path: '/accounts',
    name: 'accounts',
    component: Accounts
  },
  {
    path: '/consents/pending/:fiu/:id',
    name: 'consentdecision',
    component: ConsentDecision
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
