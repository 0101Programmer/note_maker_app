<template>
  <div class="p-4 bg-gradient-to-br from-[#6a11cb] to-[#2575fc] text-white min-h-screen flex flex-col items-center justify-center">
    <!-- Заголовок -->
    <h1 class="text-3xl font-bold mb-8 text-center">Создание новой заметки</h1>

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

export default defineComponent({
  setup() {
    const router = useRouter();
    const userStore = useUserStore();

    // Реактивные данные
    const title = ref('');
    const description = ref('');

    // Проверка валидности формы
    const isFormValid = computed(() => title.value.trim() !== '' && description.value.trim() !== '');

    // Метод для создания заметки
    const createNote = () => {
      if (isFormValid.value) {
        // Добавляем заметку в хранилище
        userStore.addNote({ title: title.value, description: description.value });

        // Очищаем поля
        title.value = '';
        description.value = '';

        // Переходим на страницу со всеми заметками
        router.push({ name: 'all-notes' });
      }
    };

    return {
      title,
      description,
      isFormValid,
      createNote,
    };
  },
});
</script>