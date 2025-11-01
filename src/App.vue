<script setup lang="ts">
  import Header from '@/components/Header.vue';
  import Presentacion from './components/Presentacion.vue';
</script>

<template>
  <div class="w-full flex flex-col gap-7">
    <Header></Header>
    <Presentacion></Presentacion>
  </div>

</template>

<style>
  @import "tailwindcss";
  @import "tailwindcss-primeui";

    /* Carga los pesos que uses */
  @import "@fontsource/poppins/400.css";
  @import "@fontsource/poppins/500.css";
  @import "@fontsource/poppins/600.css";

  /* Aplica la fuente globalmente (PrimeVue la hereda) */
  :root, html, body, #app {
    font-family: "Poppins", ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
  }

  
</style>
