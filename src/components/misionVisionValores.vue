<script lang="ts" setup>
import Card from 'primevue/card'
import Tag from 'primevue/tag'
import { scrollToNext } from '@/utilities/scroll';
const cards = [
  {
    title: 'Misión',
    icon: 'pi pi-bullseye',
    pill: 'Entrega con propósito',
    animation: 'animate-enter fade-in-10 spin-in-45 slide-in-from-t-12 animate-duration-1000' ,
    content: `
      <p><strong>Convertir ideas en productos listos para producción</strong> que resuelvan un problema claro.</p>
      <ul class="list-disc ml-6 mt-2 space-y-1">
        <li>Definir objetivos de negocio y métricas antes de escribir código.</li>
        <li>Diseñar soluciones simples, medibles y mantenibles.</li>
      </ul>
    `
  },
  {
    title: 'Visión',
    icon: 'pi pi-sitemap',
    pill: 'Socio técnico',
    animation: 'animate-enter fade-in-10 zoom-in-50 slide-in-from-t-20 animate-duration-1000',
    content: `
      <p><strong>Ser el socio técnico al que acudes</strong> cuando necesitas velocidad, claridad y calidad en entregables.</p>
      <p>Puente entre <em>arquitectura</em> y <em>experiencia de usuario</em>: integraciones SAP/AWS, frontends usables y despliegues listos para operar.</p>
    `
  },
  {
    title: 'Principios de trabajo',
    icon: 'pi pi-star',
    pill: 'Cómo ejecuto',
    animation: 'animate-enter fade-in-10 spin-in-45 slide-in-from-t-16 animate-duration-1000' ,
    content: `
      <ul class="list-disc ml-6 space-y-1">
        <li><strong>Claridad primero:</strong> documentación breve, decisiones justificadas.</li>
        <li><strong>Entrega incremental:</strong> demos frecuentes para validar rumbo.</li>
        <li><strong>Calidad visible:</strong> pruebas básicas y métricas de performance.</li>
        <li><strong>Empatía técnica:</strong> explico lo complejo en lenguaje de negocio.</li>
        <li><strong>Ownership:</strong> me hago cargo de principio a fin.</li>
      </ul>
    `
  }
]



</script>
<template>
    <div class="flex flex-col w-[90%] justify-center items-center gap-6 min-h-screen">
      <div class="space-y-3 text-center" v-animateonscroll="{ enterClass: 'animate-enter fade-in-10 slide-in-from-b-20 animate-duration-1000' }">
        <h2 class="text-3xl text-center sm:text-4xl font-bold text-primary-400 tracking-wide">
          Misión · Visión · Valores
        </h2>
        <div class="h-[3px] w-20 bg-gradient-to-r from-purple-500 via-orange-400 to-pink-400 rounded-full mx-auto"></div>
        <p class="text-surface-400 text-center max-w-xl mx-auto text-lg leading-relaxed font-light">
          Mis lineamientos para mantener claridad, entrega y calidad en cada proyecto.
        </p>
      </div>
      <div class="flex flex-col md:flex-row w-full gap-4 justify-center">
            <Card
            v-for="(card, i) in cards"
            :key="i"
            v-animateonscroll="{ enterClass: card.animation}"
            class="group bg-[#161E21] border border-white/10 rounded-2xl 
               p-8 text-left text-surface-200 shadow-[0_4px_12px_rgba(0,0,0,0.4)] transition-all duration-300 
               hover:shadow-[0_8px_20px_rgba(0,0,0,0.6)] hover:-translate-y-1">
                <template #title>
                    <div class="flex items-center gap-3 mb-4">
                      <span :class="card.icon" class="text-orange-400 text-xl"></span>
                      <h2 class="font-bold text-2xl">{{card.title}}</h2>
                      <Tag v-if="card.pill" :value="card.pill" severity="warning" class="text-xs bg-white/10 text-orange-200 border border-orange-400/40" />
                    </div>
                </template>
                <template #content>
                    <div class="m-0 leading-relaxed text-lg text-surface-300 space-y-2" v-html="card.content"></div>
                </template>
            </Card>
        </div>
        <div
          class="mt-10 animate-bounce text-orange-400 text-6xl cursor-pointer drop-shadow-[0_0_10px_rgba(255,138,0,0.5)] hover:drop-shadow-[0_0_15px_rgba(255,138,0,0.8)] transition-all"
          @click="scrollToNext"
        >
          <i class="pi pi-angle-down"></i>
        </div>
    </div>
</template>
