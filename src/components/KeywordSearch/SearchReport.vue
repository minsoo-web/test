<template>
  <div class="search-report">
    <div class="report-title">
      <strong>Step 2. 분석 보고서</strong>
    </div>
    <div class="report-body">
      <div class="report-body-left">
        <div class="report-body-top">
          <search-report-thumbnail />
          <search-report-count-summary />
        </div>
      </div>
      <search-report-related />
    </div>
  </div>
</template>

<script>
  import SearchReportRelated from "@/components/KeywordSearch/SearchReportRelated.vue";
  import SearchReportThumbnail from "@/components/KeywordSearch/SearchReportThumbnail.vue";
  import SearchReportCountSummary from "@/components/KeywordSearch/SearchReportCountSummary.vue";

  export default {
    components: {
      SearchReportRelated,
      SearchReportThumbnail,
      SearchReportCountSummary
    },
    name: "search-report"
  };
</script>

<style lang="scss" scoped>
  .search-report {
    padding: 26px 32px;
    border: 1px solid;

    .report-title {
      padding: 10px 0;
      font-size: 14px;
    }

    .report-body {
      display: flex;
      justify-content: space-between;

      .report-body-top {
        display: flex;
      }
    }
  }
</style>
