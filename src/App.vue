<template>
  <TopBar />
  <router-view></router-view>
</template>

<script>
import TopBar from "./components/TopBar.vue";
export default {
  name: "App",
  components: {
    TopBar,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 60px;
}
</style>