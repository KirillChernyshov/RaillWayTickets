
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
            console.log(state.data);
        },
        hideBookTicket(state) {
            state.data = {};
            state.show = false;
            console.log('bookTicket/hideBookTicket');
        }
    },
}
