import { authorization } from '../api/index.js'
import router from '../router'

export default {
    namespaced: true,
    state: {
        waiting: false,
        error: "",
    },
    actions: {
        authorization({ state, commit }, data) {
            state.waiting = true;
                authorization(data)
                    .then(res => {
                        console.log("authorization");
                        router.push("/");
                        commit("user/setUserData", res.data, { root: true });
                        window.ym(67271437,'reachGoal','login');
                    })
                    .catch(er => {
                        if (er.response.status == 400)
                        state.error = "Не верный логин или пароль!";
                        state.waiting = false;
                        setTimeout(() => {
                            state.error = "";
                        }, 10000);
                    })
        }
    }
}
