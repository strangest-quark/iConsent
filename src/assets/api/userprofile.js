import API from './api'

export default {
  postItem (payload) {
    return API.get('/user/user-profile', {
      headers: {
        sessionId: String(sessionStorage.getItem('user-sessionId'))
      }
    })
  }
}
