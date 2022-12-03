<template>
    <body id="poster">
      <div
        class="layout"
        style="margin-left: 40px; box-shadow: 12px 12px 12px rgba(0, 0, 0, 0.1)"
      >
        <h1>Sign up</h1>
        <el-form
          label-position="left"
          label-width="100px"
          style="max-width: 460px"
          class="loginForm"
        >
          <el-form-item label="用户名">
            <el-input v-model="rName" />
          </el-form-item>
          <el-form-item label="邮箱：">
            <el-input v-model="rEmail" />
          </el-form-item>
          <el-form-item label="密码：">
            <el-input type="password" v-model="rPassword" />
          </el-form-item>
          <el-form-item label="确认密码：">
            <el-input
              type="password"
              v-model="confirmPassword"
              @blur="confirmFunc"
            />
          </el-form-item>
          <el-row>
            <el-checkbox
              class="checkBox"
              v-model="rAgree"
              label="同意用户使用准则"
              name="type"
            />
          </el-row>
          <el-button
            v-if="rAgree"
            type="primary"
            style="width: 96%; margin-bottom: 15px"
            class="loginBtn"
            @click="register"
            color="#90C2C3"
            text-color="#fff"
          >
            注册
          </el-button>
        </el-form>
      </div>
    </body>
  </template>
  
  <script>
  import { reactive, toRefs } from "@vue/reactivity";
  import { ElMessage } from "element-plus";
  export default {
    setup() {
      const registerForm = reactive({
        rEmail: "",
        rPassword: "",
        confirmPassword: "",
        identifyCode: "",
        rAgree: 0,
      });
      // 方法
      // 注册
      function register() {
        console.log("注册", registerForm);
      }
      // 获取验证码
      function getIdentifyCode() {
        console.log("获取验证码");
      }
      // 确认密码
      // function confirmFunc() {
      //   if (registerForm.confirmPassword !== registerForm.rPassword)
      //     alert("密码与确认密码不一致");
      // }
      const confirmFunc = () => {
        if (registerForm.confirmPassword !== registerForm.rPassword)
          ElMessage.error("密码与确认密码不一致.");
      };
      return {
        ...toRefs(registerForm),
  
        register,
        getIdentifyCode,
        confirmFunc,
      };
    },
  };
  </script>
  
  <style scoped>
  .layout {
    position: absolute;
    top: 15%;
    left: calc(50% - 300px);
    border-radius: 15px;
    background-clip: padding-box;
    margin: 90px auto;
    width: 450px;
    padding: 35px 35px 15px 35px;
    background: #fff;
    border: 1px solid #eaeaea;
    box-shadow: 0 0 25px #cac6c6;
  }
  
  #poster {
    /* background: url("../pictures/login.jpg") no-repeat;
    background-position: center; */
    height: 100%;
    width: 100%;
    background-size: cover;
    background-color: #f5feff;
    position: absolute;
  }
  body {
    margin: 0px;
    padding: 0;
  }
  </style>
  