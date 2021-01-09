<template>
  <div class="search-report-market-trend box">
    <market-trend-comp />
    <market-trend-ad />
    <div class="shop-keyword_indicator" role="rowgroup">
      <div role="rowheader"></div>
      <div class="content-wrapper"></div>
    </div>
  </div>
</template>

<script>
  import MarketTrendAd from "./MarketTrendAd.vue";
  import MarketTrendComp from "./MarketTrendComp.vue";
  export default {
    name: "search-report-market-trend",
    components: { MarketTrendComp, MarketTrendAd }
  };
</script>

<style lang="scss">
  .search-report-market-trend {
    width: 96%;
    [class$="_indicator"] {
      display: flex;
      min-height: 120px;

      [role="rowheader"] {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        width: 120px;

        p {
          font-size: 14px;
          &.big-title {
            font-weight: bold;
            font-size: 22px;
          }
        }
      }

      .content-wrapper {
        flex: 1;
        border-left: 1px solid;
        padding: 14px 0 0 24px;
      }
      & + [class$="_indicator"] {
        border-top: 1px solid;
      }
    }
  }
</style>
