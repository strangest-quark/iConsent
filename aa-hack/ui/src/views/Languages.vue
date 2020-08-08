<template>
  <div>
    <!-- <Language msg="Welcome to Your Vue.js App" /> -->
    <div class="section">
      <h2 class="subtitle is-6">
        <em>The default language maybe same as the browsers language</em>
      </h2>
      <div class="columns is-multiline">
        <div
          v-for="(i,index) in languages"
          :key="index"
          class="language-options column is-one-quarter"
        >
          <div class="card">
            <div @click="changeLocale(i.language)" :class="i.class">
              <div class="card-content">
                <div class="media">
                  <div class="media-left">
                    <figure class="image is-48x48">
                      <span class="display-letter">{{i.displayLetter}}</span>
                    </figure>
                  </div>
                  <div class="media-content">
                    <p class="title is-4">{{i.displayLanguage}}</p>
                    <p class="subtitle is-6">{{ i.title }}</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import Language from '@/components/Language.vue'
import EventBus from '@/eventBus'
import i18n from '@/plugins/i18n'
export default {
  components: {
    // Language
  },
  data () {
    return {
      previousActiveLanguage: 'en',
      languages: [
        {
          flag: 'us',
          language: 'en',
          title: 'English',
          displayMessage: 'Hello',
          displayLetter: 'A',
          displayLanguage: 'English',
          class: 'active'
        },
        {
          flag: 'in',
          language: 'hi',
          title: 'Hindi',
          displayMessage: 'नमस्ते',
          displayLetter: 'आ',
          displayLanguage: 'हिन्दी',
          class: ''
        },
        {
          flag: 'in',
          language: 'ta',
          title: 'Tamil',
          displayMessage: 'வணக்கம்',
          displayLetter: 'அ',
          displayLanguage: 'தமிழ்',
          class: ''
        },
        {
          flag: 'in',
          language: 'ml',
          title: 'Malayalam',
          displayMessage: 'ഹലോ',
          displayLetter: 'എ',
          displayLanguage: 'മലയാളം',
          class: ''
        },
        {
          flag: 'in',
          language: 'te',
          title: 'Telugu',
          displayMessage: 'స్వాగతం',
          displayLetter: 'అ',
          displayLanguage: 'తెలుగు',
          class: ''
        },
        {
          flag: 'in',
          language: 'kn',
          title: 'Kannada',
          displayMessage: 'ಸ್ವಾಗತ',
          displayLetter: 'ಎ',
          displayLanguage: 'ಕನ್ನಡ',
          class: ''
        }
      ]
    }
  },
  mounted () {
    EventBus.$on('current_user_language', (language) => {
      this.setActive(language)
    })
    if (localStorage.getItem('user-language') === null) {
      this.setActive(navigator.language)
    } else {
      this.setActive(localStorage.getItem('user-language'))
    }
  },
  methods: {
    setActive (language) {
      //   if (this.previousActiveLanguage === language) return
      this.languages.find(
        (item) => item.language === this.previousActiveLanguage
      ).class = ''
      this.languages.find((item) => item.language === language).class =
        'active'
      this.previousActiveLanguage = language
    },
    activeLanguage (language) {
      return localStorage.getItem('user-language') === language
    },
    changeLocale (locale) {
      this.setActive(locale)
      localStorage.setItem('user-language', locale)
      i18n.locale = locale
    }
  }
}
</script>

<style>
.display-letter {
  font-size: 2rem;
}
.language-options .card {
  background: aliceblue;
}

.language-options .card .active {
  background: #99d25c;
  border: 1px solid gray;
  border-radius: 5px;
}

.language-options .content .icon {
  height: 1rem;
  color: green;
}
</style>
