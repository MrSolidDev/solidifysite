<script setup lang="ts">
import Card from 'primevue/card';
import Tag from 'primevue/tag';
import Button from 'primevue/button';
import { scrollToNext } from '@/utilities/scroll';

type Project = {
  title: string;
  year: string;
  role: string;
  outcome: string;
  summary: string;
  stack: string[];
  linkDemo?: string;
  linkRepo?: string;
};

const proyectos: Project[] = [
  {
    title: 'Panel financiero SAP + AWS',
    year: '2025',
    role: 'Full Stack · Arquitectura',
    outcome: 'Consolida KPIs en vivo y reduce 70% el tiempo de conciliación.',
    summary:
      'Dashboard web sobre OData y Lambda Functions para finanzas. Incluye autenticación, cacheo y reporting descargable.',
    stack: ['Vue 3', 'TypeScript', 'PrimeVue', 'AWS Lambda', 'SAP OData', 'S3'],
    linkDemo: 'https://github.com/MrSolidDev',
  },
  {
    title: 'Experiencia retail interactiva',
    year: '2023',
    role: 'Full Stack · Integraciones',
    outcome: 'Aumenta 32% la interacción en tienda con contenido reactivo a sensores.',
    summary:
      'QuickplayX + sensores PIR y control de iluminación. Backend sincroniza playlists y métricas en tiempo real.',
    stack: ['Node.js', 'Vue', 'Tailwind', 'Raspberry Pi', 'Nexmosphere'],
  },
  {
    title: 'Portal de preventa y demos',
    year: '2024',
    role: 'PM · Frontend',
    outcome: 'Estandariza propuestas y acelera demos en preventa B2B.',
    summary:
      'Librería de componentes reutilizables, flujos guiados y secciones editables para presentar soluciones a clientes.',
    stack: ['Vue 3', 'TypeScript', 'Pinia', 'PrimeVue', 'Vercel'],
    linkRepo: 'https://github.com/MrSolidDev',
  },
];
</script>

<template>
  <section
    id="proyectos"
    class="flex flex-col w-full items-center gap-10 min-h-screen scroll-mt-24"
    v-animateonscroll="{ enterClass: 'animate-enter fade-in-10 animate-duration-1000' }"
  >
    <div class="text-center space-y-3">
      <h2 class="text-3xl sm:text-4xl font-bold text-primary-400 tracking-wide">
        Proyectos destacados
      </h2>
      <div class="h-[3px] w-24 bg-gradient-to-r from-purple-500 via-orange-400 to-pink-400 rounded-full mx-auto"></div>
      <p class="text-surface-400 max-w-3xl text-lg leading-relaxed font-light px-4">
        Casos reales con impacto medible. Problema → solución → resultado.
      </p>
    </div>

    <div class="grid gap-6 w-[90%] md:grid-cols-2 xl:grid-cols-3">
      <Card
        v-for="(p, i) in proyectos"
        :key="i"
        v-animateonscroll="{ enterClass: 'animate-enter fade-in-10 slide-in-from-b-12 animate-duration-800' }"
        class="bg-[#161E21] border border-white/10 rounded-2xl text-surface-200 shadow-[0_6px_18px_rgba(0,0,0,0.45)] hover:-translate-y-1 hover:shadow-[0_12px_28px_rgba(0,0,0,0.55)] transition-all duration-300"
      >
        <template #title>
          <div class="flex items-center justify-between gap-3">
            <h3 class="text-xl font-semibold">{{ p.title }}</h3>
            <Tag :value="p.year" severity="info" class="text-xs" />
          </div>
        </template>

        <template #subtitle>
          <span class="text-sm text-primary-300">{{ p.role }}</span>
        </template>

        <template #content>
          <div class="space-y-4 text-base leading-relaxed">
            <p class="text-surface-300">{{ p.summary }}</p>
            <div class="border-l-4 border-orange-400/70 pl-4 bg-white/5 rounded-sm py-2">
              <p class="text-surface-100 font-semibold">Resultado</p>
              <p class="text-surface-300 text-sm">{{ p.outcome }}</p>
            </div>
            <div class="flex flex-wrap gap-2">
              <Tag v-for="(tech, idx) in p.stack" :key="idx" severity="secondary" class="!bg-white/5 text-xs">
                {{ tech }}
              </Tag>
            </div>
          </div>
        </template>

        <template #footer>
          <div class="flex gap-2 flex-wrap">
            <Button
              v-if="p.linkDemo"
              :href="p.linkDemo"
              as="a"
              target="_blank"
              label="Ver demo"
              icon="pi pi-external-link"
              class="p-button-sm p-button-rounded p-button-outlined text-primary-200 border-primary-300/60"
            />
            <Button
              v-if="p.linkRepo"
              :href="p.linkRepo"
              as="a"
              target="_blank"
              label="Código"
              icon="pi pi-github"
              class="p-button-sm p-button-rounded p-button-text text-surface-200"
            />
          </div>
        </template>
      </Card>
    </div>

    <div
      class="mt-6 animate-bounce text-orange-400 text-6xl cursor-pointer drop-shadow-[0_0_10px_rgba(255,138,0,0.5)] hover:drop-shadow-[0_0_15px_rgba(255,138,0,0.8)] transition-all"
      @click="scrollToNext"
    >
      <i class="pi pi-angle-down"></i>
    </div>
  </section>
</template>

<style scoped>
</style>
