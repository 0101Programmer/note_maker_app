<template>
  <div class="p-4 bg-gradient-to-br from-[#6a11cb] to-[#2575fc] text-white min-h-screen">
    <!-- Заголовок -->
    <h1 class="text-3xl font-bold mb-8 text-center">Ваши заметки</h1>

    <!-- Список заметок -->
    <div v-if="notes.length > 0" class="space-y-4">
      <div
        v-for="note in notes"
        :key="note.id"
        class="p-6 bg-white/10 backdrop-blur-lg rounded-2xl shadow-lg transition-transform duration-200 hover:scale-105"
      >
        <h2 class="text-xl font-bold text-white">{{ note.title }}</h2>
        <p class="mt-2 text-gray-300">{{ note.content }}</p>
        <div class="mt-4 text-sm text-gray-400">
          Создано: {{ formatDate(note.created_at) }}<br />
          Обновлено: {{ formatDate(note.updated_at) }}
        </div>
      </div>
    </div>

    <!-- Сообщение об отсутствии заметок -->
    <div v-else class="text-center text-gray-400">
      <p class="text-lg font-semibold">У вас пока нет заметок.</p>
      <p class="text-sm mt-2">Вы можете создать новую заметку, нажав на соответствующую кнопку.</p>
    </div>

    <!-- Кнопка "Назад" -->
    <button
      @click="goBack"
      class="mt-8 px-6 py-3 font-bold text-white bg-gradient-to-r from-purple-500 to-indigo-600 rounded-full shadow-lg hover:scale-105 transition-transform duration-200"
    >
      Назад
    </button>
  </div>
</template>

<script lang="ts">
import { defineComponent, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useUserStore } from '@/stores/userStore';

export default defineComponent({
  setup() {
    const router = useRouter();
    const userStore = useUserStore();

    // Форматирование даты
    const formatDate = (dateString: string) => {
      const date = new Date(dateString);
      return date.toLocaleString(); // Форматируем дату в удобочитаемый вид
    };

    // Возвращение на главную страницу
    const goBack = () => {
      const { sessionID, tgUsername } = userStore;
      if (sessionID && tgUsername) {
        router.push({ path: `/${sessionID}/${tgUsername}` });
      } else {
        console.error("Ошибка: sessionID или tgUsername не найдены в хранилище.");
      }
    };

    // Получаем заметки при загрузке компонента
    onMounted(() => {
      userStore.fetchNotes();
    });

    return {
      notes: userStore.notes, // Достаем заметки из стора
      formatDate,
      goBack,
    };
  },
});
</script>