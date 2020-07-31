<template>
  <div>
    <section class="section hero is-fullheight is-error-section">
      <div class="hero-body">
        <div class="container">
          <div class="columns is-centered">
            <div class="column is-two-fifths">
              <div class="card has-card-header-background">
                <header class="card-header">
                  <p class="card-header-title">
                    <span class="logo logo-background">
                      <img src="@/assets/onemoney-logo.png" />
                    </span>
                  </p>
                </header>
                <div class="card-content">
                  <form @submit.prevent="signInUser">
                    <div class="field">
                      <label class="label">Phone Number</label>
                      <div class="control has-icons-right">
                        <input
                        v-model="inputPhoneNumber"
                          type="number"
                          autocomplete="off"
                          name="number"
                          required="required"
                          autofocus="autofocus"
                          class="input is-secondary-om-black"
                        />
                      </div>
                    </div>
                    <div class="field">
                      <label class="label">OTP</label>
                      <div class="control has-icons-right">
                        <input
                        v-model="inputOTP"
                          type="password"
                          pattern="[1-9]*"
                          inputmode="numeric"
                          autocomplete="off"
                          required="required"
                          name="otp"
                          class="input"
                        />
                      </div>
                    </div>
                    <div class="field is-centered">
                      <div class="control">
                        <button type="submit" class="button is-black">Login</button>
                      </div>
                    </div>
                  </form>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="hero-foot has-text-centered">
        <div class="logo"></div>
      </div>
    </section>
  </div>
</template>

<script>
// APIs
import LoginAPI from '@/assets/api/login'
import UserAPI from '@/assets/api/userprofile'

export default {
  data () {
    return {
      inputPhoneNumber: null,
      inputOTP: null,
      loadingComponent: null,
      isLoading: false,
      isFullPage: false
    }
  },
  mounted () {
    this.$store.commit('asideHolderHide', false)
    this.userStatus()
  },
  methods: {
    userStatus () {
      if (sessionStorage.getItem('user-phonenumber') !== null && sessionStorage.getItem('user-sessionId') !== null) {
        this.$store.commit('asideHolderHide', true)
        this.$router.push('/').catch(() => {})
      }
    },
    openLoading () {
      this.isLoading = true
    },
    closeLoading () {
      this.isLoading = false
    },
    getUserDetails () {
      const here = this
      const payload = {}
      UserAPI.postItem(payload)
        .then(function (response) {
          if (response.data.status === true) {
            sessionStorage.setItem('user-name', String(response.data.userData.firstName))
          } else {
            here.$buefy.snackbar.open({
              type: 'is-danger',
              message: response.data.errMessage,
              queue: false
            })
          }
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
    },
    signInUser () {
      const here = this
      here.openLoading()
      const payload = {
        phone_number: String(this.inputPhoneNumber),
        otp_reference: '14f3625f-4918-4960-a99a-760bd2ef6609',
        code: String(this.inputOTP)
      }
      LoginAPI.postItem(payload)
        .then(function (response) {
          if (response.data.status === true) {
            sessionStorage.setItem('user-phonenumber', String(here.inputPhoneNumber))
            sessionStorage.setItem('user-sessionId', String(response.data.sessionId))
            here.$store.commit('asideHolderHide', true)
            here.$router.push('/').catch(() => {})
            here.getUserDetails()
            here.closeLoading()
          } else {
            here.closeLoading()
            here.$buefy.snackbar.open({
              type: 'is-danger',
              message: response.data.errMessage,
              queue: false
            })
          }
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
}
</script>

<style scoped>
/* To remove increase or decrese arrow in number input */
/* Chrome, Safari, Edge, Opera */
input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

/* Firefox */
input[type="number"] {
  -moz-appearance: textfield;
}

.logo {
  max-width: 8rem;
}
</style>
