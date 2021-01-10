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
        <!-- market trend score -->
        <search-report-market-trend v-if="is_search" />
        <loading-gif v-else :size="loading_size" />
      </div>
      <search-report-related />
    </div>
  </div>
</template>

<script>
  import SearchReportRelated from "@/components/KeywordSearch/SearchReportRelated.vue";
  import SearchReportThumbnail from "@/components/KeywordSearch/SearchReportThumbnail.vue";
  import SearchReportCountSummary from "@/components/KeywordSearch/SearchReportCountSummary.vue";
  import SearchReportMarketTrend from "./SearchReportMarketTrend.vue";
  import { mapState } from "vuex";
  import LoadingGif from "../Common/LoadingGif.vue";

  export default {
    components: {
      SearchReportRelated,
      SearchReportThumbnail,
      SearchReportCountSummary,
      SearchReportMarketTrend,
      LoadingGif
    },
    name: "search-report",
    computed: {
      ...mapState(["is_search"]),
      loading_size() {
        return {
          width: "200px",
          height: "200px"
        };
      }
    }
  };
</script>

<style lang="scss" scoped>
  .search-report {
    padding: 26px 32px;

    .report-title {
      padding: 20px 0;
      font-size: 16px;
    }

    .report-body {
      display: flex;
      justify-content: space-between;
      .report-body-left {
        flex: 1;
        .report-body-top {
          display: flex;
          margin-bottom: 20px;
        }
      }
    }
  }
</style>
