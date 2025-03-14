import { defineStore } from 'pinia';

export const useUserStore = defineStore('user', {
  state: () => ({
    tgUsername: '', // Имя пользователя из Telegram
    sessionID: '', // ID сессии
    notes: [] as { title: string; description: string }[], // Массив заметок
  }),
  actions: {
    setTgUsername(username: string) {
      this.tgUsername = username;
    },
    setSessionID(session_id: string){
      this.sessionID = session_id;
    },
    addNote(note: { title: string; description: string }) {
      this.notes.push(note);
    },
  },
});