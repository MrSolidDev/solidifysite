<script setup lang="ts">
import { caseStudies, services } from '@/data/siteContent'

function serviceName(id: string) {
  return services.find((service) => service.id === id)?.title ?? id
}
</script>

<template>
  <section class="section-space">
    <div class="section-wrap">
      <div class="max-w-3xl">
        <p class="eyebrow mb-4">Casos de éxito</p>
        <h2 class="section-title">La oferta cobra sentido cuando produce un resultado.</h2>
        <p class="muted mt-5 text-lg leading-8">Cada caso muestra cómo distintas capacidades de Solidify se combinan para resolver una necesidad concreta.</p>
      </div>

      <div class="mt-14 space-y-5">
        <article
          v-for="(project, index) in caseStudies"
          :id="`caso-${project.id}`"
          :key="project.id"
          class="glass-card grid overflow-hidden rounded-3xl lg:grid-cols-[.42fr_.58fr]"
        >
          <div class="relative flex min-h-64 flex-col justify-between overflow-hidden border-b border-white/8 p-7 lg:border-r lg:border-b-0 sm:p-9">
            <div class="absolute inset-0 opacity-60" :class="index % 2 ? 'bg-[radial-gradient(circle_at_20%_20%,rgba(255,138,0,.18),transparent_55%)]' : 'bg-[radial-gradient(circle_at_20%_20%,rgba(126,63,242,.24),transparent_55%)]'"></div>
            <div class="relative">
              <p class="eyebrow">{{ project.eyebrow }}</p>
              <h3 class="mt-5 text-2xl font-semibold leading-tight sm:text-3xl">{{ project.title }}</h3>
            </div>
            <div class="relative mt-10 flex flex-wrap gap-2">
              <a v-for="serviceId in project.serviceIds" :key="serviceId" :href="`#servicio-${serviceId}`" class="rounded-full border border-white/12 bg-black/10 px-3 py-1.5 text-xs text-white/65 hover:border-orange-300/50 hover:text-orange-200">
                {{ serviceName(serviceId) }}
              </a>
            </div>
          </div>

          <div class="grid gap-8 p-7 sm:p-9">
            <div class="grid gap-7 sm:grid-cols-3">
              <div><span class="text-xs font-semibold uppercase tracking-widest text-white/35">Reto</span><p class="muted mt-3 text-sm leading-6">{{ project.challenge }}</p></div>
              <div><span class="text-xs font-semibold uppercase tracking-widest text-white/35">Solución</span><p class="muted mt-3 text-sm leading-6">{{ project.solution }}</p></div>
              <div><span class="text-xs font-semibold uppercase tracking-widest text-orange-300">Resultado</span><p class="mt-3 text-sm leading-6 text-white/85">{{ project.result }}</p></div>
            </div>
            <div class="flex flex-wrap items-center gap-2 border-t border-white/8 pt-5">
              <span v-for="tech in project.stack" :key="tech" class="rounded-lg bg-white/5 px-3 py-1.5 text-xs text-white/50">{{ tech }}</span>
            </div>
          </div>
        </article>
      </div>
    </div>
  </section>
</template>
