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
          <li id="title">
            <strong class="menu-title">Consents</strong>
          </li>

          <li v-for="item in menuItems('consent')" :key="item.id">
            <span @click="menuClick(item)" :class="item.class" data-badge="3" class="menu-item">
              <b-icon class="sub-type-icon" :icon="item.icon" size="is-small" />
              {{item.label}}
            </span>
          </li>
        </ul>
        <ul>
          <li id="title">
            <strong class="menu-title">Accounts</strong>
          </li>
          <li v-for="item in menuItems('account')" :key="item.id">
            <span @click="menuClick(item)" :class="item.class" data-badge="3" class="menu-item">
              <b-icon class="sub-type-icon" :icon="item.icon" size="is-small" />
              {{item.label}}
            </span>
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
      currentLabel: '',
      previousActiveId: 1,
      menu: [
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
  methods: {
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
  margin-left: 1rem;
  margin-top: 0.75rem;
}
.strana {
  height: 100vh;
}
.strana li {
  color: #f7f7f7da;
  list-style: none;
  padding-top: 10px;
  padding-bottom: 10px;
  padding-left: 5px;
  padding-right: 10px;
  transition: 0.1s all ease;
  text-align: left;
}
.strana li span:hover {
  cursor: pointer;
}
.strana ul {
  margin-top: 0px;
  margin-left: 20px;
}
.strana ul:nth-child(2) {
  margin-top: 10px;
  margin-left: 20px;
}

.sidebar-navigation {
  padding-top: 2vh;
}

.menu-item,
.menu-item-static {
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
  padding-right: 1rem;
  padding-left: 1rem;
}
.strana .menu-item:hover {
  border-radius: 20px;
  background: #079aff;
  color: #ffffff;
  /* font-weight: bold; */
}
.strana .menu-item.active {
  border-radius: 20px;
  background: #079aff;
  color: #ffffff;
  font-weight: bold;
}
.strana li:hover i {
  color: #fff;
}
.strana .sub-type-icon {
  margin-right: 10px;
}
.menu-title {
  color: #f7f7f7;
}
.menu-icon {
  margin: 1rem;
  text-align: left;
}

.notification-badges [data-badge] {
  position: relative;
}
.notification-badges [data-badge]:after {
  position: absolute;
  right: -2px;
  top: -2px;
  min-width: 17px;
  min-height: 17px;
  line-height: 12px;
  text-align: center;
  padding: 2px;
  color: white;
  background-color: #079aff;
  font-size: 12px;
  border-radius: 20px;
  content: attr(data-badge);
  /* border: solid 1px white; */
}
</style>
