<template>
  <div class="comp_indicator" role="rowgroup">
    <div role="rowheader">
      <p class="big-title">-</p>
      <p>광고 효율 지표</p>
    </div>
    <div class="content-wrapper">
      <market-trend-score
        :title="'광고 클릭률'"
        :score="keyword_adTotal_indicator.adClickRate.average + '%'"
        :description1="`PC ${keyword_adTotal_indicator.adClickRate.desktop}%`"
        :description2="
          `MOBILE ${keyword_adTotal_indicator.adClickRate.mobile}%`
        "
      />
      <market-trend-score
        :title="'클릭경쟁률'"
        :score="keyword_adTotal_indicator.clickComp.toFixed(2)"
        :description1="`상품수 ${number_with_comma(keyword_total_count)}개`"
        :description2="`÷ 클릭수 ${count_of_click}회`"
      />
      <market-trend-score
        :title="'가격대비 광고비'"
        :score="keyword_adTotal_indicator.adCostPerPrice"
        :description1="'광고비 원'"
        :description2="'÷ 평균가 원'"
      />
      <market-trend-score
        :title="'클릭대비 광고비'"
        :score="keyword_adTotal_indicator.adCostPerClick"
        :description1="'광고비 원'"
        :description2="`÷ 클릭수 ${count_of_click}회`"
      />
    </div>
  </div>
</template>

<script>
  import { mapState } from "vuex";
  import MarketTrendScore from "./MarketTrendScore.vue";
  export default {
    name: "market-trend-ad",
    components: { MarketTrendScore },
    computed: {
      ...mapState([
        "keyword_adTotal_indicator",
        "keyword_total_count",
        "count_summary"
      ]),
      count_of_click() {
        return this.number_with_comma(
          Math.round(this.count_summary.monthlyAvgClickCnt.total)
        );
      }
    },
    methods: {
      number_with_comma(pureNumber) {
        return pureNumber.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
      }
    }
  };
</script>
