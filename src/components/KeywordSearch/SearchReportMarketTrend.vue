<template>
  <div class="search-report-market-trend box">
    <market-trend-comp />
    <market-trend-ad />
    <market-trend-keyword />
  </div>
</template>

<script>
  import MarketTrendAd from "./MarketTrendAd.vue";
  import MarketTrendComp from "./MarketTrendComp.vue";
  import MarketTrendKeyword from "./MarketTrendKeyword.vue";
  export default {
    name: "search-report-market-trend",
    components: { MarketTrendComp, MarketTrendAd, MarketTrendKeyword }
  };
</script>

<style lang="scss">
  .search-report-market-trend {
    width: 96%;
    [class$="_indicator"] {
      display: flex;
      min-height: 120px;

      & > [role="rowheader"] {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        width: 120px;
        border-right: 1px solid #e7e8ef;

        p {
          font-size: 14px;
          &.big-title {
            font-weight: bold;
            font-size: 22px;
          }
        }
      }

      & > .content-wrapper {
        flex: 1;
        padding: 14px 0 0 24px;
      }
      & + [class$="_indicator"] {
        border-top: 1px solid #e7e8ef;
      }
    }
  }
</style>
