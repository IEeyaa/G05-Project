import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import zhCn from 'element-plus/dist/locale/zh-cn.mjs'
import App from './App.vue'
import router from './router/index.js'
import axios from "axios"


const app = createApp(App)

axios.defaults.baseURL = "http://127.0.0.1:5000"

app.config.globalProperties.$http = axios

app.use(ElementPlus, {locale: zhCn})
app.use(router)
app.mount('#app')
