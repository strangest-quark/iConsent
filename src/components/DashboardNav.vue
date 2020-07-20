<template>
<section>
  <b-tabs type="is-boxed">
    <b-tab-item>
      <template slot="header">
        <!-- <b-icon icon="clock" size="is-small"></b-icon> -->
        <span>
          <strong>Pending</strong>
          <!-- <b-tag type="is-primary" rounded>1</b-tag> -->
        </span>
      </template>
    </b-tab-item>
    <b-tab-item>
      <template slot="header">
        <!-- <b-icon icon="file" size="is-small"></b-icon> -->
        <span>
          <strong>Active</strong>
        </span>
      </template>
    </b-tab-item>
    <b-tab-item>
      <template slot="header">
        <!-- <b-icon icon="pause" size="is-small"></b-icon> -->
        <span>
          <strong>Revoked</strong>
        </span>
      </template>
    </b-tab-item>
    <b-tab-item>
      <template slot="header">
        <!-- <b-icon icon="stop" size="is-small"></b-icon> -->
        <span>
          <strong>Rejected</strong>
        </span>
      </template>
    </b-tab-item>
  </b-tabs>
</section>
</template>
