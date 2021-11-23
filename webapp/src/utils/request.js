import axios from 'axios'


const service = axios.create({
    // process.env.NODE_ENV === 'development' 来判断是否开发环境
    baseURL: 'http://127.0.0.1:5000/api',
    timeout: 13000
});

export default service;
