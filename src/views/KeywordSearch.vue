<template>
  <div class="keyword-search">
    <search-header />
  </div>
</template>

<script>
  import SearchHeader from "@/components/KeywordSearch/SearchHeader.vue";
  export default {
    name: "keyword-search",
    components: { SearchHeader }
  };
</script>

<style lang="scss" scoped>
  .keyword-search {
    padding: 0 30px;
  }
</style>
