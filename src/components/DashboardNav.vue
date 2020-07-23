<template>
<section>
  <b-tabs type="is-boxed">
    <b-tab-item v-for="(item, i) in menuItems" :key="i">
      <template slot="header">
        <!-- <b-icon icon="clock" size="is-small"></b-icon> -->
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
  data () {
    return {
      menuItems: [
        {
          id: 1,
          label: 'Pending'
        },
        {
          id: 2,
          label: 'Active'
        },
        {
          id: 3,
          label: 'Revoked'
        },
        {
          id: 4,
          label: 'Rejected'
        }
      ]
    }
  }
}
</script>
