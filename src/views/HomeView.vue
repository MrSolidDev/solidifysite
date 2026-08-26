<script setup lang="ts">
import PublicLayout from '@/layouts/PublicLayout.vue'
import Presentacion from '@/components/Presentacion.vue'
import Servicios from '@/components/Servicios.vue'
import AboutMe from '@/components/AboutMe.vue'
import MisionVisionValores from '@/components/misionVisionValores.vue'
</script>

<template>
  <PublicLayout>
    <Presentacion id="inicio" />
    <Servicios id="soluciones" />
    <MisionVisionValores id="proceso" />
    <AboutMe id="empresa" />
  </PublicLayout>
</template>
