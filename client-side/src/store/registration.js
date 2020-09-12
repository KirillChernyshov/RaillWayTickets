import { registration } from '../api/index.js'
import router from '../router'

export default {
    namespaced: true,
    state: {
        waiting: false,
        error: "",
    },
    actions: {
        registration({ state, commit }, data) {
            state.waiting = true;
            registration(data)
                .then(res => {
                    console.log("registration");
                    window.ym(67271437,'reachGoal','register');
                    router.push("/");
                    commit("user/setUserData", res.data, { root: true });
                })
                .catch(er => {
                    console.log(er.response, er.response.status == 422);
                    if (er.response.status == 400)
                        state.error = "Данный почтовый адрес уже занят! :(";
                        state.waiting = false;

                        setTimeout(() => {
                            state.error = "";
                        }, 10000);
                })
        }
    }
}
