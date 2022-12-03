<template>
  <div>
    主页
    <el-button @click="info">info</el-button>
  </div>
</template>
<script>
export default {
  methods: {
    info(event) {
      if (event) {
        this.$router.push("/info");
      }
    },
  },
};
</script>
