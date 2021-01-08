<template>
  <div class="search-box" :class="{ after_search: is_search }">
    <input
      type="text"
      role="searchbox"
      placeholder="키워드를 입력하세요"
      v-model="search_query"
      @keypress.enter="go_search(search_query)"
    />
    <img
      :src="search_img.src"
      alt="검색 돋보기"
      @click="go_search(search_query)"
    />
  </div>
</template>

<script>
  import { mapActions } from "vuex";
  export default {
    name: "search-box",
    data() {
      return {
        search_img: {
          src: require("@/assets/images/search.png")
        },
        search_query: ""
      };
    },
    props: {
      is_search: {
        type: Boolean,
        default: false
      }
    },
    methods: {
      ...mapActions(["go_search"])
    }
  };
</script>

<style lang="scss" scoped>
  .search-box {
    display: flex;
    align-items: center;
    width: 700px;
    height: 82px;
    padding-right: 18px;

    border: 1px solid #ffd400;
    box-sizing: border-box;
    border-radius: 3px;
    input {
      width: 100%;
      height: 100%;
      padding: 11px 0 11px 18px;

      font-size: 14px;
      font-weight: 400;
      box-sizing: border-box;
    }
    img {
      cursor: pointer;
      width: 25px;
      height: 25px;
    }
  }

  .search-box.after_search {
    width: 450px;
    height: 40px;

    img {
      width: 17px;
      height: 17px;
    }
  }
</style>
