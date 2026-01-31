<script lang="ts" setup>
import { scrollToNext } from '@/utilities/scroll';

const badges = [
  'Full Stack · Vue 3 · TypeScript · Python',
  'SAP · AWS · OData',
  'Digital signage · Retail interactivo',
  'Project mgmt · Preventa',
];
</script>

<template>
  <div class="flex flex-col items-center text-center w-full min-h-screen gap-10 scroll-mt-20">
    <div
      class="flex flex-col w-[90%] justify-center items-center text-center py-12 px-6 gap-5
             bg-gradient-to-b from-[#161E21] to-[#0e1315]
             rounded-3xl shadow-[0_6px_18px_rgba(0,0,0,0.35)] border border-white/5"
      v-animateonscroll="{ enterClass: 'animate-enter fade-in-10 animate-duration-1000' }"
    >
      <p class="text-xs sm:text-sm uppercase tracking-[0.35em] text-orange-400 font-semibold">Portafolio · Solidify</p>
      <h1 class="text-3xl sm:text-4xl font-bold text-primary-100 tracking-wide">
        Transformo ideas en productos listos para operar
      </h1>

      <div class="h-[3px] w-24 bg-gradient-to-r from-purple-500 via-orange-400 to-pink-400 rounded-full"></div>

      <p class="text-surface-300 text-lg sm:text-xl max-w-[900px] leading-relaxed font-light">
        Soy <strong class="text-primary-300">Bryan Rodríguez</strong>, dev Full Stack. Diseño y ejecuto soluciones end‑to‑end
        con <strong class="text-orange-400">integraciones empresariales</strong> (SAP, AWS, OData) y
        <strong class="text-orange-400">experiencias interactivas</strong> para retail. Código listo para producción, métricas claras
        y entregas incrementales.
      </p>

      <div class="flex flex-wrap justify-center gap-2 text-sm text-primary-100">
        <span
          v-for="(badge, i) in badges"
          :key="i"
          class="px-3 py-1 rounded-full border border-white/10 bg-white/5 shadow-[0_2px_8px_rgba(0,0,0,0.25)]"
        >
          {{ badge }}
        </span>
      </div>

      <div class="flex flex-col sm:flex-row gap-3 mt-2">
        <a
          href="#proyectos"
          class="px-5 py-3 rounded-xl bg-gradient-to-r from-orange-400 to-pink-500 text-[#0e1315] font-semibold shadow hover:shadow-lg transition"
        >
          Ver proyectos
        </a>
        <a
          href="#contacto"
          class="px-5 py-3 rounded-xl border border-primary-300/70 text-primary-100 font-semibold hover:bg-white/5 transition"
        >
          Agenda una llamada
        </a>
      </div>
    </div>

    <div
      class="mt-6 animate-bounce text-orange-400 text-6xl cursor-pointer drop-shadow-[0_0_10px_rgba(255,138,0,0.5)] hover:drop-shadow-[0_0_15px_rgba(255,138,0,0.8)] transition-all"
      @click="scrollToNext"
    >
      <i class="pi pi-angle-down"></i>
    </div>
  </div>
</template>

