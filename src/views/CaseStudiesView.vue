<script setup lang="ts">
import PublicLayout from '@/layouts/PublicLayout.vue'
import { useApiResource } from '@/composables/useApiResource'
import { listCaseStudies } from '@/services/caseStudies'

const { data: caseStudies, loading, error, reload } = useApiResource(listCaseStudies)
</script>

<template>
  <PublicLayout>
    <section class="section-space pt-36">
      <div class="section-wrap">
        <p class="eyebrow mb-4">Casos de éxito</p>
        <h1 class="display-title max-w-4xl">Problemas concretos, soluciones que se pueden medir.</h1>
        <p class="muted mt-6 max-w-2xl text-lg leading-8">Conoce cómo combinamos estrategia, diseño e ingeniería para resolver necesidades reales.</p>
        <div v-if="loading" class="mt-14 space-y-6"><div v-for="item in 3" :key="item" class="glass-card h-52 animate-pulse rounded-3xl"></div></div>
        <div v-else-if="error" class="glass-card mt-14 rounded-3xl p-8 text-center"><p class="text-white/75">{{ error }}</p><button class="mt-5 text-sm font-semibold text-orange-300" @click="reload">Intentar de nuevo</button></div>
        <div v-else-if="caseStudies?.length" class="mt-14 grid gap-6">
          <RouterLink
            v-for="study in caseStudies"
            :key="study.id"
            :to="{ name: 'case-study-detail', params: { slug: study.id } }"
            class="glass-card group grid gap-7 rounded-3xl p-7 transition hover:border-orange-300/40 sm:p-9 lg:grid-cols-[.4fr_.6fr]"
          >
            <div><p class="eyebrow">{{ study.project.name }}</p><h2 class="mt-4 text-2xl font-semibold leading-tight">{{ study.title }}</h2></div>
            <div><p class="muted leading-7">{{ study.challenge }}</p><span class="mt-6 inline-flex items-center gap-2 text-sm font-semibold text-orange-300">Leer caso <i class="pi pi-arrow-right transition group-hover:translate-x-1"></i></span></div>
          </RouterLink>
        </div>
        <p v-else class="muted mt-14">Próximamente publicaremos nuevos casos de éxito.</p>
      </div>
    </section>
  </PublicLayout>
</template>
