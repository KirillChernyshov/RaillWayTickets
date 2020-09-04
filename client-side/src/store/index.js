import Vue from 'vue'
import Vuex from 'vuex'

import auth from './authorization.js'
import reg from './registration.js'
import user from './user.js'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        hi: "hi",
    },
    getters: {
        // isAuth(state) {
        //     let keys = Object.keys(state.user.local);
        //     console.log(keys);
        //     console.log(state.user.local)
        //     for (let key of keys) {
        //         console.log(key, state.user.local[key]);
        //         if (!state.user.local[key])
        //             return false
        //     }
        //
        //     return true;
        // }
    },
  mutations: {
  },
  actions: {
  },
  modules: {
      auth,
      reg,
      user,
  }
});
