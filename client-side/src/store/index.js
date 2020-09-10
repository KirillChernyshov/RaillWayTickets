import Vue from 'vue'
import Vuex from 'vuex'

import auth from './authorization.js'
import reg from './registration.js'
import user from './user.js'
import timetable from './timetable.js'
import bookTicket from './bookTicket.js'
import confirmationTickets from './confirmationTickets.js'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        hi: "hi",
    },
    getters: {

    },
  mutations: {
  },
  actions: {
  },
  modules: {
      auth,
      reg,
      user,
      timetable,
      bookTicket,
      confirmationTickets,
  }
});
