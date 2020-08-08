import BackendAPI from './backendAPI'

export default {
  postItem (payload, artifactId) {
    return BackendAPI.post('/consent', payload, {
      headers: {
        sessionId: String(sessionStorage.getItem('user-sessionId')),
        language: localStorage.getItem('user-language'),
        consentArtefactId: String(artifactId)
      }
    })
  }
}
