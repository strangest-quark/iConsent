import API from './api'

export default {
  postItem (payload) {
    return API.post('/app/loginwithotp/verify', payload)
  }
}
