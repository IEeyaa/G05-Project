import { createRouter, createWebHashHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "mainHome",
    component: () => import("../views/HomeView.vue"),
  },
  {
    path: "/Infor",
    name: "information",
    component: () => import("../views/InforView.vue"),
  },
  {
    path: "/login",
    name: "login",
    component: () => import("../views/LoginView.vue"),
  },
  {
    path: "/register",
    name: "register",
    component: () => import("../views/RegisterView.vue"),
  },
  {
    path: "/search",
    name: "search",
    component: () => import("../views/SearchView.vue"),
  },
  {
    path: "/compare",
    name: "compare",
    component: () => import("../views/CompareView.vue"),
  },
  {
    path: "/compare",
    name: "compare",
    component: () => import("../views/CompareView.vue"),
  },
  {
    path: "/statistics",
    name: "statistics",
    component: () => import("../views/StatisticsView.vue"),
  },
  {
    path: "/main",
    name: "main",
    component: () => import("../views/MainView.vue"),
    children: [
      {
        path: "",
        name: "showinfo",
        component: () => import("../components-main/ShowInfo.vue"),
      },
      {
        path: "infoeditor",
        name: "infoeditor",
        component: () => import("../components-main/InfoEditor.vue"),
      },
      {
        path: "accounteditor",
        name: "accounteditor",
        component: () => import("../components-main/AccountEditor.vue"),
      },
      {
        path: "myarticle",
        name: "myarticle",
        component: () => import("../components-main/MyArticle.vue"),
      },
    ],
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
