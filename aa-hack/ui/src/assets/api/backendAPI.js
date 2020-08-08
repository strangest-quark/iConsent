
import axios from 'axios'

const BackendAPI = axios.create({
  baseURL: 'https://orc132v9be.execute-api.ap-south-1.amazonaws.com/dev/'
})

const isHandlerEnabled = (config = {}) => {
  return !(config.hasOwnProperty.call('handlerEnabled') && !config.handlerEnabled)
}

const requestHandler = (request) => {
  if (isHandlerEnabled(request)) {
    // request.headers.common['Access-Control-Allow-Origin'] = '*'
    // request.headers.client_secret = String(process.env.VUE_APP_client_secret)
    // request.headers.fiu_id = String(process.env.VUE_APP_fiu_id)
    // request.headers.aa_api_key = String(process.env.VUE_APP_aa_api_key)
    // request.headers.client_id = String(process.env.VUE_APP_client_id)
    // request.headers.app_id = String(process.env.VUE_APP_app_id)
  }
  return request
}

BackendAPI.interceptors.request.use(
  request => requestHandler(request)
)

export default BackendAPI
