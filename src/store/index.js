import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    is_search: true,
    search_query: null
  },
  mutations: {
    set_search_state(state, payload) {
      state.is_search = payload;
    },
    set_search_query(state, query) {
      state.search_query = query;
    }
  },
  actions: {
    go_search({ commit }, query) {
      commit("set_search_query", query);
      commit("set_search_state", true);
    }
  },
  modules: {}
});
