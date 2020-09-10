import { getTickets } from '../api/index.js'

export default {
    namespaced: true,
    state: {
        tickets: '',
    },
    actions: {
        searchTickets({ state }, data) {
            getTickets(data)
                .then(res => {
                    console.log("confirmationTickets/searchTickets");
                    console.log(res.data);
                    state;
                    data;
                })
                .catch(err => {
                    console.log(err.response);
                })
        }
    }
}
