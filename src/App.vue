<template>
  <div id="app">
    <left-nav />
    <section role="main">
      <top-bar />
      <router-view />
    </section>
  </div>
</template>

<script>
  import LeftNav from "@/components/Common/LeftNav.vue";
  import TopBar from "@/components/Common/TopBar.vue";
  export default {
    components: { LeftNav, TopBar },
    name: "app"
  };
</script>

<style lang="scss">
  @import "./assets/styles/reset.css";
  @import "./App.scss";
  [role="main"] {
    margin-left: 240px;
  }
</style>
