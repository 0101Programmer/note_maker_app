<template>
  <router-view />
</template>

<script lang="ts">
import { defineComponent, onMounted, onUnmounted } from 'vue';
import { useRouter } from 'vue-router';
import { useUserStore } from '@/stores/userStore';

export default defineComponent({
  name: 'App',
  setup() {
    const router = useRouter();
    const userStore = useUserStore();

    // --- Функция для периодической проверки сессии ---
    const startSessionCheck = () => {
      const interval = setInterval(async () => {
        if (!userStore.sessionID) {
          clearInterval(interval); // Останавливаем интервал, если sessionID пустой
          return;
        }

        try {
          await userStore.checkSession(router);
        } catch (error) {
          console.error('Ошибка при проверке сессии:', error);
        }
      }, 30000); // Проверка каждые 30 секунд

      // Очищаем интервал при размонтировании компонента
      onUnmounted(() => {
        clearInterval(interval);
      });
    };

    // Запускаем проверку при загрузке приложения
    onMounted(() => {
      startSessionCheck();
    });

    return {};
  },
});
</script>

<style>
/* Глобальные стили */
</style>
