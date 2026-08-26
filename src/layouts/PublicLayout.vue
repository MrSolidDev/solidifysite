<script setup lang="ts">
import Header from '@/components/Header.vue'
import Contacto from '@/components/Contacto.vue'
</script>

<template>
  <div class="site-shell">
    <Header />
    <main><slot /></main>
    <Contacto id="contacto" />
  </div>
</template>
