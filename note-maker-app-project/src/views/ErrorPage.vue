<template>
  <div class="p-4 bg-gradient-to-br from-[#ff4d4d] to-[#ff1a1a] text-white min-h-screen flex flex-col items-center justify-center">
    <!-- Заголовок -->
    <h1 class="text-3xl font-bold mb-6">Ошибка получения данных</h1>

    <!-- Сообщение -->
    <p class="text-lg text-gray-300 text-center max-w-md">
      Не удалось получить данные о пользователе. Пожалуйста, убедитесь, что вы перешли по корректной ссылке.
    </p>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'ErrorPage',
});
</script>