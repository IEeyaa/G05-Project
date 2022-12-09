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
  }
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
