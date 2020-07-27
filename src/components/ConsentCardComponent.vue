<template>
  <div @click="clickPendingConsent"  class="card">
    <div class="card-content">
      <slot />
    </div>
    <footer class="card-footer">
      <span class="card-footer-item reject">
        <b-icon icon="close" custom-size="default" />
        <a href="#">Reject</a>
      </span>
       <span class="card-footer-item approve">
           <b-icon icon="check-circle-outline" custom-size="default" />
        <a href="#">Approve</a>
      </span>
      <span class="card-footer-item more">
          <b-icon icon="arrow-right-circle-outline" custom-size="default" />
        <a href="#">More</a>
      </span>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'CardComponent',
  props: {
    status: {
      type: String,
      default: null
    },
    artifactId: {
      type: String,
      default: null
    },
    fiu: {
      type: String,
      default: null
    }
  },
  methods: {
    clickPendingConsent () {
      if (this.status === 'pending') {
        this.$router.push(`/consents/pending/${this.fiu}/${this.artifactId}`)
      }
    }
  }
}
</script>

<style scoped>
.logo {
  max-width: 10rem;
}
.card:hover {
  box-shadow: 2px 2px 2px 2px rgba(0, 0, 0, 0.2);
}
.card-header-end {
  text-align: right;
}
.card-footer-item.reject a{
  /* background-color: #F26C63 !important; */
  /* color: white */
    font-weight: bold;
color: #E11A50
}
.card-footer-item.approve a,card-footer-item.approve{
  /* background-color: #99D25C !important; */
  font-weight: bold;
  color: #03B072
}

.card-footer-item.more a,card-footer-item.more{
  /* background-color: #99D25C !important; */
  font-weight: bold;
  color: #666666
}
</style>
