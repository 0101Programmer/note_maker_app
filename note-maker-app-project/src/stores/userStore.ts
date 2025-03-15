import { defineStore } from 'pinia';

export const useUserStore = defineStore('user', {
  state: () => ({
    tgUsername: '', // Имя пользователя из Telegram
    sessionID: '', // ID сессии
  }),
  actions: {
    setTgUsername(username: string) {
      this.tgUsername = username;
    },
    setSessionID(session_id: string){
      this.sessionID = session_id;
    },
  },
});