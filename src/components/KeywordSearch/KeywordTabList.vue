<template>
  <div class="keyword-tab-list" role="rowgroup">
    <div role="rowheader">
      <span>{{ row_title }}</span>
      <span class="shop_order">
        <strong>{{ shop_order + 1 }}</strong>
        위
      </span>
    </div>
    <ul class="list-wrapper">
      <li
        v-for="(item, index) in keyword_list"
        :key="row_title + index"
        v-show="index < 7"
        :class="{ active: shop_order == index }"
      >
        <span>{{ item }}</span>
      </li>
    </ul>
  </div>
</template>

<script>
  export default {
    name: "keyword-tab-list",
    props: {
      row_title: {
        type: String,
        required: true
      },
      // 쇼핑 키워드 순위
      shop_order: {
        type: Number,
        required: true
      },
      keyword_list: {
        type: Array,
        required: true
      }
    }
  };
</script>

<style lang="scss" scoped>
  .keyword-tab-list {
    display: flex;
    font-size: 12px;
    padding: 10px 0;

    & > [role="rowheader"] {
      display: flex;
      justify-content: space-between;
      align-items: center;
      width: 120px;
      .shop_order > strong {
        color: #eac100;
      }
    }
    .list-wrapper {
      flex: 1;
      margin-left: 30px;
      li {
        display: inline-block;
        padding: 5px 10px;
        border: 1px solid #e7e8ef;
        border-radius: 2px;

        & + li {
          margin-left: 15px;
        }
        &.active {
          border: 1px solid #eac100;
        }
      }
    }
  }
</style>
