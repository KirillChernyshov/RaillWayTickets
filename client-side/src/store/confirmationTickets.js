import { getTickets, deleteTicket, verifyTicket } from '../api/index.js'
import moment from 'moment'

export default {
    namespaced: true,
    state: {
        tickets: [],
    },
    mutations: {
        setTickets(state, tickets) {
            this.tickets = [];
            state.tickets = tickets.map(ticket => ({
                ...ticket,
                departure_time: moment(ticket.departure_time).format("DD.MM.YYYY HH:mm"),
                arrival_time: moment(ticket.arrival_time).format("DD.MM.YYYY HH:mm"),
            }));

            // for (let i = 0; i < 100; i++) {
            //     state.tickets.push(tickets[0]);
            // }
        },
    },
    actions: {
        searchTickets({ commit }, data) {
            getTickets(data)
                .then(res => {
                    console.log("confirmationTickets/searchTickets");
                    commit('setTickets', res.data);
                })
                .catch(err => {
                    console.log(err.response);
                })
        },
        cancelReservation({ dispatch }, id) {
            deleteTicket({ ticket_id: id })
                .then(() => {
                    console.log("confirmationTickets/cancelReservation");
                    // dispatch('user/getUserTickets');
                    // dispatch('confirmationTickets/searchTickets');
                    dispatch();
                })
                .catch(err => {
                    console.log(err.response);
                })
        },
        confirmReservation({ state }, id) {
            verifyTicket({ ticket_id: id })
                .then(() => {
                    // commit('removeTicket', id);
                    // dispatch('user/getUserTickets');
                    // dispatch('searchTickets');
                    state;
                })
                .catch(err => {
                    console.log("test");
                    console.log(err);
                })
        },
    }
}
