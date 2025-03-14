<template>
  <div class="p-4 bg-gradient-to-br from-[#6a11cb] to-[#2575fc] text-white min-h-screen flex flex-col items-center justify-center">
    <!-- Кнопка "Назад" -->
    <button
      @click="goBack"
      class="mb-6 px-4 py-2 font-bold text-purple-500 bg-white rounded-full shadow-lg hover:bg-purple-500 hover:text-white transition-colors duration-200"
    >
      Назад
    </button>

    <!-- Заголовок -->
    <h1 class="text-3xl font-bold mb-8 text-center">Создание новой заметки</h1>

    <!-- Сообщение об успехе -->
    <div v-if="successMessage" class="mb-4 text-green-400 font-bold">
      {{ successMessage }}
    </div>

    <!-- Форма -->
    <div class="w-full max-w-lg p-6 bg-white/10 backdrop-blur-lg rounded-2xl shadow-lg">
      <!-- Поле для заголовка -->
      <div class="mb-4">
        <label class="block text-lg mb-2 text-gray-300">Заголовок:</label>
        <input
          v-model="title"
          type="text"
          placeholder="Введите заголовок"
          class="w-full p-3 border border-gray-700 rounded-lg bg-transparent text-white placeholder:text-gray-400 focus:outline-none focus:border-purple-500 transition-colors duration-200"
        />
      </div>

      <!-- Поле для описания -->
      <div class="mb-6">
        <label class="block text-lg mb-2 text-gray-300">Описание:</label>
        <textarea
          v-model="description"
          placeholder="Введите описание"
          rows="4"
          class="w-full p-3 border border-gray-700 rounded-lg bg-transparent text-white placeholder:text-gray-400 focus:outline-none focus:border-purple-500 transition-colors duration-200"
        ></textarea>
      </div>

      <!-- Кнопка "Создать" -->
      <button
        @click="createNote"
        :disabled="!isFormValid"
        :class="[
          'w-full px-6 py-3 font-bold rounded-full shadow-lg transition-transform duration-200',
          isFormValid
            ? 'bg-gradient-to-r from-purple-500 to-indigo-600 hover:scale-105'
            : 'bg-gray-500 cursor-not-allowed'
        ]"
      >
        Создать
      </button>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, computed } from 'vue';
import { useRouter } from 'vue-router';
import { useUserStore } from '@/stores/userStore';
import axios from 'axios';

export default defineComponent({
  setup() {
    const router = useRouter();
    const userStore = useUserStore();

    // Реактивные данные
    const title = ref('');
    const description = ref('');
    const successMessage = ref<string | null>(null); // Объявляем successMessage

    // Проверка валидности формы
    const isFormValid = computed(() => title.value.trim() !== '' && description.value.trim() !== '');

    // Метод для создания заметки
    const createNote = async () => {
      if (!isFormValid.value) return;

      try {
        // Получаем tg_username из хранилища
        const { tgUsername } = userStore;
        if (!tgUsername) {
          console.error("Ошибка: tgUsername не найден в хранилище.");
          return;
        }

        // Отправляем данные на сервер
        const response = await axios.post(`http://localhost:8000/notes/create_note/${tgUsername}`, {
          title: title.value,
          content: description.value, // Передаем описание как "content"
        });

        // Если всё успешно
        if (response.data.status) {
          successMessage.value = "Заметка успешно создана!";
          title.value = ''; // Очищаем поля формы
          description.value = '';
        }
      } catch (error) {
        console.error("Ошибка при создании заметки:", error);
        successMessage.value = "Произошла ошибка при создании заметки.";
      }
    };

    // Метод для кнопки "Назад"
    const goBack = () => {
      const { sessionID, tgUsername } = userStore;
      if (sessionID && tgUsername) {
        router.push({ path: `/${sessionID}/${tgUsername}` });
      } else {
        console.error("Ошибка: sessionID или tgUsername не найдены в хранилище.");
      }
    };

    return {
      title,
      description,
      successMessage, // Возвращаем successMessage
      isFormValid,
      createNote,
      goBack,
    };
  },
});
</script>