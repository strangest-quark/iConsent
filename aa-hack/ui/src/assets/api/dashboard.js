import BackendAPI from './backendAPI'

export default {
  postItem (payload) {
    return BackendAPI.post('/dashboard', payload, {
      headers: {
        sessionId: String(sessionStorage.getItem('user-sessionId')),
        language: localStorage.getItem('user-language')
      }
    })
  }
}
