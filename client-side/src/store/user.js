import { userTickets } from '../api/index.js'
import axios from 'axios'

export default {
    namespaced: true,
    state: {
        local: {
            firstname: null,
            lastname: null,
            access_token: null,
            role: null,
        }
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

            axios.defaults.headers.post['Bearer'] = localStorage.access_token;
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
    },
    actions: {
        getUserTickets({ state }) {
            userTickets()
                .then(res => {
                    console.log("userTickets", state);
                    console.log(res.data);
                    //router.push("/");
                    //commit("user/setUserData", res.data, { root: true });
                })
                .catch(er => {
                    console.log(er.response, er.response.status == 422);
                    // if (er.response.status == 400)
                    //     state.error = "Данный почтовый адрес уже занят! :(";
                    //     state.waiting = false;
                    //
                    //     setTimeout(() => {
                    //         state.error = "";
                    //     }, 10000);
                })
        },

    }
}
