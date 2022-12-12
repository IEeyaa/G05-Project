<template>
  <div>
    <div
      style="
        width: 14%;
        height: 130px;
        border-radius: 100px;
        display: inline-block;
      "
    >
      <img
        style="width: 100%; height: 100%; border-radius: 100px"
        src="@/assets/default-profile.png"
        class="image"
      />
    </div>

    <br />
    <br />
    <el-descriptions :column="1" border>
      <el-descriptions-item label="用户名" v-model="username"
        ><p class="message">{{ username }}</p></el-descriptions-item
      >
      <el-descriptions-item label="邮箱号" v-model="email" class="message"
        ><p class="message">{{ email }}</p></el-descriptions-item
      >
      <el-descriptions-item label="论文收藏数" v-model="level" class="message"
        ><p class="message">{{ number }}</p></el-descriptions-item
      >
      <el-descriptions-item label="座右铭" v-model="motto" class="message"
        ><p class="message">{{ motto }}</p></el-descriptions-item
      >
      <el-descriptions-item label="居住地" v-model="city" class="message"
        ><p class="message">{{ city }}</p></el-descriptions-item
      >
    </el-descriptions>
  </div>
</template>

<script>
export default {
  name: "ShowInfo",
  data() {
    return {
      username: "Test",
      email: "3200100000@zju.edu.cn",
      motto:
        "诸位在校，有两个问题应该自己问问，第一，到浙大来做什么？ 第二，将来毕业后做什么样的人？",
      city: "浙江杭州",
      number: 9999,
    };
  },
};
</script>

<style scoped>
.message {
  width: 20em;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
</style>
