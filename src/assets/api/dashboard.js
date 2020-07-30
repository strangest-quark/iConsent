import BackendAPI from './backendAPI'

export default {
  postItem (payload) {
    console.log('Hi ' + localStorage.getItem('user-language'))
    return BackendAPI.post('/dashboard', payload, {
      headers: {
        sessionId: String(sessionStorage.getItem('user-sessionId')),
        language: navigator.language
      }
    })
  }
}
