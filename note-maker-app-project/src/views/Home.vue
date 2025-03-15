<template>
  <div class="p-4 bg-gradient-to-br from-[#6a11cb] to-[#2575fc] text-white min-h-screen flex flex-col justify-center items-center">
    <!-- Заголовок -->
    <h1 class="text-3xl font-bold mb-8 text-center">Привет, {{ tgUsername }}!</h1>

    <!-- Отображение таймера -->
    <div v-if="sessionTTL !== null" class="mb-4 text-center">
      <p class="text-lg font-semibold text-gray-200">
        Ваша сессия активна. Время до завершения:
        <span class="text-xl font-bold text-white">{{ formattedTime }}</span>
      </p>
      <p class="text-sm text-gray-400 mt-2">
        После завершения сессии вам потребуется перезайти в приложение.
      </p>

      <!-- Выпадающий список для выбора времени -->
      <div class="mt-4">
        <select v-model="selectedDuration" class="px-4 py-2 border rounded-md text-gray-700">
          <option value="60">1 минута</option>
          <option value="1800">30 минут</option>
          <option value="3600">1 час</option>
        </select>

        <!-- Кнопка "Продлить сессию" -->
        <button
          @click="extendSession(selectedDuration)"
          class="ml-2 px-4 py-2 bg-gradient-to-r from-purple-500 to-indigo-600 text-white font-bold rounded-full shadow-lg hover:scale-105 transition-transform duration-200"
        >
          Продлить сессию
        </button>
      </div>
    </div>

    <!-- Сообщение об истечении сессии -->
    <div v-else class="mb-4 text-center">
      <p class="text-lg font-semibold text-red-400">
        Сессия истекла или не существует.
      </p>
      <p class="text-sm text-gray-400 mt-2">
        Пожалуйста, войдите в приложение заново.
      </p>
    </div>

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
import { defineComponent, ref, computed, onMounted, onUnmounted } from 'vue';
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

    // Состояние для хранения TTL
    const sessionTTL = ref<number | null>(null);

    // Форматирование времени
    const formattedTime = computed(() => {
      if (sessionTTL.value === null) return '';
      const minutes = Math.floor(sessionTTL.value / 60);
      const seconds = sessionTTL.value % 60;
      return `${minutes}:${seconds.toString().padStart(2, '0')}`;
    });

    // Функция для проверки TTL сессии
    const fetchSessionTTL = async () => {
      try {
        const fastApiHost = import.meta.env.VITE_FASTAPI_HOST;
        const fastApiPort = import.meta.env.VITE_FASTAPI_PORT;

        const response = await axios.post(
          `http://${fastApiHost}:${fastApiPort}/set_get_session/check_session_timer`,
          { tg_username: tgUsername },
          { headers: { 'Content-Type': 'application/json' } }
        );

        const ttl = response.data.ttl;
        if (ttl !== null && ttl > 0) {
          sessionTTL.value = ttl;
        } else {
          sessionTTL.value = null; // Сессия истекла
        }
      } catch (error) {
        console.error('Ошибка при получении TTL:', error);
        sessionTTL.value = null;
      }
    };

    // Периодическое обновление TTL
    const startTTLUpdate = () => {
      const interval = setInterval(() => {
        if (sessionTTL.value !== null && sessionTTL.value > 0) {
          sessionTTL.value -= 1; // Уменьшаем TTL каждую секунду
        } else {
          clearInterval(interval); // Останавливаем интервал, если TTL <= 0
        }
      }, 1000);

      // Обновляем TTL с сервера каждые 30 секунд
      const serverUpdateInterval = setInterval(fetchSessionTTL, 30000);

      // Очищаем интервалы при размонтировании компонента
      onUnmounted(() => {
        clearInterval(interval);
        clearInterval(serverUpdateInterval);
      });
    };

    // Вызываем проверку сессии при загрузке страницы
    onMounted(() => {
      fetchSessionTTL();
      startTTLUpdate();
    });

    // Состояние для хранения выбранного времени продления
    const selectedDuration = ref<number>(60); // По умолчанию 1 минута

    // Функция для продления сессии
    const extendSession = async (duration: number) => {
      try {
        const fastApiHost = import.meta.env.VITE_FASTAPI_HOST;
        const fastApiPort = import.meta.env.VITE_FASTAPI_PORT;

        const response = await axios.post(
          `http://${fastApiHost}:${fastApiPort}/set_get_session/update_session_timer`,
          { tg_username: tgUsername, duration },
          { headers: { 'Content-Type': 'application/json' } }
        );

        console.log('Сессия продлена:', response.data);

        // Обновляем TTL после продления
        await fetchSessionTTL();
      } catch (error) {
        console.error('Ошибка при продлении сессии:', error);
        alert('Не удалось продлить сессию. Попробуйте снова.');
      }
    };

    // Функция для проверки ID сессии
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

    // Возвращаем все переменные и методы, которые нужны в шаблоне
    return {
      tgUsername,
      sessionTTL,
      formattedTime,
      goToNotes,
      createNewNote,
      extendSession,
      selectedDuration,
    };
  },
});
</script>