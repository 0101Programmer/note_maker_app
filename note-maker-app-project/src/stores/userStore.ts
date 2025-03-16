import { defineStore } from 'pinia';
import axios from 'axios';

export const useUserStore = defineStore('user', {
  state: () => ({
    tgUsername: '', // Имя пользователя из Telegram
    sessionID: '', // ID сессии
    notes: [] as any[], // Список заметок пользователя
    isLoading: false, // Флаг загрузки
  }),
  actions: {
    setTgUsername(username: string) {
      this.tgUsername = username;
    },
    setSessionID(session_id: string) {
      this.sessionID = session_id;
    },
    async checkSession(router: any) {
      try {
        const fastApiHost = import.meta.env.VITE_FASTAPI_HOST;
        const fastApiPort = import.meta.env.VITE_FASTAPI_PORT;

        const response = await axios.post(
          `http://${fastApiHost}:${fastApiPort}/set_get_session/check_session`,
          {
            session_id: this.sessionID,
            tg_username: this.tgUsername,
          },
          {
            headers: { 'Content-Type': 'application/json' },
          }
        );

        if (!response.data.valid) {
          await router.push({ name: 'access-denied' });
        }
      } catch (error) {
        console.error('Ошибка при проверке сессии:', error);
        await router.push({ name: 'iternal-error' });
      }
    },
    async fetchNotes(): Promise<void> {
      if (this.isLoading) return;

      this.isLoading = true;
      try {
        const fastApiHost = import.meta.env.VITE_FASTAPI_HOST;
        const fastApiPort = import.meta.env.VITE_FASTAPI_PORT;

        const response = await axios.post(
          `http://${fastApiHost}:${fastApiPort}/notes/get_all_notes/`,
          { username: this.tgUsername },
          { headers: { 'Content-Type': 'application/json' } }
        );

        this.notes = response.data;
      } catch (error) {
        console.error('Ошибка при получении заметок:', error);
        alert('Не удалось загрузить заметки. Попробуйте снова.');
      } finally {
        this.isLoading = false;
      }
    },
    async deleteNote(noteId: number): Promise<void> {
      try {
        const fastApiHost = import.meta.env.VITE_FASTAPI_HOST;
        const fastApiPort = import.meta.env.VITE_FASTAPI_PORT;

        await axios.post(
          `http://${fastApiHost}:${fastApiPort}/notes/delete_note/`,
          { note_id: noteId }, // Отправляем данные в формате JSON
          { headers: { 'Content-Type': 'application/json' } }
        );

        // Удаляем заметку из состояния
        this.notes = this.notes.filter((note) => note.id !== noteId);
      } catch (error) {
        console.error('Ошибка при удалении заметки:', error);
        alert('Не удалось удалить заметку. Попробуйте снова.');
      }
    },
  },
});