<script setup lang="ts">
  import Header from '@/components/Header.vue';
  import Presentacion from './components/Presentacion.vue';
</script>

<template>
  <div class="w-full flex flex-col gap-10">
    <Header></Header>
    <Presentacion></Presentacion>
  </div>

</template>

<style>
  @import "tailwindcss";
  @import "tailwindcss-primeui";
  
</style>
