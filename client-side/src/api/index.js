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

export function getProfile() {
    return axios.get(`${url}/profile`);
}

export function searchRoutes(data) {
    return axios.post(`${url}/search`, data);
}

export function getRouteInfo(data) {
    return axios.post(`${url}/get_route_info`, data);
}

export function getTickets(data) {
    return axios.post(`${url}/search_tickets`, data);
}

export function bookTicket(data) {
    return axios.post(`${url}/book_ticket`, data);
}

export function issueTicket(data) {
    return axios.post(`${url}/place_ticket`, data);
}

export function deleteTicket(data) {
    return axios.post(`${url}/delete_ticket`, data);
}

export function verifyTicket(data) {
    return axios.post(`${url}/verify_ticket`, data);
}
