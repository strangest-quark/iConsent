import Vue from 'vue'
import VueI18n from 'vue-i18n'

Vue.use(VueI18n)

const messages = {
  en: {
    welcomeMsg: 'Welcome to Your Vue.js App',
    label: 'For a guide and recipes on how to configure / customize this project,',
    menulabelDashboard: 'Dashboard',
    menulabelConsents: 'Consents',
    menulabelAccounts: 'Accounts',
    menulabelLanguage: 'Language',
    dashboardMenulabelPending: 'Pending',
    dashboardMenulabelActive: 'Active',
    dashboardMenulabelRevoked: 'Revoked',
    dashboardMenulabelRejected: 'Rejected',
    dashboardConsentsPending: 'Consents Pending',
    dashboardConsentsActive: 'Consents Active'
  },
  ta: {
    welcomeMsg: 'உங்கள் Vue.js பயன்பாட்டிற்கு வருக',
    guide: 'இந்த திட்டத்தை எவ்வாறு கட்டமைப்பது / தனிப்பயனாக்குவது என்பது குறித்த வழிகாட்டி மற்றும் சமையல் குறிப்புகளுக்கு,',
    menulabelDashboard: 'டாஷ்போர்டு',
    menulabelConsents: 'சம்மதம்',
    menulabelAccounts: 'கணக்குகள்',
    menulabelLanguage: 'மொழி',
    dashboardMenulabelPending: 'நிலுவை',
    dashboardMenulabelActive: 'செயலில்',
    dashboardMenulabelRevoked: 'ரத்து செய்யப்பட்டது',
    dashboardMenulabelRejected: 'நிராகரிக்கப்பட்டது',
    dashboardConsentsPending: 'சம்மதம் நிலுவையில்',
    dashboardConsentsActive: 'சம்மதம் செயலில்'
  },
  ml: {
    welcomeMsg: 'നിങ്ങളുടെ Vue.js അപ്ലിക്കേഷനിലേക്ക് സ്വാഗതം',
    guide: 'ഈ പ്രോജക്റ്റ് എങ്ങനെ ക്രമീകരിക്കാം / ഇഷ്ടാനുസൃതമാക്കാം എന്നതിനെക്കുറിച്ചുള്ള ഒരു ഗൈഡിനും പാചകക്കുറിപ്പുകൾക്കും',
    menulabelDashboard: 'ഡാഷ്ബോർഡ്',
    menulabelConsents: 'സമ്മതം',
    menulabelAccounts: 'അക്കൗണ്ടുകൾ',
    menulabelLanguage: 'ഭാഷ',
    dashboardMenulabelPending: 'ശേഷിക്കുന്നു',
    dashboardMenulabelActive: 'സജീവമാണ്',
    dashboardMenulabelRevoked: 'അസാധുവാക്കി',
    dashboardMenulabelRejected: 'നിരസിച്ചു',
    dashboardConsentsPending: 'സമ്മതം ശേഷിക്കുന്നു',
    dashboardConsentsActive: 'സമ്മതം സജീവമാണ്'

  },
  hi: {
    welcomeMsg: 'आपका स्वागत है आपका Vue.js ऐप में',
    guide: 'इस परियोजना को कॉन्फ़िगर / अनुकूलित करने के तरीके पर एक गाइड और व्यंजनों के लिए',
    menulabelDashboard: 'डैशबोर्ड',
    menulabelConsents: 'सहमति',
    menulabelAccounts: 'हिसाब',
    menulabelLanguage: 'भाषा',
    dashboardMenulabelPending: 'विचाराधीन',
    dashboardMenulabelActive: 'सक्रिय',
    dashboardMenulabelRevoked: 'निरस्त',
    dashboardMenulabelRejected: 'अस्वीकृत',
    dashboardConsentsPending: 'लंबित है',
    dashboardConsentsActive: 'सक्रिय रहता'
  }
}

const i18n = new VueI18n({
  locale: localStorage.getItem('user-language'),
  fallbackLocale: 'en',
  messages
})

export default i18n
