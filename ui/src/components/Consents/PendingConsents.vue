<template>
  <div>
    <div v-if="data.length === 0">
      <consents-no-data consentType="pending" />
    </div>
    <div class="mx-2 my-2" v-for="i in data" :key="i">
      <consent-card-component status="pending" :artifactId="i.consentArtefactID">
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
          <!-- <div class="row columns is-mobile">
            <div @click="isImageModalActive = true" class="play-video-trigger column" align="left">
              <b-icon class="mr-1" icon="play-circle" size="is-small" />
              <a class="is-6">How does it work?</a>
            </div>
            <div class="column is-gray is-two-fifths report-fraud" align="right">
              <h2 @click="$router.push()" class="is-8">Report Fraud</h2>
            </div>
          </div> -->
        </div>
      </consent-card-component>
      <b-modal class="video-modal" :active.sync="isImageModalActive">
        <Video :url="i.video" />
      </b-modal>
      <p></p>
    </div>
  </div>
</template>

<script>
import ConsentCardComponent from '@/components/ConsentCardComponent'
import ConsentsNoData from '@/components/ConsentsNoData'
import Video from '@/components/Video'
export default {
  components: {
    ConsentCardComponent,
    ConsentsNoData,
    Video
  },
  props: {
    data: {
      type: String,
      default: null
    }
  },
  data () {
    return {
      isImageModalActive: false
    }
  }
}
</script>

<style scoped>
.play-video-trigger,
.play-video-trigger a {
  color: #f26c63;
  font-weight: bold;
  text-decoration: underline;
}
.is-gray {
  color: #acacac !important;
}

.is-green {
  color: #03b072 !important;
  font-weight: bold;
}
.video-modal {
  text-align: center;
}
.report-fraud{
  text-decoration: underline;
  cursor: pointer;
}
</style>
