<script setup lang="ts">
import { watch } from 'vue'
import { useRoute } from 'vue-router'
import PublicLayout from '@/layouts/PublicLayout.vue'
import { useApiResource } from '@/composables/useApiResource'
import { getProject } from '@/services/projects'

const route = useRoute()
const { data: project, loading, error, reload } = useApiResource((signal) => getProject(String(route.params.slug), signal))
watch(() => route.params.slug, reload)
</script>

<template>
  <PublicLayout>
    <section v-if="loading" class="section-space pt-36"><div class="section-wrap"><div class="glass-card h-96 animate-pulse rounded-3xl"></div></div></section>
    <section v-else-if="project" class="section-space pt-36">
      <div class="section-wrap">
        <RouterLink :to="{ name: 'projects' }" class="text-sm text-white/55 hover:text-orange-300"><i class="pi pi-arrow-left mr-2"></i>Todos los productos</RouterLink>
        <div class="mt-10 grid gap-12 lg:grid-cols-[1.1fr_.9fr] lg:items-start">
          <div>
            <p class="eyebrow">Proyecto Solidify</p>
            <h1 class="display-title mt-5">{{ project.name }}</h1>
            <p v-if="project.tagline" class="mt-6 text-xl leading-9 text-white/75">{{ project.tagline }}</p>
            <p class="muted mt-6 leading-8">{{ project.full_description }}</p>
          </div>
          <aside class="glass-card rounded-3xl p-7 sm:p-9">
            <p class="text-sm font-semibold uppercase tracking-widest text-orange-300">Descripción</p>
            <p class="mt-5 leading-8 text-white/80">{{ project.short_description }}</p>
            <div class="mt-7 border-t border-white/8 pt-7">
              <span v-if="project.status" class="rounded-full border border-white/10 px-3 py-1.5 text-xs text-white/60">{{ project.status }}</span>
              <div class="mt-5 flex gap-4 text-sm text-orange-300"><a v-if="project.project_url" :href="project.project_url" target="_blank" rel="noopener noreferrer">Visitar proyecto</a><a v-if="project.repository_url" :href="project.repository_url" target="_blank" rel="noopener noreferrer">Repositorio</a></div>
            </div>
          </aside>
        </div>

        <div v-if="project.technologies.length || project.media.length" class="mt-16 grid gap-6 lg:grid-cols-2">
          <article v-if="project.technologies.length" class="glass-card rounded-3xl p-7"><h2 class="text-xl font-semibold">Tecnologías</h2><div class="mt-5 flex flex-wrap gap-2"><span v-for="technology in project.technologies" :key="technology.id" class="rounded-lg bg-white/5 px-3 py-2 text-xs text-white/60">{{ technology.name }}</span></div></article>
          <article v-if="project.media.length" class="glass-card rounded-3xl p-7"><h2 class="text-xl font-semibold">Galería</h2><div class="mt-5 grid grid-cols-2 gap-3"><img v-for="media in project.media.filter((item) => item.type === 'image')" :key="media.id" :src="media.url" :alt="media.alt" class="rounded-xl object-cover" /></div></article>
        </div>
        <section v-if="project.case_studies.length" class="mt-12"><p class="eyebrow text-emerald-300">Casos de éxito</p><h2 class="mt-3 text-3xl font-semibold">Resultados asociados a este producto</h2><div class="mt-6 grid gap-4"><RouterLink v-for="study in project.case_studies" :key="study.id" :to="{ name: 'case-study-detail', params: { slug: study.slug } }" class="grid gap-5 rounded-3xl border border-emerald-300/20 bg-emerald-300/[.06] p-7 transition hover:border-emerald-300/40 sm:p-9 lg:grid-cols-[1fr_auto] lg:items-center"><div><h3 class="text-2xl font-semibold">{{ study.title }}</h3><p class="muted mt-3 leading-7">{{ study.challenge }}</p></div><span class="inline-flex items-center gap-2 font-semibold text-emerald-200">Ver resultados <i class="pi pi-arrow-right"></i></span></RouterLink></div></section>
      </div>
    </section>
    <section v-else class="section-space pt-36 text-center"><div class="section-wrap"><h1 class="section-title">Producto no disponible</h1><p class="muted mt-5">{{ error }}</p><button class="mt-5 text-sm font-semibold text-orange-300" @click="reload">Intentar de nuevo</button><br><RouterLink :to="{ name: 'projects' }" class="mt-7 inline-block text-white/60">Volver a productos</RouterLink></div></section>
  </PublicLayout>
</template>
