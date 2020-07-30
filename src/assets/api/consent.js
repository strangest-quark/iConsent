import BackendAPI from './backendAPI'

export default {
  postItem (payload, artifactId, fiuName) {
    return BackendAPI.post('/consent', payload, {
      headers: {
        sessionId: String(sessionStorage.getItem('user-sessionId')),
        language: navigator.language,
        consentArtefactId: String(artifactId),
        fiu: String(fiuName)
      }
    })
  }
}
