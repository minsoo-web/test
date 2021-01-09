import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    is_search: false,
    search_query: null,
    loading_src: require("@/assets/images/loading.gif"),
    keyword_thumbnail: null,
    count_summary: null
  },
  mutations: {
    set_search_state(state, payload) {
      state.is_search = payload;
    },
    set_search_query(state, query) {
      state.search_query = query;
    },
    set_thumbnail(state, payload) {
      state.keyword_thumbnail = payload;
    },
    set_countSummary(state, payload) {
      state.count_summary = payload;
    }
  },
  actions: {
    async go_search({ commit }, query) {
      console.log("검색 시작");
      commit("set_search_state", false);
      commit("set_search_query", query);

      // setTimeout(() => {
      //   console.log("검색 끝");
      //   commit("set_search_state", true);
      // }, 2000);

      await axios
        .get(`https://sckroll-insights.herokuapp.com/api/v1?q=${query}`)
        .then(res => {
          // thumbnail
          commit("set_thumbnail", res.data.thumbnail);

          // count_summary
          commit("set_countSummary", {
            total: res.data.totalCount, // 전체 상품 수,
            month_total: res.data.relKeywordStat.monthlySearchCnt.total, // 한 달 검색 수
            search_device_ratio: res.data.relKeywordStat.monthlySearchRate // 객체, desktop, mobile
          });
          console.log(res);
          commit("set_search_query", query);
          commit("set_search_state", true);
        })
        .catch(err => {
          console.log(err);
        });
    }
  },
  modules: {}
});
