<template>
    <el-menu
      :default-active="this.$router.path"
      class="menu-1"
      mode="horizontal"
      @select="handleSelect"
      router
    >
      <el-menu-item index="/"> 主页 </el-menu-item>
      <el-menu-item index="/login"> 登录 </el-menu-item>
      <el-menu-item index="/register"> 注册 </el-menu-item>
    </el-menu>
  
    <el-menu
      :default-active="activeIndex2"
      class="menu-2"
      mode="horizontal"
      background-color="#90C2C3"
      text-color="#fff"
      active-text-color="#ffd04b"
      popper-effect="light"
      @select="handleSelect"
    >
      <el-menu-item index="1"> 论文导航 </el-menu-item>
      <el-menu-item index="2"> 论文比较 </el-menu-item>
      <el-menu-item index="3"> 用户中心 </el-menu-item>
    </el-menu>
  </template>
  <script></script>
  <style scoped>
  .menu-1 > {
    color: #789;
  }
  </style>
  