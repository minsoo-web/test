<template>
  <div class="search-report-thumbnail">
    <img v-if="is_search" :src="keyword_thumbnail" alt="키워드 아이템 썸네일" />
    <loading-gif v-else :size="loading_size" />
  </div>
</template>

<script>
  import { mapState } from "vuex";
  import LoadingGif from "@/components/Common/LoadingGif.vue";
  export default {
    name: "search-report-thumbnail",
    components: { LoadingGif },
    computed: {
      ...mapState(["is_search", "keyword_thumbnail"]),
      loading_size() {
        return {
          width: "100%",
          height: "100%"
        };
      }
    }
  };
</script>

<style lang="scss" scoped>
  .search-report-thumbnail {
    width: 150px;
    height: 150px;
    img {
      width: 100%;
      height: 100%;
    }
  }
</style>
