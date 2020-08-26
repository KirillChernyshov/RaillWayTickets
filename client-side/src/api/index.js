import axios from 'axios'

let url = "http://localhost:5000"

export function registration (data) {
    return axios.post(`${url}/register`, data)
}

export function authorization (data) {
    return axios.post(`${url}/login`, data)
}
