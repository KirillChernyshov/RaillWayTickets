import { getRouteInfo, bookTicket } from '../api/index.js'

export default {
    namespaced: true,
    state: {
        show: false,
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
                dispatch();
                //commit("setWagonInfo", res.data.wagon_seats_info);
            })
            .catch(err => {
                console.log(err.response);
            });
        }
    }
}
