import API from './api'

export default {
  postItem (payload) {
    return API.post('/user/user-profile', payload, {
      headers: {
        sessionId: String(sessionStorage.getItem('user-sessionId'))
      }
    })
  }
}
