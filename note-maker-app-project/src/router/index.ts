import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/:tg_username',  // Динамический параметр
      name: 'home',
      component: Home,
    },
  ],
})

export default router