<template>
  <header class="search-header">
    <h1 class="header-title">Step 1. 키워드 검색</h1>
    <search-box />
  </header>
</template>

<script>
  import SearchBox from "@/components/KeywordSearch/SearchBox.vue";
  export default {
    components: { SearchBox }
  };
</script>

<style lang="scss" scoped>
  .search-header {
    margin: 30px 0;

    .header-title {
      padding: 23px 0;
      font-size: 25px;
    }
  }
</style>
