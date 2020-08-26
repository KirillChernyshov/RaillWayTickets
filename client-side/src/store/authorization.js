import { authorization } from '../api/index.js'

export default {
    namespaced: true,
    state: {
        waiting: false,
        error: "",
    },
    actions: {
        authorization({ state }, data) {
            state.waiting = true;
            data;
            authorization({ email: "test@test.ru", password: "11211121"})
                .then(res => {
                    console.log(res.data);
                })
                .catch(er => {
                    console.log(er.response, er.response.status == 422);
                    if (er.response.status == 422)
                        state.error = "Данный пользователь уже зарегистрирован!";
                        state.waiting = false;

                        setTimeout(() => {
                            state.error = "";
                        }, 10000);
                })
        }
    }
}
