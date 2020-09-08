import { getCities } from '../api/index.js'

export default {
    namespaced: true,
    state: {
        cities: [],
    },
    mutations: {
        setCities(state, cities) {
            state.cities = cities;
        },
    },
    actions: {
        getCitiesList({ commit }) {
            getCities()
                .then(res => {
                    console.log("timetable/getCitiesList");
                    console.log(res.data);
                    commit('setCities', res.data);
                })
                .catch(er => {
                    console.log(er.response);

                })
        }
    }
}
