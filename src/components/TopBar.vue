<template>
<<<<<<< HEAD
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
    router
  >
    <el-menu-item index="/search"> 论文搜索 </el-menu-item>
    <el-menu-item index="/compare"> 论文比较 </el-menu-item>
    <el-menu-item index="/main"> 用户中心 </el-menu-item>
  </el-menu>
</template>
<script></script>
<style scoped>
.menu-1 > {
  color: #789;
}
</style>
=======
    <el-menu
      :default-active="this.$router.path"
      class="menu-1"
      mode="horizontal"
      @select="handleSelect"
      router
    >
      <el-menu-item index="/">主页</el-menu-item>
      <el-menu-item>
          <div v-if="this.$cookies.get('name') != null">
            <span @click="toInfor()">{{ "欢迎您：" + this.$cookies.get('name')}}</span>
          </div>
          <div v-else>
            <span @click="toInfor()">登录</span>
          </div>
      </el-menu-item>

      <el-menu-item>
          <div v-if="this.$cookies.get('name') != null">
            <span @click="removeCookie()">注销</span>
          </div>
          <div v-else>
            <span @click="removeCookie()">注册</span>
          </div>
      </el-menu-item>


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
      router
    >
      <el-menu-item index="/search"> 论文搜索 </el-menu-item>
      <el-menu-item index="/compare"> 论文比较 </el-menu-item>
      <el-menu-item index="3"> 用户中心 </el-menu-item>
      <el-menu-item index="/statistics"> 数据统计 </el-menu-item>
    </el-menu>
  </template>

  <script>
  import { watch } from 'vue'
  import router from '../router/index.js'
    watch(
        () => router.currentRoute.value['name'],
        (oldValue, newValue) => {
          if(oldValue == "mainHome" && newValue == "login"){
            router.go(0);
          }
        }
    );
  export default {
      // 登录/进入用户界面
      methods: {
        toInfor(){
          if(this.$cookies.get('name') == null) this.$router.push("/login");
          else this.$router.push("/Infor");
        },
        // 注册/注销
        removeCookie(){
          if(this.$cookies.get('name') == null) this.$router.push("/register");
          else{
            this.$cookies.remove("name");
            this.$router.go(0);
          }
        },
      }
    }
</script>



  <style scoped>
  .menu-1 > {
    color: #789;
  }
  </style>
  
>>>>>>> 5de6481e2fcab9763952df165b51fcd1506495f8
