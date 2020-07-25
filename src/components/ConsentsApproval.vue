<template>
   <div class="section is-fluid">
      <div v-if="isLoading" class="is-center">
         <bounce :loading="isLoading"></bounce>
      </div>
      <div v-if="!isLoading" class="columns is-multiline">
         <div class="column">
            <b-button icon-left="chevron-left" type="is-light">Pending</b-button>
            <div>
               <div class="rows">
                  <div class="row columns is-mobile is-vcentered">
                     <div class="logo column" align="left">
                        <img src="@/assets/FIU_Logo/quickbooks.jpg" />
                     </div>
                     <div class="column is-green" align="right">
                        Verified
                        <b-icon icon="shield-check" custom-size="default" />
                     </div>
                  </div>
                  <div>
                     <div class="row">
                        <h2 class="title is-5">Quickbooks wants to access your savings account details</h2>
                     </div>
                     <br>
                     <p class="answer">Please read the consent details carefully</p>
                     <progress-bar
                        :options="options"
                        :value="value"
                        style="padding: 0px 0px 1% 0"
                        />
                     <hr />
                     <div id="scroll" ref="scroll" @scroll="onScroll">
                        <div class="row">
                           <div class="rows">
                              <span class="row">
                                 <h2 class="question subtitle is-6">What range of my data will be accessed?</h2>
                              </span>
                              <span class="row">
                                 <span class="columns">
                                    <span class="column">
                                       <p class="answer">From</p>
                                       <p class="answer">
                                          <strong>06 July 2020</strong>
                                       </p>
                                    </span>
                                    <span class="column">
                                       <p class="answer">To</p>
                                       <p class="answer">
                                          <strong>06 July 2021</strong>
                                       </p>
                                    </span>
                                 </span>
                              </span>
                           </div>
                        </div>
                        <hr />
                        <span class="row">
                           <h2 class="question subtitle is-6">What access will quickbooks have?</h2>
                        </span>
                        <div class="row" style="width: 75%">
                           <div style="padding: 1% 4% 0% 0%" >
                              <div class="row">
                                 <div class="column1">
                                    <div class="hvrbox">
                                       <a @mouseover="onHover('card1')" class="card1" href="#">
                                          <img src="@/assets/periodic.png"/>
                                          <h1>Periodic</h1>
                                          <div class="hvrbox-layer_top">
                                             <h2 class="hvrbox-text"><b>Periodic fetch of data</b></h2>
                                          </div>
                                       </a>
                                    </div>
                                 </div>
                                 <div class="column1">
                                    <div class="hvrbox">
                                       <a @mouseover="onHover('card2')" class="card1" href="#">
                                          <img src="@/assets/stream.png"/>
                                          <h1>View</h1>
                                          <div class="hvrbox-layer_top">
                                             <h2 class="hvrbox-text"><b>View your data</b></h2>
                                          </div>
                                       </a>
                                    </div>
                                 </div>
                                 <div @mouseover="onHover('card3')" class="column1">
                                    <div class="hvrbox">
                                       <a  @mouseover="onHover" class="card1" href="#">
                                          <img src="@/assets/summary.png"/>
                                          <h1>Summary</h1>
                                          <div class="hvrbox-layer_top">
                                             <h2 class="hvrbox-text"><b>Summary data view</b></h2>
                                          </div>
                                       </a>
                                    </div>
                                 </div>
                              </div>
                           </div>
                        </div>
                        <hr />
                        <div class="row">
                           <div class="rows">
                              <span class="row">
                                 <h2 class="question subtitle is-6">Why does quickbook needs this data?</h2>
                              </span>
                              <span class="row">
                                 <p class="answer">Explicit consent for something</p>
                              </span>
                           </div>
                        </div>
                        <hr />
                        <div class="row">
                           <div class="rows">
                              <span class="row">
                                 <h2 class="question subtitle is-6">Till when this consent is valid?</h2>
                              </span>
                              <span class="row">
                                 <p class="answer">
                                    Valid till
                                    <strong>06 July 2021</strong>
                                 </p>
                              </span>
                           </div>
                        </div>
                        <hr />
                     </div>
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
                  </footer>
               </div>
            </div>
         </div>
         <div class="column is-half content-right is-hidden-mobile" style="padding-left: 5%">
            <div class="rows">
               <div class="row" style="width: 80%">
                  <BankList :line1="line1" :line2="line2" :haveCheckBox="haveCheckBox" />
               </div>
               <div class="row" style="width: 75%">
                  <Video style="margin-top: 5%"/>
               </div>
            </div>
         </div>
      </div>
   </div>
</template>
<script>
import Video from '@/components/Video'
import BankList from '@/components/BankList'

// APIs
import DashboardAPI from '@/assets/api/dashboard'

