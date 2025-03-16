import { defineStore } from 'pinia';
import axios from 'axios';

export const useUserStore = defineStore('user', {
  state: () => ({
    tgUsername: '', // Имя пользователя из Telegram
    sessionID: '', // ID сессии
    notes: [] as any[], // Список заметок пользователя
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

        // Отправляем POST-запрос для проверки сессии
        const response = await axios.post(
          `http://${fastApiHost}:${fastApiPort}/set_get_session/check_session`,
          {
            session_id: this.sessionID,
            tg_username: this.tgUsername,
          },
          {
            headers: {
              'Content-Type': 'application/json',
            },
          }
        );

        // Проверяем результат
        if (!response.data.valid) {
          // Если сессия недействительна, перенаправляем на страницу ошибки
          await router.push({ name: 'access-denied' });
        }
      } catch (error) {
        console.error('Ошибка при проверке сессии:', error);
        await router.push({ name: 'iternal-error' });
      }
    },
    async fetchNotes() {
      try {
        const fastApiHost = import.meta.env.VITE_FASTAPI_HOST;
        const fastApiPort = import.meta.env.VITE_FASTAPI_PORT;

        // Отправляем POST-запрос для получения заметок
        const response = await axios.post(
          `http://${fastApiHost}:${fastApiPort}/notes/get_all_notes/`,
          { username: this.tgUsername },
          { headers: { 'Content-Type': 'application/json' } }
        );

        // Сохраняем заметки в состоянии
        this.notes = response.data;
      } catch (error) {
        console.error('Ошибка при получении заметок:', error);
        alert('Не удалось загрузить заметки. Попробуйте снова.');
      }
    },
  },
});