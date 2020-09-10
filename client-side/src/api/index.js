import axios from 'axios'

let url = "http://localhost:5000"

export function registration (data) {
    return axios.post(`${url}/register`, data)
}

export function authorization (data) {
    return axios.post(`${url}/login`, data)
}

export function userTickets() {
    return axios.get(`${url}/user_tickets`);
}

export function getCities() {
    return axios.get(`${url}/cities`);
}

export function searchRoutes(data) {
    return axios.post(`${url}/search`, data);
}

export function getRouteInfo(data) {
    return axios.get(`${url}/get_route_info`, data);
}

export function getTickets(data) {
    console.log(data);
    return axios.post(`${url}/search_tickets`, data);
}
