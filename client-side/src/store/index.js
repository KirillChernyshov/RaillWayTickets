import Vue from 'vue'
import Vuex from 'vuex'

import auth from './authorization.js'
import reg from './registration.js'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
      auth,
      reg,
  }
})
