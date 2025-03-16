<template>
  <div class="p-4 bg-gradient-to-br from-[#6a11cb] to-[#2575fc] text-white min-h-screen">
    <!-- Заголовок -->
    <h1 class="text-3xl font-bold mb-8 text-center">Ваши заметки</h1>

    <!-- Индикатор загрузки -->
    <div v-if="isLoading" class="text-center text-gray-400">
      <p class="text-lg font-semibold">Загрузка заметок...</p>
    </div>

    <!-- Список заметок -->
    <div v-else-if="notes.length > 0" class="space-y-4">
      <div
        v-for="note in notes"
        :key="note.id"
        class="p-6 bg-white/10 backdrop-blur-lg rounded-2xl shadow-lg transition-transform duration-200 hover:scale-105 relative group"
      >
        <!-- Кнопка удаления -->
        <button
          @click="deleteNote(note.id)"
          class="absolute top-3 right-3 p-1.5 bg-gradient-to-br from-[#6a11cb]/20 to-[#2575fc]/20 rounded-full text-gray-300 opacity-0 group-hover:opacity-100 transition-opacity duration-300 hover:text-white hover:from-[#6a11cb]/50 hover:to-[#2575fc]/50"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-5 w-5"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M6 18L18 6M6 6l12 12"
            />
          </svg>
        </button>

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
import { defineComponent, onMounted, computed } from 'vue';
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

    // Реактивное получение заметок
    const notes = computed(() => userStore.notes);

    // Реактивный флаг загрузки
    const isLoading = computed(() => userStore.isLoading);

    // Возвращение на главную страницу
    const goBack = () => {
      const { sessionID, tgUsername } = userStore;
      if (sessionID && tgUsername) {
        router.push({ path: `/${sessionID}/${tgUsername}` });
      } else {
        console.error("Ошибка: sessionID или tgUsername не найдены в хранилище.");
      }
    };

    // Удаление заметки
    const deleteNote = async (noteId: number) => {
      if (confirm('Вы уверены, что хотите удалить эту заметку?')) {
        await userStore.deleteNote(noteId);
      }
    };

    // Получаем заметки при загрузке компонента
    onMounted(async () => {
      try {
        await userStore.fetchNotes(); // Ждем завершения загрузки
      } catch (error) {
        console.error('Ошибка при загрузке заметок:', error);
      }
    });

    return {
      notes, // Реактивные заметки
      isLoading, // Реактивный флаг загрузки
      formatDate,
      goBack,
      deleteNote,
    };
  },
});
</script>