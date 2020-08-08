<template>
  <section>
    <b-tabs @input="tabChanged" type="is-boxed">
      <b-tab-item v-for="(item, i) in menuItems" :key="i">
        <template v-if="item.show" slot="header">
          <span>
            <strong>{{$t('dashboardMenulabel'+item.label)}}</strong>
          </span>
        </template>
      </b-tab-item>
    </b-tabs>
  </section>
</template>

<script>
export default {
  props: {
    pending: {
      type: Boolean,
      default: null
    },
    active: {
      type: Boolean,
      default: null
    },
    inactive: {
      type: Boolean,
      default: null
    },
    paused: {
      type: Boolean,
      default: null
    },
    revoked: {
      type: Boolean,
      default: null
    },
    rejected: {
      type: Boolean,
      default: null
    }
  },
  data () {
    return {
      menuItems: [
        {
          id: 1,
          label: 'Pending',
          show: this.pending
        },
        {
          id: 2,
          label: 'Active',
          show: this.active
        },
        {
          id: 3,
          label: 'Inactive',
          show: this.inactive
        },
        {
          id: 4,
          label: 'Paused',
          show: this.paused
        },
        {
          id: 5,
          label: 'Revoked',
          show: this.revoked
        },
        {
          id: 6,
          label: 'Rejected',
          show: this.rejected
        }
      ]
    }
  },
  methods: {
    tabChanged (index) {
      this.$emit('tabChanged', index)
    }
  }
}
</script>
