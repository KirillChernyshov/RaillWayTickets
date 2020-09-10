import { getRouteInfo } from '../api/index.js'

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
        }
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
        }
    },
    actions: {
        getRouteInfo({ commit }, data) {
            getRouteInfo(data)
                .then(res => {
                    console.log("bookTicket/getRouteInfo");
                    console.log(res.data);
                    commit();
                })
                .catch(err => {
                    console.log(err.response);
                });
        }
    }
}
