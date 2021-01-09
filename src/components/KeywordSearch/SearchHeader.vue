<template>
  <header class="search-header" :class="{ after_search: search_query }">
    <div class="header-title">
      <strong v-if="!search_query">Step 1. 키워드 검색</strong>
      <strong v-else>"{{ search_query }}"로 검색한 결과입니다.</strong>
    </div>
    <search-box :class="{ after_search: search_query }" />
  </header>
</template>

<script>
  import SearchBox from "@/components/KeywordSearch/SearchBox.vue";
  import { mapState } from "vuex";
  export default {
    components: { SearchBox },
    computed: { ...mapState(["search_query"]) },
    props: {
      is_search: {
        type: Boolean,
        default: false
      }
    }
  };
</script>

<style lang="scss" scoped>
  .search-header {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 26px 0;
    border: 1px solid;

    .header-title {
      width: 700px;
      padding: 23px 0;
      font-size: 25px;
    }
  }
  .search-header.after_search {
    display: block;
    padding: 26px 32px;
    .header-title {
      padding: 10px 0;
      font-size: 14px;
    }
  }
</style>
