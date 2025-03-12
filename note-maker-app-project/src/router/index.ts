import { createRouter, createWebHistory } from 'vue-router'
import { useUserStore } from '../stores/userStore';
import Home from '@/views/Home.vue'
import CreateNote from '@/views/CreateNote.vue'
import ErrorPage from '@/views/ErrorPage.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/:tg_username',  // Динамический параметр
      name: 'home',
      component: Home,
    },
    {
      path: '/create_note', // Страница создания заметки
      name: 'create-note',
      component: CreateNote,
      beforeEnter: (_, __, next) => {
        const userStore = useUserStore();

        // Проверяем, есть ли tg_username в хранилище
        if (!userStore.tgUsername) {
          // Перенаправляем на страницу ошибки
          next({ name: 'error' });
        } else {
          // Разрешаем переход на страницу создания заметки
          next();
        }
      },
    },
    {
      path: '/error', // Страница ошибки
      name: 'error',
      component: ErrorPage,
    },
  ],
})

export default router