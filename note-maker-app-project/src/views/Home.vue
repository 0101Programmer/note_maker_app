<template>
  <div class="p-4 bg-gradient-to-br from-[#6a11cb] to-[#2575fc] text-white min-h-screen flex flex-col justify-center items-center">
    <!-- Заголовок -->
    <h1 class="text-3xl font-bold mb-8 text-center">Привет, {{ tgUsername }}!</h1>

    <!-- Контейнер для меню -->
    <div class="w-full max-w-lg p-6 bg-white/10 backdrop-blur-lg rounded-2xl shadow-lg">
      <!-- Меню -->
      <div class="flex flex-col items-center space-y-4">
        <!-- Кнопка "Все заметки" -->
        <button
          @click="goToNotes"
          class="w-full px-6 py-3 font-bold text-white bg-gradient-to-r from-purple-500 to-indigo-600 rounded-full shadow-lg hover:scale-105 transition-transform duration-200"
        >
          Все заметки
        </button>

        <!-- Кнопка "Создать новую заметку" -->
        <button
          @click="createNewNote"
          class="w-full px-6 py-3 font-bold text-white bg-gradient-to-r from-purple-500 to-indigo-600 rounded-full shadow-lg hover:scale-105 transition-transform duration-200"
        >
          Создать новую заметку
        </button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import { useUserStore } from '@/stores/userStore';
import axios from 'axios';

export default defineComponent({
  setup() {
    const route = useRoute();
    const router = useRouter();
    const userStore = useUserStore();

    // Получаем параметры из URL
    const tgUsername = Array.isArray(route.params.tg_username)
      ? route.params.tg_username[0]
      : route.params.tg_username;

    const sessionID = Array.isArray(route.params.session_id)
      ? route.params.session_id[0]
      : route.params.session_id;

    // Функция для проверки сессии
    const checkSession = async () => {
      try {

        // Используем переменные окружения из .env
        const fastApiHost = import.meta.env.VITE_FASTAPI_HOST;
        const fastApiPort = import.meta.env.VITE_FASTAPI_PORT;

        // Отправляем POST-запрос с данными в формате JSON
        const response = await axios.post(
          `http://${fastApiHost}:${fastApiPort}/set_get_session/check_session`,
          {
            session_id: sessionID,
            tg_username: tgUsername,
          },
          {
            headers: {
              'Content-Type': 'application/json',
            },
          }
        );

        // Проверяем результат
        if (response.data.valid) {
          // Если сессия валидна, сохраняем данные в хранилище
          userStore.setTgUsername(tgUsername);
          userStore.setSessionID(sessionID);
        } else {
          // Если сессия недействительна, перенаправляем на страницу ошибки
          await router.push({ name: 'access-denied' });
          console.log('message', response.data.message);
        }
      } catch (error) {
        console.error('Ошибка при проверке сессии:', error);
        await router.push({ name: 'iternal-error' });
      }
    };

    // Вызываем проверку сессии при загрузке страницы
    checkSession();

    // Переход к списку заметок
    const goToNotes = () => {
      router.push({ name: 'all-notes' });
    };

    // Переход к созданию новой заметки
    const createNewNote = () => {
      router.push({ name: 'create-note' });
    };

    return {
      tgUsername,
      goToNotes,
      createNewNote,
    };
  },
});
</script>