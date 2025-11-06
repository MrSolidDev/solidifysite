<script lang="ts" setup>
import Card from 'primevue/card'
const cards = [
  {
    title: 'Misión',
    content: `
      <p><strong>Desarrollar soluciones tecnológicas</strong> confiables, personalizadas y humanas.</p>
      <ul class="list-disc ml-6 mt-2">
        <li>Acompañamos a nuestros clientes desde la idea inicial hasta el producto final.</li>
        <li>Combinamos ingeniería, diseño y propósito para generar impacto real.</li>
      </ul>
    `
  },
  {
    title: 'Visión',
    content: `
      <p><strong>Convertirnos en una marca reconocida</strong> por crear tecnología sólida, intuitiva y con significado.</p>
      <p>Aspiramos a ser un puente entre la <em>creatividad</em> y la <em>ingeniería</em>, donde las ideas se vuelven realidad.</p>
    `
  },
  {
    title: 'Valores',
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
    <div class="flex flex-col w-full justify-center items-center gap-5">
      <div class="flex w-full gap-4 justify-center">
            <Card
            v-for="(card, i) in cards"
            :key="i"
            class="w-full sm:w-[30%] bg-[#161E21] text-primary-400 shadow-[_0_4px_4px_rgba(0,0,0,0.5)] rounded-b-2xl p-4">
                <template #title>
                    <h2 class="font-bold mb-6 text-2xl">{{card.title}}</h2>
                    
                </template>
                <template #content>
                    <div class="m-0 leading-relaxed text-lg text-surface-300 space-y-2" v-html="card.content"></div>
                </template>
            </Card>
        </div>
        
    </div>
</template>
