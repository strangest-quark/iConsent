import BackendAPI from './backendAPI'

const headerContent = {
  sessionId: String(sessionStorage.getItem('user-sessionId')),
  language: localStorage.getItem('user-language')
}

export default {
  postItem (payload) {
    return BackendAPI.post('/dashboard', payload, {
      headers: headerContent
    })
  }
}
