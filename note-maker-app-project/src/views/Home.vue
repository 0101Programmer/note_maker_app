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

export default defineComponent({
  setup() {
    const route = useRoute();
    const router = useRouter();
    const userStore = useUserStore();

    // Получаем параметр из URL и приводим его к строке
    const tgUsername = Array.isArray(route.params.tg_username)
      ? route.params.tg_username[0] // Берем первый элемент, если это массив
      : route.params.tg_username; // Или используем строку напрямую

    // Устанавливаем tg_username в хранилище
    userStore.setTgUsername(tgUsername);

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