export default {
  components: {
    Video,
    BankList
  },
  data () {
    return {
      value: 0,
      maxProgress: 0,
      cardsChecked: [],
      isImageModalActive: false,
      haveCheckBox: true,
      line1: 'Select',
      line2: 'Accounts',
      isActiveTab: 0,
      dashboardData: null,
      isLoading: false,
      options: {
        text: {
          color: '#FFFFFF',
          shadowEnable: true,
          shadowColor: '#000000',
          fontSize: 14,
          fontFamily: 'Helvetica',
          dynamicPosition: false,
          hideText: true
        },
        progress: {
          color: '#2dbd2d',
          backgroundColor: 'white'
        },
        layout: {
          height: 10,
          width: 650,
          verticalTextAlign: 61,
          horizontalTextAlign: 43,
          zeroOffset: 0,
          strokeWidth: 30,
          progressPadding: 0,
          type: 'line'
        }
      }
    }
  },
  methods: {
    openLoading () {
      this.isLoading = true
    },
    closeLoading () {
      this.isLoading = false
    },
    dashboardTabChanged (index) {
      this.isActiveTab = index
    },
    onScroll () {
      const progress = this.$refs.scroll.scrollTop * 40 / (this.$refs.scroll.scrollHeight - this.$refs.scroll.clientHeight)
      if (progress > this.maxProgress) {
        this.maxProgress = progress
        this.value = progress
      }
    },
    onHover (card) {
      if (!this.cardsChecked.includes(card)) {
        this.cardsChecked.push(card)
        this.value += 20
      }
    }
  },
  mounted () {
    const here = this
    here.openLoading()
    const payload = {}
    DashboardAPI.postItem(payload)
      .then(function (response) {
        here.dashboardData = response.data
        here.closeLoading()
      })
      .catch(error => {
        console.log(error)
        here.closeLoading()
        here.$buefy.snackbar.open({
          type: 'is-danger',
          message: 'Failed. Please Retry..',
          queue: false
        })
      })
  }
}
</script>
<style scoped>
   .content-right {
   height: 100%;
   /* margin-left: 2rem; */
   }
   .content-left {
   height: 100%;
   }
   .pending-consent {
   background-color: #f26c63;
   }
   .active-consent {
   background-color: #99d25c;
   }
   .video {
   text-align: center;
   }
   .dashboard-consents {
   overflow-y: scroll;
   height: 74vh;
   }
   .logo {
   max-width: 10rem;
   }
   .is-green {
   color: #03b072 !important;
   font-weight: bold;
   }
   .rows {
   margin: 0.5rem;
   }
   hr {
   display: block;
   height: 1px;
   border: 0;
   border-top: 1px solid #ccc;
   margin: 1em 0;
   padding: 0;
   opacity: 0.5;
   }
   .question {
   color: #079aff;
   font-weight: bold;
   margin-bottom: 0.5rem;
   }
   .answer {
   color: #222222;
   }
   #scroll {
   overflow-y: auto;
   height: 50vh;
   }
   .column1 {
   float: center;
   width: 33.33%;
   padding: 0.1em;
   }
   /* Clear floats after the columns */
   .row:after {
   content: "";
   display: table;
   clear: both;
   }
   h1{
   font-size: large;
   text-align: center;
   color: black;
   }
   h2{
   font-size: medium;
   text-align: center;
   color: black;
   }
   img{
   width: 50%;
   }
   .card1 {
   text-align: center;
   display: block;
   position: relative;
   max-width: auto;
   background-color: white;
   border-radius: 8px;
   padding: 10% 5%;
   margin: 12px;
   text-decoration: none;
   z-index: 0;
   overflow: hidden;
   box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
   }
   .hvrbox,
   .hvrbox * {
   box-sizing: border-box;
   }
   .hvrbox {
   position: relative;
   display: inline-block;
   overflow: hidden;
   max-width: 100%;
   height: auto;
   }
   .hvrbox img {
   max-width: 100%;
   }
   .hvrbox .hvrbox-layer_bottom {
   display: block;
   }
   .hvrbox .hvrbox-layer_top {
   opacity: 0;
   position: absolute;
   top: 0;
   left: 0;
   right: 0;
   bottom: 0;
   width: 100%;
   height: 100%;
   background: #D9DEE8;
   color: #000000;
   padding: 15px;
   -moz-transition: all 0.4s ease-in-out 0s;
   -webkit-transition: all 0.4s ease-in-out 0s;
   -ms-transition: all 0.4s ease-in-out 0s;
   transition: all 0.4s ease-in-out 0s;
   }
   .hvrbox:hover .hvrbox-layer_top,
   .hvrbox.active .hvrbox-layer_top {
   opacity: 1;
   }
   .hvrbox .hvrbox-text {
   text-align: center;
   font-size: 16px;
   display: inline-block;
   position: absolute;
   text-emphasis: bold;
   top: 50%;
   left: 50%;
   -moz-transform: translate(-50%, -50%);
   -webkit-transform: translate(-50%, -50%);
   -ms-transform: translate(-50%, -50%);
   transform: translate(-50%, -50%);
   }
   .hvrbox .hvrbox-text_mobile {
   font-size: 15px;
   border-top: 1px solid rgb(179, 179, 179); /* for old browsers */
   border-top: 1px solid rgba(179, 179, 179, 0.7);
   margin-top: 5px;
   padding-top: 2px;
   display: none;
   }
   .hvrbox.active .hvrbox-text_mobile {
   display: block;
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
</style>
