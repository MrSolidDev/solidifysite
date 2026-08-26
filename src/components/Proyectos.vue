<script setup lang="ts">
import { useApiResource } from '@/composables/useApiResource'
import { listCaseStudies } from '@/services/caseStudies'

const { data: caseStudies, loading, error, reload } = useApiResource(listCaseStudies)
</script>

<template>
  <section class="section-space">
    <div class="section-wrap">
      <div class="max-w-3xl">
        <p class="eyebrow mb-4">Casos de éxito</p>
        <h2 class="section-title">La oferta cobra sentido cuando produce un resultado.</h2>
        <p class="muted mt-5 text-lg leading-8">Cada caso muestra cómo distintas capacidades de Solidify se combinan para resolver una necesidad concreta.</p>
      </div>

      <div v-if="loading" class="mt-14 space-y-5"><div v-for="item in 2" :key="item" class="glass-card h-72 animate-pulse rounded-3xl"></div></div>
      <div v-else-if="error" class="glass-card mt-14 rounded-3xl p-8 text-center"><p class="text-white/70">{{ error }}</p><button class="mt-5 text-sm font-semibold text-orange-300" @click="reload">Intentar de nuevo</button></div>
      <div v-else-if="caseStudies?.length" class="mt-14 space-y-5">
        <article
          v-for="(project, index) in caseStudies"
          :id="`caso-${project.id}`"
          :key="project.id"
          class="glass-card grid overflow-hidden rounded-3xl lg:grid-cols-[.42fr_.58fr]"
        >
          <div class="relative flex min-h-64 flex-col justify-between overflow-hidden border-b border-white/8 p-7 lg:border-r lg:border-b-0 sm:p-9">
            <div class="absolute inset-0 opacity-60" :class="index % 2 ? 'bg-[radial-gradient(circle_at_20%_20%,rgba(255,138,0,.18),transparent_55%)]' : 'bg-[radial-gradient(circle_at_20%_20%,rgba(126,63,242,.24),transparent_55%)]'"></div>
            <div class="relative">
              <p class="eyebrow">{{ project.project.name }}</p>
              <h3 class="mt-5 text-2xl font-semibold leading-tight sm:text-3xl">{{ project.title }}</h3>
            </div>
            <div class="relative mt-10 flex flex-wrap gap-2">
              <span v-for="technology in project.project.technologies" :key="technology.id" class="rounded-full border border-white/12 bg-black/10 px-3 py-1.5 text-xs text-white/65">
                {{ technology.name }}
              </span>
            </div>
          </div>

          <div class="grid gap-8 p-7 sm:p-9">
            <div class="grid gap-7 sm:grid-cols-3">
              <div><span class="text-xs font-semibold uppercase tracking-widest text-white/35">Reto</span><p class="muted mt-3 text-sm leading-6">{{ project.challenge }}</p></div>
              <div><span class="text-xs font-semibold uppercase tracking-widest text-white/35">Solución</span><p class="muted mt-3 text-sm leading-6">{{ project.solution }}</p></div>
              <div><span class="text-xs font-semibold uppercase tracking-widest text-orange-300">Resultado</span><p class="mt-3 text-sm leading-6 text-white/85">{{ project.results }}</p></div>
            </div>
            <div class="flex flex-wrap items-center gap-2 border-t border-white/8 pt-5">
              <RouterLink :to="{ name: 'case-study-detail', params: { slug: project.slug } }" class="ml-auto text-sm font-semibold text-orange-300 hover:text-orange-200">Ver caso <i class="pi pi-arrow-right ml-1"></i></RouterLink>
            </div>
          </div>
        </article>
      </div>
      <p v-else class="muted mt-14">Próximamente publicaremos nuevos casos de éxito.</p>
    </div>
  </section>
</template>
