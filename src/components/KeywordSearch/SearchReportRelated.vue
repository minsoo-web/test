<template>
  <div class="search-report-related box">
    <div class="related-title">
      <strong>연관 키워드</strong>
    </div>
    <table class="related-table">
      <caption></caption>
      <thead>
        <tr>
          <th scope="col">키워드</th>
          <th scope="col">검색량</th>
          <th scope="col">상품수</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>여성 롱패딩</td>
          <td>20</td>
          <td>20</td>
        </tr>
        <tr>
          <td>여성 롱패딩</td>
          <td>20</td>
          <td>20</td>
        </tr>
        <tr>
          <td>여성 롱패딩</td>
          <td>20</td>
          <td>20</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
  export default {
    name: "search-report-related"
  };
</script>

<style lang="scss" scoped>
  .search-report-related {
    width: 250px;
    min-height: 520px;
    padding: 0 20px;

    .related-title {
      padding: 20px 0;
      font-size: 14px;
    }

    .related-table {
      width: 100%;
      border-spacing: 10px 0;

      td,
      th {
        padding: 10px 0;
      }

      tr > th:first-child,
      tr > td:first-child {
        text-align: left;
      }

      tr > th,
      tr > td {
        text-align: right;
      }
    }
  }
</style>
