import request from '../utils/request'

export function fetchCardStyle(query) {
    return request({
        url: '/cards-info/',
        method: 'get',
        params: query
    })
}

export function fetchCar(query) {
    return request({
        url: '/car/',
        method: 'get',
        params: query
    })
}

export function getDateInfo(query) {
    return request({
        url: '/get-datetime/',
        method: 'get',
        params: query
    })
}

export function getWeatherInfo(query) {
    return request({
        url: '/get-weather/',
        method: 'get',
        params: query
    })
}

export function fetchTemplates(query) {
    return request({
        url: '/get-templates/',
        method: 'get',
        params: query
    })
}

export function executeTemplate(template) {
    return request({
        url: `/excecute-template/?template=${template}`,
        method: 'get'
    })
}

export function fetchAllMethods(query) {
    return request({
        url: '/get-all-methods/',
        method: 'get',
        params: query
    })
}

export function sendTemplate(data) {
    return request({
      url: '/create-template/',
      method: 'post',
      data
    })
  }
