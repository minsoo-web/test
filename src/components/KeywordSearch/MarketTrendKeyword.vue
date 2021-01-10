<template>
  <div class="shop-keyword_indicator" role="rowgroup">
    <div role="rowheader">
      <p class="big-title">-</p>
      <p>쇼핑키워드 지표</p>
    </div>
    <div class="content-wrapper">
      <keyword-tab-list
        :row_title="'PC 섹션'"
        :shop_order="keyword_sectionList.desktopShoppingIdx"
        :keyword_list="keyword_sectionList.desktop"
      />
      <keyword-tab-list
        :row_title="'모바일 섹션'"
        :shop_order="keyword_sectionList.mobileShoppingIdx"
        :keyword_list="keyword_sectionList.mobile"
      />
      <keyword-tab-list
        :row_title="'PC 탭'"
        :shop_order="keyword_tabList.desktopShoppingIdx"
        :keyword_list="keyword_tabList.desktop"
      />
      <keyword-tab-list
        :row_title="'모바일 탭'"
        :shop_order="keyword_tabList.desktopShoppingIdx"
        :keyword_list="keyword_tabList.mobile"
      />
    </div>
  </div>
</template>

<script>
  import { mapState } from "vuex";
  import KeywordTabList from "./KeywordTabList.vue";
  export default {
    components: { KeywordTabList },
    name: "market-trend-keyword",
    computed: { ...mapState(["keyword_tabList", "keyword_sectionList"]) }
  };
</script>

<style lang="scss" scoped>
  .shop-keyword_indicator {
    & > .content-wrapper {
      padding: 10px 0 10px 24px !important;
    }
  }
</style>
