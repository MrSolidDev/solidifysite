<script setup lang="ts">
import PublicLayout from '@/layouts/PublicLayout.vue'
</script>

<template>
  <PublicLayout>
    <section class="section-space pt-36 text-center">
      <div class="section-wrap"><p class="eyebrow">404</p><h1 class="section-title mt-5">Esta página no existe.</h1><RouterLink :to="{ name: 'home' }" class="mt-7 inline-block text-orange-300">Volver al inicio</RouterLink></div>
    </section>
  </PublicLayout>
</template>
