<template>
  <div class="search-report-related box">
    <div class="related-title">
      <strong>연관 키워드</strong>
    </div>
    <div v-if="is_search">
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
          <tr
            v-for="(keyword, index) in keyword_related"
            v-show="index < show_related_number"
            :key="keyword.tag + index"
          >
            <td>{{ keyword.tag }}</td>
            <td>{{ keyword.searchCount }}</td>
            <td>{{ keyword.productCount }}</td>
          </tr>
        </tbody>
      </table>
      <a
        href="#"
        class="btn-more"
        v-if="related_length > show_related_number"
        @click="related_expand"
      >
        더보기
      </a>
    </div>
    <loading-gif v-else :size="loading_size" />
  </div>
</template>

<script>
  import { mapState } from "vuex";
  import LoadingGif from "@/components/Common/LoadingGif.vue";
  export default {
    name: "search-report-related",
    components: { LoadingGif },
    computed: {
      ...mapState(["is_search", "keyword_related"]),
      loading_size() {
        return {
          width: "100%"
        };
      },
      related_length() {
        return this.keyword_related.length;
      }
    },
    watch: {
      is_search() {
        // 재검색이 이루어지면 초기화
        this.show_related_number = 13;
      }
    },
    data() {
      return {
        show_related_number: 13
      };
    },
    methods: {
      related_expand(e) {
        e.preventDefault();
        this.show_related_number += 10;
      }
    }
  };
</script>

<style lang="scss" scoped>
  .search-report-related {
    width: 250px;
    // min-height: 520px;
    padding: 20px;

    .related-title {
      margin-bottom: 20px;
      font-size: 16px;
    }

    .related-table {
      width: 100%;
      border-spacing: 10px 0;
      font-size: 12px;

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
    .btn-more {
      display: inline-block;
      height: 40px;
      line-height: 40px;
      width: 100%;
      text-align: center;
      text-decoration: underline;
      font-size: 12px;
    }
  }
</style>
