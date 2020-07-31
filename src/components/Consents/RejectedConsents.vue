<template>
  <div>
     <div v-if="data.length === 0">
        <consents-no-data consentType="rejected"/>
     </div>
    <div v-for="i in data" :key="i">
      <consent-card-component title="Performance" icon="finance">
        <div class="rows">
          <div class="row columns is-mobile is-vcentered">
            <div class="logo column" align="left">
              <img :src="i.fiu_logo" />
            </div>
            <div v-if="i.isVerified" class="column is-green" align="right">
               {{$t('labelVerified')}}
              <b-icon icon="shield-check" custom-size="default" />
            </div>
          </div>
          <div class="row">
            <h2 class="title is-6">{{i.tagline}}</h2>
          </div>
          <div class="row columns my-1">
            <div class="column is-gray" align="left">
              <h2 class="is-7">{{i.validTill}}</h2>
            </div>
          </div>
          <div class="row columns is-mobile">
            <div @click="isImageModalActive = true" class="play-video-trigger column" align="left">
              <b-icon class="mr-1" icon="play-circle" size="is-small" />
              <a class="is-6">How does it work?</a>
            </div>
            <div class="column is-gray is-two-fifths" align="right">
              <h2 class="is-8">Report Fraud</h2>
            </div>
          </div>
        </div>
      </consent-card-component>
      <p></p>
    </div>
  </div>
</template>

<script>
import ConsentCardComponent from '@/components/ConsentCardComponent'
import ConsentsNoData from '@/components/ConsentsNoData'
export default {
  components: {
    ConsentCardComponent,
    ConsentsNoData
  },
  props: {
    data: {
      type: String,
      default: null
    }
  }
}
</script>

<style scoped>
.play-video-trigger,
.play-video-trigger a {
  color: #079AFF;
  font-weight: bold;
  text-decoration: underline;
}

.is-gray {
  color: #acacac !important;
}

.is-green {
    color: #03B072 !important;
    font-weight: bold;
}
</style>
