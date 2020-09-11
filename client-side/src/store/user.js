import { userTickets, getProfile, deleteTicket } from '../api/index.js'
import axios from 'axios'
import moment from 'moment';

export default {
    namespaced: true,
    state: {
        local: {
            firstname: null,
            lastname: null,
            access_token: null,
            role: null,
        },
        email: '',
        tickets: [],
    },
    getters: {
        valid(state) {
            let keys = Object.keys(state.local);

            for (let key of keys)
                if (!state.local[key])
                    return localStorage.isAuth = "";

            return localStorage.isAuth = true;
        },
        name(state) {
            return `${state.local.firstname} ${state.local.lastname}`;
        }
    },
    mutations: {
        setUserData(state, data) {
            let keys = Object.keys(data);
            // console.log("setUserData");
            for (let key of keys) {
                state.local[key] = localStorage[key] = data[key];
            }

            axios.defaults.headers.post['Authorization'] = `Bearer ${localStorage.access_token}`;
            axios.defaults.headers.get['Authorization'] = `Bearer ${localStorage.access_token}`;
        },
        clearUserData(state) {
            let keys = Object.keys(state.local);
            // console.log("clearUserData");
            for (let key of keys) {
                state.local[key] = null;
            }

            localStorage.clear();
        },
        initUserData(state) {
            let keys = Object.keys(state.local);
            // console.log("initUserData");
            for (let key of keys)
                if (!localStorage[key])
                    return this.commit('user/clearUserData');

            this.commit('user/setUserData', localStorage);
        },
        setTickets(state, tickets) {
            state.tickets = tickets.map(ticket => ({
                ...ticket,
                departure_time: moment(ticket.departure_time).format("DD.MM.YYYY HH:mm"),
                arrival_time: moment(ticket.arrival_time).format("DD.MM.YYYY HH:mm"),
                is_booked: (ticket.is_booked) ? 'Забронирован' : 'Оформлен',
            }));

            // for (let i = 0; i < 100; i++) {
            //     state.tickets.push(tickets[0]);
            // }
        },
        removeTicket(state, id) {
            let index = state.tickets.findIndex(ticket => ticket.ticket_id == id)

            if (index == -1)
                return;

            state.tickets.splice(index, 1);
        }
    },
    actions: {
        getUserTickets({ commit }) {
            userTickets()
                .then(res => {
                    console.log("userTickets");
                    commit('setTickets', res.data);
                })
                .catch(er => {
                    console.log(er.response);

                })
        },
        cancelTicketReservation({ dispatch }, id) {
            deleteTicket({ ticket_id: id })
                .then(() => {
                    //commit('removeTicket', id);
                    dispatch('user/getUserTickets');
                })
                .catch(err => {
                    console.log(err.response);
                })
        },
        getProfile({ state }) {
            getProfile()
                .then(res => {
                    state.email = res.data.email;
                })
        }
    }
}
