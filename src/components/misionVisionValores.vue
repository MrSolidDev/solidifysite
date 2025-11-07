<script lang="ts" setup>
import Card from 'primevue/card'
import { scrollToNext } from '@/utilities/scroll';
const cards = [
  {
    title: 'Misión',
    animation: 'animate-enter fade-in-10 spin-in-45 slide-in-from-t-12 animate-duration-1000' ,
    content: `
      <p><strong>Desarrollar soluciones tecnológicas</strong> confiables, personalizadas y humanas.</p>
      <ul class="list-disc ml-6 mt-2 space-y-1">
        <li>Acompañamos a nuestros clientes desde la idea inicial hasta el producto final.</li>
        <li>Combinamos ingeniería, diseño y propósito para generar impacto real.</li>
      </ul>
    `
  },
  {
    title: 'Visión',
    animation: 'animate-enter fade-in-10 zoom-in-50 slide-in-from-t-20 animate-duration-1000',
    content: `
      <p><strong>Convertirnos en una marca reconocida</strong> por crear tecnología sólida, intuitiva y con significado.</p>
      <p>Aspiramos a ser un puente entre la <em>creatividad</em> y la <em>ingeniería</em>, donde las ideas se vuelven realidad.</p>
    `
  },
  {
    title: 'Valores',
    animation: 'animate-enter fade-in-10 spin-in-45 slide-in-from-t-16 animate-duration-1000' ,
    content: `
      <ul class="list-disc ml-6 space-y-1">
        <li><strong>Claridad:</strong> Comunicación honesta y procesos transparentes.</li>
        <li><strong>Compromiso:</strong> Cada proyecto nos importa como si fuera nuestro.</li>
        <li><strong>Creatividad:</strong> La tecnología también puede inspirar.</li>
        <li><strong>Evolución:</strong> Siempre aprendemos, mejoramos y buscamos innovar.</li>
        <li><strong>Humanidad:</strong> Detrás de cada línea de código hay una historia y una persona.</li>
      </ul>
    `
  }
]



</script>
<template>
    <div class="flex flex-col w-[90%] justify-center items-center gap-5 min-h-screen">
      <div class="space-y-3" v-animateonscroll="{ enterClass: 'animate-enter fade-in-10 slide-in-from-b-20 animate-duration-1000' }">
        <h2 class="text-3xl text-center sm:text-4xl font-bold text-primary-400 tracking-wide">
          Misión · Visión · Valores
        </h2>
        <div class="h-[3px] w-20 bg-gradient-to-r from-purple-500 via-orange-400 to-pink-400 rounded-full mx-auto"></div>
        <p class="text-surface-400 text-center max-w-xl mx-auto text-lg leading-relaxed font-light">
          Los pilares que guían cómo pensamos, diseñamos y construimos tecnología con propósito.
        </p>
      </div>
      <div class="flex w-full gap-4 justify-center">
            <Card
            v-for="(card, i) in cards"
            :key="i"
            v-animateonscroll="{ enterClass: card.animation}"
            class="group bg-[#161E21] border border-white/10 rounded-2xl 
               p-8 text-left text-surface-200 shadow-[0_4px_12px_rgba(0,0,0,0.4)] transition-all duration-300 
               hover:shadow-[0_8px_20px_rgba(0,0,0,0.6)] hover:-translate-y-1">
                <template #title>
                    <h2 class="font-bold mb-6 text-2xl">{{card.title}}</h2>
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
