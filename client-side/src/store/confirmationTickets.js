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
            console.log(data);
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
            return new Promise((res, rej) => {
                deleteTicket({ ticket_id: id })
                .then(() => {
                    console.log("confirmationTickets/cancelReservation");
                    res();
                    dispatch();
                })
                .catch(err => {
                    console.log(err.response);
                    rej();
                })
            });
        },
        confirmReservation({ state }, id) {
            return new Promise((res, rej) => {
                verifyTicket({ ticket_id: id })
                    .then(() => {
                        state;
                        res();
                    })
                    .catch(err => {
                        rej();
                        console.log(err);
                    })
            });
        },
    }
}
