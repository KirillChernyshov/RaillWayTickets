import { getRouteInfo, bookTicket, issueTicket } from '../api/index.js'

export default {
    namespaced: true,
    state: {
        show: false,
        showIssue: false,
        data: {
            route_name: '',
            schedule_id: '',
            dep_station_name: '',
            departure_time: '',
            arr_station_name: '',
            arrival_time: '',
            arr_stop_id: '',
            dep_stop_id: '',
        },
        wagon_seats_info: [],
    },
    mutations: {
        showBookTicket(state, data) {
            state.data = data;
            state.show = true;
            console.log('bookTicket/showBookTicket');
        },
        hideBookTicket(state) {
            state.data = {};
            state.show = false;
            console.log('bookTicket/hideBookTicket');
        },
        showIssueTicket(state, data) {
            state.data = data;
            state.showIssue = true;
            console.log('bookTicket/showIssueTicket');
        },
        hideIssueTicket(state) {
            state.data = {};
            state.showIssue = false;
            console.log('bookTicket/hideIssueTicket');
        },
        setWagonInfo(state, data) {
            state.wagon_seats_info = data;
        }
    },
    actions: {
        getRouteInfo({ commit }, data) {
            getRouteInfo(data)
                .then(res => {
                    console.log("bookTicket/getRouteInfo");
                    commit("setWagonInfo", res.data.wagon_seats_info);
                })
                .catch(err => {
                    console.log(err.response);
                });
        },
        bookTicket({ dispatch }, data) {
            bookTicket(data)
            .then(() => {
                console.log("bookTicket/bookTicket");
                window.ym(67271437,'reachGoal','book_ticket');
                dispatch();
                //commit("setWagonInfo", res.data.wagon_seats_info);
            })
            .catch(err => {
                console.log(err.response);
            });
        },
        issueTicket({ dispatch }, data) {
            issueTicket(data)
            .then(() => {
                console.log("bookTicket/issueTicket");
                dispatch();
                //commit("setWagonInfo", res.data.wagon_seats_info);
            })
            .catch(err => {
                console.log(err.response);
            });
        }
    }
}
