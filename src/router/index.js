import { createRouter, createWebHashHistory} from "vue-router"

const routes = [
    {
        //主页面
        path:'/',
        name:'Home',
        component:()=>import(/*webpackChunkName:'Home'*/ '@/views/HomeView.vue')
    }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router;