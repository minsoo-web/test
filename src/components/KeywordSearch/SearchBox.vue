<template>
  <div class="search-box">
    <input
      type="text"
      role="searchbox"
      placeholder="키워드를 입력하세요"
      v-model="search_query"
    />
    <img :src="search_img.src" alt="검색 돋보기" />
  </div>
</template>

<script>
  export default {
    name: "search-box",
    data() {
      return {
        search_img: {
          src: require("@/assets/images/search.png")
        },
        search_query: ""
      };
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
</style>
