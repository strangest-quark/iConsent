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
    labelVerified: 'Verified',
    buttonViewMore: 'View More',
    chatNeedHelp: 'Need Help?',
    chatSubtitle: 'Our support can help you understand your data rights better',
    scrollTitleYour: 'Your',
    scrollTitleAccounts: 'Accounts',
    buttonPending: 'Pending',
    buttonBack: 'Back',
    buttonNext: 'Next',
    buttonApprove: 'Approve',
    buttonReject: 'Reject',
    buttonChat: 'Chat',
    buttonDelink: 'Delink',
    buttonAddAccount: 'Add Account',
    buttonHowDoesItWork: 'How does it work?',
    accountLinkedConsents: 'Linked Consents',
    banks: [{
      id: 1,
      name: 'Citibank',
      imgName: 'citi.png',
      accType: 'Savings',
      accNo: 4545
    },
    {
      id: 2,
      name: 'HDFC Bank',
      imgName: 'hdfc.png',
      accType: 'Loan',
      accNo: 3455
    },
    {
      id: 3,
      name: 'Axis Bank',
      imgName: 'axis.png',
      accType: 'Savings',
      accNo: 9545
    }]
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
    labelVerified: 'சரிபார்க்கப்பட்டது',
    buttonViewMore: 'மேலும் பார்க்க',
    chatNeedHelp: 'உதவி தேவை?',
    chatSubtitle: 'உங்கள் தரவு உரிமைகளை நன்கு புரிந்துகொள்ள எங்கள் ஆதரவு உதவும்',
    scrollTitleYour: 'உங்கள்',
    scrollTitleAccounts: 'கணக்குகள்',
    buttonPending: 'நிலுவை',
    buttonBack: 'பின்னால்',
    buttonNext: 'அடுத்தது',
    buttonApprove: 'ஒப்புதல்',
    buttonReject: 'நிராகரி',
    buttonChat: 'அரட்டை',
    buttonDelink: 'முறிவுசெய்',
    buttonAddAccount: 'கணக்கு சேர்க்க',
    buttonHowDoesItWork: 'எப்படி வேலை செய்கிறது?',
    accountLinkedConsents: 'செயலில் ஒப்புதல்',
    banks: [{
      id: 1,
      name: 'சிட்டி வங்கி',
      imgName: 'citi.png',
      accType: 'சேமிப்பு',
      accNo: 4545
    },
    {
      id: 2,
      name: 'எச்டிஎஃப்சி வங்கி',
      imgName: 'hdfc.png',
      accType: 'கடன்',
      accNo: 3455
    },
    {
      id: 3,
      name: 'ஆக்சிஸ் வங்கி',
      imgName: 'axis.png',
      accType: 'சேமிப்பு',
      accNo: 9545
    }]
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
    labelVerified: 'പരിശോധിച്ചുറപ്പിച്ചു',
    buttonViewMore: 'കൂടുതൽ കാണു',
    chatNeedHelp: 'സഹായം ആവശ്യമുണ്ട്?',
    chatSubtitle: 'നിങ്ങളുടെ ഡാറ്റ അവകാശങ്ങൾ നന്നായി മനസ്സിലാക്കാൻ ഞങ്ങളുടെ പിന്തുണ സഹായിക്കും',
    scrollTitleYour: 'നിങ്ങളുടെ',
    scrollTitleAccounts: 'അക്കൗണ്ടുകൾ',
    buttonPending: 'ശേഷിക്കുന്നു',
    buttonBack: 'തിരികെ',
    buttonNext: 'അടുത്തത്',
    buttonApprove: 'അംഗീകരിക്കുക',
    buttonReject: 'നിരസിക്കുക',
    buttonChat: 'ചാറ്റ്',
    buttonDelink: 'പൊട്ടുക',
    buttonAddAccount: 'അക്കൗണ്ട് ചേർക്കുക',
    buttonHowDoesItWork: 'അതെങ്ങനെയാണ് പ്രവര്ത്തിക്കുന്നത്?',
    accountLinkedConsents: 'സജീവ സമ്മതം',
    banks: [{
      id: 1,
      name: 'സിറ്റിബാങ്ക്',
      imgName: 'citi.png',
      accType: 'സേവിംഗ്സ്',
      accNo: 4545
    },
    {
      id: 2,
      name: 'എച്ച്ഡിഎഫ്സി',
      imgName: 'hdfc.png',
      accType: 'വായ്പ',
      accNo: 3455
    },
    {
      id: 3,
      name: 'ആക്സിസ്',
      imgName: 'axis.png',
      accType: 'സേവിംഗ്സ്',
      accNo: 9545
    }]

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
    labelVerified: 'सत्यापित',
    buttonViewMore: 'और देखो',
    chatNeedHelp: 'मदद ज़रूरत है?',
    chatSubtitle: 'हमारा समर्थन आपके डेटा अधिकारों को बेहतर ढंग से समझने में आपकी सहायता कर सकता है',
    scrollTitleYour: 'तुम्हारी',
    scrollTitleAccounts: 'हिसाब किताब',
    buttonPending: 'विचाराधीन',
    buttonBack: 'वापस',
    buttonNext: 'आगे',
    buttonApprove: 'मंजूर',
    buttonReject: 'अस्वीकार',
    buttonChat: 'बातचीत',
    buttonDelink: 'से अलग',
    buttonAddAccount: 'खाता जोड़ो',
    buttonHowDoesItWork: 'कैसे काम करता है?',
    accountLinkedConsents: 'सक्रिय सहमति',
    banks: [{
      id: 1,
      name: 'सिटी बैंक',
      imgName: 'citi.png',
      accType: 'जमा पूंजी',
      accNo: 4545
    },
    {
      id: 2,
      name: 'एचडीएफसी बैंक',
      imgName: 'hdfc.png',
      accType: 'ऋण',
      accNo: 3455
    },
    {
      id: 3,
      name: 'ऐक्सिस बैंक',
      imgName: 'axis.png',
      accType: 'जमा पूंजी',
      accNo: 9545
    }]
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
    labelVerified: 'నిర్ధారిత',
    buttonViewMore: 'మరిన్ని చూడండి',
    chatNeedHelp: 'సహాయం కావాలి?',
    chatSubtitle: 'మీ డేటా హక్కులను బాగా అర్థం చేసుకోవడానికి మా మద్దతు మీకు సహాయపడుతుంది',
    scrollTitleYour: 'మీ',
    scrollTitleAccounts: 'అకౌంట్స్',
    buttonPending: 'పెండింగ్',
    buttonBack: 'తిరిగి',
    buttonNext: 'తరువాత',
    buttonApprove: 'ఆమోదించడానికి',
    buttonReject: 'తిరస్కరించు',
    buttonChat: 'కబుర్లు',
    buttonDelink: 'విరామం',
    buttonAddAccount: 'ఖాతా జోడించండి',
    buttonHowDoesItWork: 'ఇది ఎలా పని చేస్తుంది?',
    accountLinkedConsents: 'లింక్డ్ సమ్మతులు',
    banks: [{
      id: 1,
      name: 'సిటీబ్యాంకు',
      imgName: 'citi.png',
      accType: 'పొదుపు',
      accNo: 4545
    },
    {
      id: 2,
      name: 'హెచ్డిఎఫ్సి',
      imgName: 'hdfc.png',
      accType: 'అప్పు',
      accNo: 3455
    },
    {
      id: 3,
      name: 'యాక్సిస్',
      imgName: 'axis.png',
      accType: 'పొదుపు',
      accNo: 9545
    }]
  },
  kn: {
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
    labelVerified: 'ಪರಿಶೀಲಿಸಲಾಗಿದೆ',
    buttonViewMore: 'ಇನ್ನಷ್ಟು ವೀಕ್ಷಿಸಿ',
    chatNeedHelp: 'ಸಹಾಯ ಬೇಕೇ?',
    chatSubtitle: 'ನಿಮ್ಮ ಡೇಟಾ ಹಕ್ಕುಗಳನ್ನು ಚೆನ್ನಾಗಿ ಅರ್ಥಮಾಡಿಕೊಳ್ಳಲು ನಮ್ಮ ಬೆಂಬಲವು ನಿಮಗೆ ಸಹಾಯ ಮಾಡುತ್ತದೆ',
    scrollTitleYour: 'ನಿಮ್ಮ',
    scrollTitleAccounts: 'ಖಾತೆಗಳು',
    buttonPending: 'ಬಾಕಿ ಉಳಿದಿದೆ',
    buttonBack: 'ಹಿಂದೆ',
    buttonNext: 'ಮುಂದೆ',
    buttonApprove: 'ಅನುಮೋದಿಸಿ',
    buttonReject: 'ತಿರಸ್ಕರಿಸಿ',
    buttonChat: 'ಚಾಟ್',
    buttonDelink: 'ವಿರಾಮ',
    buttonAddAccount: 'ಖಾತೆಯನ್ನು ಸೇರಿಸು',
    buttonHowDoesItWork: 'ಇದು ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ?',
    accountLinkedConsents: 'ಲಿಂಕ್ಡ್ ಸಮ್ಮತಿಗಳು',
    banks: [{
      id: 1,
      name: 'ಸಿಟಿಬ್ಯಾಂಕ್',
      imgName: 'citi.png',
      accType: 'ಉಳಿತಾಯ',
      accNo: 4545
    },
    {
      id: 2,
      name: 'ಎಚ್ಡಿಎಫ್ಸಿ',
      imgName: 'hdfc.png',
      accType: 'ಸಾಲ',
      accNo: 3455
    },
    {
      id: 3,
      name: 'ಆಕ್ಸಿಸ್',
      imgName: 'axis.png',
      accType: 'ಉಳಿತಾಯ',
      accNo: 9545
    }]
  }
}

const i18n = new VueI18n({
  locale: localStorage.getItem('user-language'),
  fallbackLocale: 'en',
  messages
})

export default i18n
