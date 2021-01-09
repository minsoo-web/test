<template>
  <div id="app">
    <left-nav />
    <section role="main" :class="{ expand: is_search }">
      <top-bar />
      <router-view />
    </section>
  </div>
</template>

<script>
  import LeftNav from "@/components/Common/LeftNav.vue";
  import TopBar from "@/components/Common/TopBar.vue";
  import { mapState } from "vuex";
  export default {
    components: { LeftNav, TopBar },
    name: "app",
    computed: { ...mapState(["is_search"]) }
  };
</script>

<style lang="scss">
  @import "./assets/styles/reset.css";
  @import "./App.scss";
</style>
