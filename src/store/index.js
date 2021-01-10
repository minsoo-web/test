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
    keyword_total_count: null,
    count_summary: null,
    keyword_related: null,
    keyword_compTotal_indicator: null, // 경쟁 종합 지표 객체
    keyword_adTotal_indicator: null, // 광고 효율 지표 객체
    keyword_tabList: null,
    keyword_sectionList: null
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
    set_total_count(state, payload) {
      // 3자리 수 콤마 찍기
      state.keyword_total_count = payload;
    },
    set_countSummary(state, payload) {
      state.count_summary = payload;
    },
    set_related(state, payload) {
      state.keyword_related = payload;
    },
    set_compIdx(state, payload) {
      state.keyword_compTotal_indicator = payload;
    },
    set_adIdx(state, payload) {
      state.keyword_adTotal_indicator = payload;
    },
    set_tabList(state, payload) {
      state.keyword_tabList = payload;
    },
    set_sectionList(state, payload) {
      state.keyword_sectionList = payload;
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

          // 전체 상품 수
          commit("set_total_count", res.data.totalCount);

          // count_summary
          commit("set_countSummary", res.data.relKeywordStat);

          // 연관 검색어
          commit("set_related", res.data.relatedTags);

          // 경쟁 종합 지표
          commit("set_compIdx", res.data.compTotalIdx);

          // 광고 효율 지표
          commit("set_adIdx", res.data.adEfficiencyIdx);

          // 쇼핑 키워드 지표 (tab)
          commit("set_tabList", res.data.tabList);
          // 쇼핑 키워드 지표 (section)
          commit("set_sectionList", res.data.sectionList);

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
