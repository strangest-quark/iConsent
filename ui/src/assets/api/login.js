import API from './api'

export default {
  postItem (payload) {
    return API.post('/app/loginwithotp/verify', payload, {
      headers: {
        client_secret: String(process.env.VUE_APP_client_secret),
        client_id: String(process.env.VUE_APP_client_id)
      }
    })
  }
}
