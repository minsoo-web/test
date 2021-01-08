<template>
  <div class="keyword-search" :class="{ after_search: is_search }">
    <search-header :is_search="is_search" />
    <search-report v-if="is_search" />
  </div>
</template>

<script>
  import SearchHeader from "@/components/KeywordSearch/SearchHeader.vue";
  import SearchReport from "@/components/KeywordSearch/SearchReport.vue";
  import { mapState } from "vuex";
  export default {
    name: "keyword-search",
    computed: { ...mapState(["is_search"]) },
    components: { SearchHeader, SearchReport }
  };
</script>

<style lang="scss" scoped>
  .keyword-search {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 30px;
    min-height: 88vh;
  }
  .keyword-search.after_search {
    display: block;
  }
</style>
