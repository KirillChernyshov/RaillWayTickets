import { getCities, searchRoutes } from '../api/index.js'

export default {
    namespaced: true,
    state: {
        cities: [],
    },
    mutations: {
        setCities(state, cities) {
            state.cities = cities.map((city) => city.city_name);
        },
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
        searchRoutes() {
            searchRoutes()
                .then(res => {
                    console.log("timetable/searchRoutes");
                    console.log(res);
                })
                .catch(er => {
                    console.log(er.response);
                })
        }
    }
}
