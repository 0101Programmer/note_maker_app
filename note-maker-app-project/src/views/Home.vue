<template>
  <div>
    <h1 class="text-2xl font-bold">Профиль пользователя: {{ tgUsername }}</h1>
    <p>Информация о пользователе.</p>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { useRoute } from 'vue-router'

export default defineComponent({
  setup() {
    const route = useRoute()
    const tgUsername = route.params.tg_username  // Получаем параметр из URL

    return {
      tgUsername,
    }
  },
})
</script>