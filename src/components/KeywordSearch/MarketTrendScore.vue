<template>
  <div class="market-trend-score">
    <span class="trend-title">{{ title }}</span>
    <strong class="trend-score">{{ score }}</strong>
    <p class="trend-desc">{{ description1 }}</p>
    <p class="trend-desc">{{ description2 }}</p>
  </div>
</template>

<script>
  export default {
    name: "market-trend-score",
    props: {
      title: {
        type: String,
        required: true
      },
      score: {
        required: true
      },
      description1: {
        type: String,
        required: false
      },
      description2: {
        type: String,
        required: false
      }
    }
  };
</script>

<style lang="scss" scoped>
  .market-trend-score {
    display: inline-flex;
    flex-direction: column;
    justify-content: space-between;
    width: 100px;
    margin-right: 24px;

    .trend-title {
      font-size: 12px;
    }

    .trend-score {
      font-size: 20px;
      margin: 5px 0;
    }

    .trend-desc {
      font-size: 11px;
    }
  }
</style>
