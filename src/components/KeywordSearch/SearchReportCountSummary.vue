<template>
  <ul class="search-report-count-summary box">
    <li>
      <strong>검색된 상품수</strong>
      <span v-if="is_search">{{ parsed_result.total }} 개</span>
      <loading-gif v-else :size="loading_size" />
    </li>
    <li>
      <strong>한 달 검색수</strong>
      <span v-if="is_search">{{ parsed_result.month_total }} 회</span>
      <loading-gif v-else :size="loading_size" />
    </li>
    <li>
      <strong>검색 비율</strong>
      <div v-if="is_search" class="search_device_ratio">
        <div
          class="desktop_ratio"
          :style="{ width: `${parsed_result.desktop_ratio}%` }"
        >
          <span>PC {{ parsed_result.desktop_ratio }}%</span>
        </div>
        <div
          class="mobile_ratio"
          :style="{ width: `${parsed_result.mobile_ratio}%` }"
        >
          <span>모바일 {{ parsed_result.mobile_ratio }}%</span>
        </div>
      </div>
      <loading-gif v-else :size="loading_size" />
    </li>
  </ul>
</template>

<script>
  import { mapState } from "vuex";
  import LoadingGif from "@/components/Common/LoadingGif.vue";
  export default {
    name: "search-report-count-summary",
    components: { LoadingGif },
    computed: {
      ...mapState(["is_search", "count_summary"]),
      parsed_result() {
        return {
          total: this.parsing_number(this.count_summary.total),
          month_total: this.parsing_number(this.count_summary.month_total),
          desktop_ratio: this.count_summary.search_device_ratio.desktop,
          mobile_ratio: this.count_summary.search_device_ratio.mobile
        };
      },
      loading_size() {
        return {
          width: "20px",
          height: "20px"
        };
      }
    },
    methods: {
      // 3자리 수 콤마 찍기
      parsing_number(before_parse) {
        return before_parse.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
      }
    }
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

      [class$="_ratio"] {
        position: relative;
        display: inline-block;
        vertical-align: top;
        white-space: nowrap;
        overflow: visible;
        box-sizing: border-box;

        span {
          line-height: 20px;
        }
      }

      .search_device_ratio {
        font-size: 10px;
        color: #fff;
        width: 200px;
        .desktop_ratio {
          text-align: left;
          padding-left: 5px;
          z-index: 1;
          height: 100%;
          background-color: #0da574;
        }

        .mobile_ratio {
          text-align: right;
          padding-right: 5px;
          z-index: 0;
          height: 100%;
          background-color: #083358;
        }
      }
    }
  }
</style>
