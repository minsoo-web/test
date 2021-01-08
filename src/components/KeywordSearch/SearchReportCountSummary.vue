<template>
  <ul class="search-report-count-summary box">
    <li>
      <strong>검색된 상품수</strong>
      <span>1,739,241개</span>
    </li>
    <li>
      <strong>한 달 검색수</strong>
      <span>1,739,241개</span>
    </li>
    <li>
      <strong>검색 비율</strong>
      <span>1,739,241개</span>
    </li>
  </ul>
</template>

<script>
  export default {
    name: "search-report-count-summary"
  };
</script>

<style lang="scss" scoped>
  .search-report-count-summary {
    width: 316px;
    margin-left: 20px;
    li {
      display: flex;
      justify-content: space-between;
      width: 100%;
      padding: 15px;
      font-size: 14px;
      box-sizing: border-box;
    }
  }
</style>
