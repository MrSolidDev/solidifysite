<script setup lang="ts">
import { watch } from 'vue'
import { useRoute } from 'vue-router'
import PublicLayout from '@/layouts/PublicLayout.vue'
import { useApiResource } from '@/composables/useApiResource'
import { getCaseStudy } from '@/services/caseStudies'

const route = useRoute()
const { data: study, loading, error, reload } = useApiResource((signal) => getCaseStudy(String(route.params.slug), signal))
watch(() => route.params.slug, reload)
</script>

<template>
  <PublicLayout>
    <section v-if="loading" class="section-space pt-36"><div class="section-wrap"><div class="glass-card h-96 animate-pulse rounded-3xl"></div></div></section>
    <section v-else-if="study" class="section-space pt-36">
      <div class="section-wrap max-w-5xl">
        <RouterLink :to="{ name: 'case-studies' }" class="text-sm text-white/55 hover:text-orange-300"><i class="pi pi-arrow-left mr-2"></i>Todos los casos</RouterLink>
        <p class="eyebrow mt-10">{{ study.project.name }}</p>
        <h1 class="display-title mt-5">{{ study.title }}</h1>
        <div class="mt-14 grid gap-6 md:grid-cols-3">
          <article class="glass-card rounded-3xl p-7"><span class="eyebrow">01 · Reto</span><p class="muted mt-5 leading-7">{{ study.challenge }}</p></article>
          <article class="glass-card rounded-3xl p-7"><span class="eyebrow">02 · Solución</span><p class="muted mt-5 leading-7">{{ study.solution }}</p></article>
          <article class="rounded-3xl border border-orange-300/25 bg-orange-300/8 p-7"><span class="eyebrow">03 · Resultado</span><p class="mt-5 leading-7 text-white/85">{{ study.results }}</p></article>
        </div>
        <article v-if="study.architecture" class="glass-card mt-6 rounded-3xl p-7"><span class="eyebrow">Arquitectura</span><p class="muted mt-5 leading-7">{{ study.architecture }}</p></article>
        <div class="mt-10 flex flex-wrap gap-2"><span v-for="technology in study.project.technologies" :key="technology.id" class="rounded-lg bg-white/5 px-3 py-2 text-xs text-white/60">{{ technology.name }}</span></div>
      </div>
    </section>
    <section v-else class="section-space pt-36 text-center"><div class="section-wrap"><h1 class="section-title">Caso no disponible</h1><p class="muted mt-5">{{ error }}</p><button class="mt-5 text-sm font-semibold text-orange-300" @click="reload">Intentar de nuevo</button><br><RouterLink :to="{ name: 'case-studies' }" class="mt-7 inline-block text-white/60">Volver a casos de éxito</RouterLink></div></section>
  </PublicLayout>
</template>
