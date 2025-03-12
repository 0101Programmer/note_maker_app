import { defineStore } from 'pinia';

export const useUserStore = defineStore('user', {
  state: () => ({
    tgUsername: '', // Имя пользователя из Telegram
    notes: [] as { title: string; description: string }[], // Массив заметок
  }),
  actions: {
    setTgUsername(username: string) {
      this.tgUsername = username;
    },
    addNote(note: { title: string; description: string }) {
      this.notes.push(note);
    },
  },
});