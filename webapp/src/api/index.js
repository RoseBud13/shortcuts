import request from '../utils/request'

export function fetchCardStyle(query) {
    return request({
        url: '/cards-info/',
        method: 'get',
        params: query
    })
}
