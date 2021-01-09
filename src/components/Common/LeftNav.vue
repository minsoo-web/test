<template>
  <nav class="left-nav">
    <div class="logo-wrapper">
      <span>로고</span>
    </div>
    <ul class="nav-list">
      <li><a href="#">키워드 분석</a></li>
    </ul>
  </nav>
</template>

<script>
  export default {
    name: "left-nav"
  };
</script>

<style lang="scss" scoped>
  .left-nav {
    position: fixed;
    top: 0;
    left: 0;
    width: 240px;
    height: 100vh;
    border-right: 1px solid;
    z-index: 99;
    background-color: #fff;

    .logo-wrapper {
      padding: 17px 20px;
      border-bottom: 1px solid;
      font-size: 20px;
    }

    .nav-list {
      padding: 20px;
      font-size: 15px;
      a {
        display: inline-block;
        width: 100%;
      }
    }
  }
</style>
