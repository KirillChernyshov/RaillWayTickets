

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
        }
    },
    actions: {

    }
}
