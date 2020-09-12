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
            return new Promise((res, rej) => {
                authorization(data)
                .then(res => {
                    console.log("authorization");
                    router.push("/");
                    commit("user/setUserData", res.data, { root: true });
                    res();
                })
                .catch(er => {
                    if (er.response.status == 400)
                    state.error = "Не верный логин или пароль!";
                    state.waiting = false;
                    rej();
                    setTimeout(() => {
                        state.error = "";
                    }, 10000);
                })

            })

        }
    }
}
