<template>
  <img aria-label="loading" :src="loading_src" alt="로딩 중" :style="size" />
</template>

<script>
  import { mapState } from "vuex";
  export default {
    name: "loading-gif",
    computed: { ...mapState(["is_search", "loading_src"]) },
    props: {
      size: {
        type: Object,
        default() {
          return {
            width: "200px",
            height: "200px"
          };
        }
      }
    }
  };
</script>

<style></style>
