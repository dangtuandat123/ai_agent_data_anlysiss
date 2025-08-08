import { createRouter, createWebHistory } from "vue-router";
import HomePage from "../src/components/HomePage.vue"; // Sửa đường dẫn import
import ChatBot from "../src/components/ChatBot.vue"; // Sửa đường dẫn import

const routes = [
  {
    path: '/',
    name: 'home', // Sửa tên route
    component: HomePage // Sửa tên component
  },
  {
    path: '/chatbot',
    name: 'chatbot', // Sửa tên route
    component: ChatBot // Sửa tên component
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;