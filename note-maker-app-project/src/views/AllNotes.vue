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
        class="p-6 bg-white/10 backdrop-blur-lg rounded-2xl shadow-lg transition-transform duration-200 hover:scale-105 relative group transform-gpu backface-hidden"
      >
        <!-- Кнопка удаления -->
        <button
          @click="deleteNote(note.id)"
          class="absolute top-3 right-3 p-2 text-gray-300 opacity-0 group-hover:opacity-100 transition-opacity duration-300 rounded-full hover:bg-white/20 hover:text-white"
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

        <!-- Кнопка редактирования -->
        <button
          v-if="!note.isEditing"
          @click="startEditing(note)"
          class="absolute top-3 left-3 p-2 text-gray-300 opacity-0 group-hover:opacity-100 transition-opacity duration-300 rounded-full hover:bg-white/20 hover:text-white"
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
              d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z"
            />
          </svg>
        </button>

        <!-- Кнопка сохранения -->
        <button
          v-else
          @click="saveNote(note)"
          class="absolute top-3 left-3 p-2 text-green-400 opacity-0 group-hover:opacity-100 transition-opacity duration-300 rounded-full hover:bg-green-400/20 hover:text-white"
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
              d="M5 13l4 4L19 7"
            />
          </svg>
        </button>

        <!-- Содержимое заметки -->
        <div class="flex flex-col items-center">
          <!-- Заголовок -->
          <input
            v-if="note.isEditing"
            v-model="note.title"
            class="mt-8 text-xl font-bold text-white bg-transparent outline-none w-full text-center"
          />
          <h2
            v-else
            class="text-xl font-bold text-white text-center"
            :class="{ 'mt-8': note.isEditing }"
          >
            {{ note.title }}
          </h2>

          <!-- Содержание -->
          <textarea
            v-if="note.isEditing"
            v-model="note.content"
            class="mt-2 text-gray-300 bg-transparent outline-none w-full resize-none text-center"
          ></textarea>
          <p
            v-else
            class="mt-2 text-gray-300 text-center"
            :class="{ 'mt-8': note.isEditing }"
          >
            {{ note.content }}
          </p>
        </div>

        <div class="mt-4 text-sm text-gray-400 text-center">
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

    // Редактирование заметки
    const startEditing = (note: any) => {
      note.isEditing = true; // Добавляем флаг редактирования
    };

    const saveNote = async (note: any) => {
      try {
        await userStore.updateNote(note.id, note.title, note.content);
        note.isEditing = false; // Отключаем режим редактирования
      } catch (error) {
        console.error('Ошибка при сохранении заметки:', error);
        alert('Не удалось сохранить изменения. Попробуйте снова.');
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
      startEditing,
      saveNote,
    };
  },
});
</script>