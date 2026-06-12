<script setup lang="ts">
import bryan from '@/assets/bryanr.jpeg'
</script>

<template>
  <section class="section-space">
    <div class="section-wrap grid items-center gap-12 lg:grid-cols-[.8fr_1.2fr]">
      <div class="relative mx-auto w-full max-w-md">
        <div class="absolute -inset-4 translate-x-5 translate-y-5 rounded-[2rem] border border-primary-300/20"></div>
        <img :src="bryan" alt="Bryan Rodríguez, fundador de Solidify" class="relative aspect-[4/5] w-full rounded-[2rem] object-cover object-top grayscale-[20%]" />
        <div class="glass-card absolute right-4 bottom-4 rounded-2xl px-5 py-4">
          <b class="block">Bryan Rodríguez</b>
          <span class="text-xs text-white/50">Founder · Full Stack Developer</span>
        </div>
      </div>

      <div>
        <p class="eyebrow mb-4">Quién está detrás</p>
        <h2 class="section-title">Una empresa con criterio técnico y cercanía humana.</h2>
        <div class="mt-7 space-y-5 text-base leading-8 text-white/65">
          <p>Solidify nace de la experiencia construyendo soluciones para entornos donde la tecnología debe convivir con procesos, equipos y objetivos reales de negocio.</p>
          <p>La dirección técnica está a cargo de Bryan Rodríguez, desarrollador Full Stack con experiencia en software empresarial, ecosistemas SAP y AWS, retail interactivo, preventa y gestión de proyectos.</p>
          <p>Trabajamos con una red flexible de especialistas según el alcance. Esto permite formar el equipo correcto sin agregar estructura innecesaria al proyecto.</p>
        </div>
        <div class="mt-8 grid gap-4 sm:grid-cols-3">
          <div class="border-l border-orange-300/60 pl-4"><b class="block text-lg">Negocio</b><span class="text-xs text-white/45">Entender antes de construir</span></div>
          <div class="border-l border-primary-300/60 pl-4"><b class="block text-lg">Ingeniería</b><span class="text-xs text-white/45">Bases mantenibles</span></div>
          <div class="border-l border-emerald-300/60 pl-4"><b class="block text-lg">Experiencia</b><span class="text-xs text-white/45">Tecnología fácil de usar</span></div>
        </div>
      </div>
    </div>
  </section>
</template>
