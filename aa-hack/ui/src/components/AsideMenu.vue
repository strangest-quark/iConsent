<template>
  <aside v-if="isAsideVisible" class="aside is-placed-left is-expanded">
    <aside-tools :is-main-menu="true">
      <span slot="label" class="logo">
        <img src="@/assets/onemoney-logo.png" />
      </span>
    </aside-tools>

    <div class="strana">
      <div class="sidebar-navigation">
        <ul>
          <li
            class="notification-badges sidebar-content"
            v-for="item in menuItems('consent')"
            :key="item.id"
          >
            <div
              @click="menuClick(item)"
              :class="item.class"
              class="menu-item"
              @mouseover="showDetails(item.id)"
              @mouseleave="hideDetails(item.id)"
            >
            <div class="row item-label">
              <b-icon :icon="item.icon" size="is-default" />
            </div>
            <div class="row item-label">
              <span>{{$t('menulabel'+item.label)}}</span>
            </div>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </aside>
</template>

<script>
import { mapState } from 'vuex'
import AsideTools from '@/components/AsideTools'

export default {
  name: 'AsideMenu',
  components: { AsideTools },
  computed: {
    ...mapState(['isAsideVisible'])
  },
  mounted () {
    this.setPreviousActiveId()
  },
  data () {
    return {
      showDetailId: null,
      currentLabel: '',
      previousActiveId: 1,
      menu: [
        {
          id: 1,
          label: 'Dashboard',
          icon: 'home',
          path: '/dashboard',
          class: 'active',
          type: 'consent',
          pending: 3
        },
        {
          id: 2,
          label: 'Consents',
          icon: 'file',
          path: '/consents',
          class: '',
          type: 'consent'
        },
        {
          id: 3,
          label: 'Accounts',
          icon: 'account-box-multiple',
          path: '/accounts',
          class: '',
          type: 'consent'
        },
        {
          id: 4,
          label: 'Language',
          icon: 'translate',
          path: '/language',
          class: '',
          type: 'consent'
        }
      ]
    }
  },
  methods: {
    showDetails (id) {
      this.showDetailId = id
    },
    hideDetails (id) {
      this.showDetailId = null
    },
    menuItems (itemType) {
      return this.menu.filter(value => value.type === itemType)
    },
    setPreviousActiveId () {
      this.menu.forEach(value => {
        if (this.$router.currentRoute.path === value.path) {
          this.setActive(value.id)
        }
      })
    },
    checkIfClassActive (labelItem) {
      if (labelItem === this.currentLabel) {
        return 'active'
      }
    },
    setActive (id) {
      // if (this.previousActiveId === id) return
      this.menu.find(item => item.id === this.previousActiveId).class = ''
      this.menu.find(item => item.id === id).class = 'active'
      this.previousActiveId = id
    },
    menuClick (item) {
      this.setActive(item.id)
      if (this.$router.currentRoute.path !== item.path) {
        this.$router.push(item).catch(() => {})
      }
    }
  }
}
</script>

<style scoped>
.logo img {
  height: 1.8rem;
  /* margin-left: 1rem; */
  margin-top: 0.75rem;
}
.strana {
  height: 100vh;
}
.sidebar-content {
  margin-top: 0.5rem;
}
.strana li {
  color: #f7f7f7da;
  list-style: none;
  padding-top: 10px;
  padding-bottom: 10px;
  padding-left: 5px;
  padding-right: 10px;
  transition: 0.1s all ease;
}
.strana li span:hover {
  cursor: pointer;
}
.strana ul {
  margin-top: 0px;
  /* margin-left: 20px; */
}
.strana ul:nth-child(2) {
  margin-top: 10px;
  /* margin-left: 20px; */
}

.sidebar-navigation {
  padding-top: 2vh;
}

.menu-item,
.menu-item-static {
  text-align: left;
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
  padding-right: 1rem;
  padding-left: 1rem;
    display: flex;
    flex-direction: column;
}
.strana .menu-item:hover {
  border-radius: 10px;
  background: #079aff;
  color: #ffffff;
  /* font-weight: bold; */
}
.strana .menu-item.active {
  border-radius: 10px;
  background: #079aff;
  color: #ffffff;
  font-weight: bold;
}
.strana li:hover i {
  color: #fff;
}
.menu-title {
  color: #f7f7f7;
}
.menu-icon {
  margin: 1rem;
  text-align: left;
}

.item-label{
  text-align: center;
}
</style>
