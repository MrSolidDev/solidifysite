<script setup lang="ts">
  import Header from '@/components/Header.vue';
  import Presentacion from '@/components/Presentacion.vue';
  import misionVisionValores from '@/components/misionVisionValores.vue';
  import Servicios from '@/components/Servicios.vue';
  import AboutMe from '@/components/AboutMe.vue';
</script>

<template>
  <div class="w-full flex flex-col gap-7">
    <Header></Header>
    <AboutMe></AboutMe>
    <Presentacion></Presentacion>
    <Servicios></Servicios>
    <misionVisionValores></misionVisionValores>
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

  .rich ul { list-style: disc; margin-left: 1.5rem; }
  .rich li { margin: 0.25rem 0; }
  .rich strong { font-weight: 600; }
  .rich h3 { line-height: 1.2; }
  .rich h4 { margin-bottom: .25rem; }

  
</style>
