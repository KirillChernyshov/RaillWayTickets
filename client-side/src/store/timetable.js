import { getCities, searchRoutes } from '../api/index.js'
import moment from 'moment'

export default {
    namespaced: true,
    state: {
        cities: [],
        routes: [],
        load: false,
    },
    mutations: {
        setCities(state, cities) {
            state.cities = cities.map((city) => city.city_name);
        },
        setRoutes(state, routes = []) {
            state.routes = routes.map(route => ({
                ...route,
                departure_time: moment(route.departure_time).format("DD.MM.YYYY HH:mm"),
                arrival_time: moment(route.arrival_time).format("DD.MM.YYYY HH:mm"),
                places: route.seats_info.reduce((a, b) => a + b.num_of_places, 0),
            }));

            state.load = false;
        }
    },
    actions: {
        getCitiesList({ commit }) {
            getCities()
                .then(res => {
                    console.log("timetable/getCitiesList");
                    commit('setCities', res.data);
                })
                .catch(er => {
                    console.log(er.response);

                })
        },
        searchRoutes({ commit, state }, data) {
            state.load = true;
            console.log(data);
            searchRoutes(data)
                .then(res => {
                    console.log("timetable/searchRoutes");
                    console.log(res.data);
                    commit('setRoutes', res.data.routes);
                })
                .catch(er => {
                    console.log(er);
                })
        }
    }
}
