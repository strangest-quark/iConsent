import Vue from 'vue'
import VueI18n from 'vue-i18n'

Vue.use(VueI18n)

const messages = {
  en: {
    menulabelDashboard: 'Dashboard',
    menulabelConsents: 'Consents',
    menulabelAccounts: 'Accounts',
    menulabelLanguage: 'Language',
    dashboardMenulabelPending: 'Pending',
    dashboardMenulabelActive: 'Active',
    dashboardMenulabelInactive: 'Inactive',
    dashboardMenulabelPaused: 'Paused',
    dashboardMenulabelRevoked: 'Revoked',
    dashboardMenulabelRejected: 'Rejected',
    dashboardConsentsPending: 'Consents Pending',
    dashboardConsentsActive: 'Consents Active',
    stepProgressWhy: 'Why',
    stepProgressBanks: 'For',
    stepProgressHowLong: 'How Long',
    stepProgressWhat: 'What',
    stepProgressTillWhen: 'Till When',
    labelVerified: 'Verified'
  },
  ta: {
    menulabelDashboard: 'டாஷ்போர்டு',
    menulabelConsents: 'சம்மதம்',
    menulabelAccounts: 'கணக்குகள்',
    menulabelLanguage: 'மொழி',
    dashboardMenulabelPending: 'நிலுவை',
    dashboardMenulabelActive: 'செயலில்',
    dashboardMenulabelInactive: 'செயலற்றது',
    dashboardMenulabelPaused: 'இடைநிறுத்தப்பட்டது',
    dashboardMenulabelRevoked: 'ரத்து செய்யப்பட்டது',
    dashboardMenulabelRejected: 'நிராகரிக்கப்பட்டது',
    dashboardConsentsPending: 'சம்மதம் நிலுவையில்',
    dashboardConsentsActive: 'சம்மதம் செயலில்',
    stepProgressWhy: 'ஏன்',
    stepProgressBanks: 'கணக்குகள்',
    stepProgressHowLong: 'எவ்வளவு காலம்',
    stepProgressWhat: 'என்ன',
    stepProgressTillWhen: 'எப்போது வரை',
    labelVerified: 'சரிபார்க்கப்பட்டது'
  },
  ml: {
    menulabelDashboard: 'ഡാഷ്ബോർഡ്',
    menulabelConsents: 'സമ്മതം',
    menulabelAccounts: 'അക്കൗണ്ടുകൾ',
    menulabelLanguage: 'ഭാഷ',
    dashboardMenulabelPending: 'ശേഷിക്കുന്നു',
    dashboardMenulabelActive: 'സജീവമാണ്',
    dashboardMenulabelInactive: 'നിഷ്‌ക്രിയം',
    dashboardMenulabelPaused: 'താൽക്കാലികമായി നിർത്തി',
    dashboardMenulabelRevoked: 'അസാധുവാക്കി',
    dashboardMenulabelRejected: 'നിരസിച്ചു',
    stepProgressBanks: 'ബാങ്ക്',
    dashboardConsentsPending: 'സമ്മതം ശേഷിക്കുന്നു',
    dashboardConsentsActive: 'സമ്മതം സജീവമാണ്',
    stepProgressWhy: 'എന്തുകൊണ്ട്',
    stepProgressHowLong: 'എത്രകാലം',
    stepProgressWhat: 'എന്ത്',
    stepProgressTillWhen: 'എപ്പോൾ വരെ',
    labelVerified: 'പരിശോധിച്ചുറപ്പിച്ചു'

  },
  hi: {
    menulabelDashboard: 'डैशबोर्ड',
    menulabelConsents: 'सहमति',
    menulabelAccounts: 'हिसाब',
    menulabelLanguage: 'भाषा',
    dashboardMenulabelPending: 'विचाराधीन',
    dashboardMenulabelActive: 'सक्रिय',
    dashboardMenulabelInactive: 'निष्क्रिय',
    dashboardMenulabelPaused: 'रोके गए',
    dashboardMenulabelRevoked: 'निरस्त',
    dashboardMenulabelRejected: 'अस्वीकृत',
    dashboardConsentsPending: 'लंबित है',
    dashboardConsentsActive: 'सक्रिय रहता',
    stepProgressWhy: 'क्यों',
    stepProgressBanks: 'खाते',
    stepProgressHowLong: 'कितना लंबा',
    stepProgressWhat: 'क्या',
    stepProgressTillWhen: 'कब तक',
    labelVerified: 'सत्यापित'
  },
  te: {
    menulabelDashboard: 'డాష్బోర్డ్',
    menulabelConsents: 'సమ్మతిస్తే',
    menulabelAccounts: 'అకౌంట్స్',
    menulabelLanguage: 'భాషా',
    dashboardMenulabelPending: 'పెండింగ్',
    dashboardMenulabelActive: 'చురుకుగా',
    dashboardMenulabelInactive: 'క్రియారహిత',
    dashboardMenulabelPaused: 'పాజ్',
    dashboardMenulabelRevoked: 'రద్దు',
    dashboardMenulabelRejected: 'తిరస్కరించబడిన',
    dashboardConsentsPending: 'సమ్మతి పెండింగ్‌లో',
    dashboardConsentsActive: 'సమ్మతించింది',
    stepProgressWhy: 'ఎందుకు',
    stepProgressHowLong: 'ఎంతసేపు',
    stepProgressBanks: 'ఖాతాల',
    stepProgressWhat: 'ఏం',
    stepProgressTillWhen: 'ఎప్పటి దాకా',
    labelVerified: 'ధృవీకరించబడిన'
  },
  ka: {
    menulabelDashboard: 'ಡ್ಯಾಶ್‌ಬೋರ್ಡ್',
    menulabelConsents: 'ಒಪ್ಪಿಗೆ',
    menulabelAccounts: 'ಖಾತೆಗಳು',
    menulabelLanguage: 'ಭಾಷೆ',
    dashboardMenulabelPending: 'ಬಾಕಿ ಉಳಿದಿದೆ',
    dashboardMenulabelActive: 'ಸಕ್ರಿಯ',
    dashboardMenulabelInactive: 'ನಿಷ್ಕ್ರಿಯ',
    dashboardMenulabelPaused: 'ವಿರಾಮಗೊಳಿಸಲಾಗಿದೆ',
    dashboardMenulabelRevoked: 'ಹಿಂತೆಗೆದುಕೊಳ್ಳಲಾಗಿದೆ',
    dashboardMenulabelRejected: 'ತಿರಸ್ಕರಿಸಿದ',
    dashboardConsentsPending: 'ಒಪ್ಪಿಗೆಗಳು ಉಳಿದಿವೆ',
    dashboardConsentsActive: 'ಸಕ್ರಿಯವಾಗಿದೆ',
    stepProgressWhy: 'ಏಕೆ',
    stepProgressBanks: 'ಖಾತೆಗಳು',
    stepProgressHowLong: 'ಎಷ್ಟು ಉದ್ದ',
    stepProgressWhat: 'ಏನು',
    stepProgressTillWhen: 'ಯಾವಾಗ',
    labelVerified: 'ಪರಿಶೀಲಿಸಲಾಗಿದೆ'
  }
}

const i18n = new VueI18n({
  locale: localStorage.getItem('user-language'),
  fallbackLocale: navigator.language,
  messages
})

export default i18n
