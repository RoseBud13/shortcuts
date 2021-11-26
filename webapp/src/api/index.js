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

export function getWeatherInfo(query) {
    return request({
        url: '/get-weather/',
        method: 'get',
        params: query
    })
}
