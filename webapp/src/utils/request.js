import axios from 'axios'


const instance = axios.create({
    // process.env.NODE_ENV === 'development' 来判断是否开发环境
    baseURL: 'http://127.0.0.1:5000/api',
    timeout: 13000
});

instance.interceptors.response.use(
    response => {
        if (response.status === 200 || response.status === 201 ) {
            return response.data;
        } else {
            Promise.reject(response)
        }
    },
    error => {
        console.log(error);
        // Any status codes outside the range of 2xx cause this function to trigger
        // Do something with response error
        return Promise.reject(error);
    }
);

export default instance;
