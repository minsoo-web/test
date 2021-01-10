<template>
  <div class="comp_indicator" role="rowgroup">
    <div role="rowheader">
      <p class="big-title">-</p>
      <p>경쟁 종합 지표</p>
    </div>
    <div class="content-wrapper">
      <market-trend-score
        :title="'경쟁강도'"
        :score="keyword_compTotal_indicator.compIntensity.toFixed(2)"
        :description1="`상품수 ${number_with_comma(keyword_total_count)}개`"
        :description2="
          `÷ 검색수 ${number_with_comma(
            count_summary.monthlySearchCnt.total
          )}회`
        "
      />
      <market-trend-score
        :title="'실거래상품 비율'"
        :score="keyword_compTotal_indicator.actualDealRate + '%'"
      />
      <market-trend-score
        :title="'묶음상품 비율'"
        :score="keyword_compTotal_indicator.bundleRate + '%'"
      />
      <market-trend-score
        :title="'해외상품 비율'"
        :score="keyword_compTotal_indicator.overseasRate + '%'"
      />
      <market-trend-score
        :title="'1년 내 게시 비율'"
        :score="keyword_compTotal_indicator.postWithinPeriodRate.oneYear + '%'"
        :description1="
          `1개월 ${keyword_compTotal_indicator.postWithinPeriodRate.oneMonth}%, 
          6개월 ${keyword_compTotal_indicator.postWithinPeriodRate.sixMonths}%`
        "
      />
    </div>
  </div>
</template>

<script>
  import { mapState } from "vuex";
  import MarketTrendScore from "./MarketTrendScore.vue";
  export default {
    name: "market-trend-comp",
    components: { MarketTrendScore },
    computed: {
      ...mapState([
        "keyword_compTotal_indicator",
        "keyword_total_count",
        "count_summary"
      ])
    },
    methods: {
      number_with_comma(pureNumber) {
        return pureNumber.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
      }
    }
  };
</script>
