<script setup lang="ts">
import { computed, ref, watch } from 'vue'
import { useRoute } from 'vue-router'
import PublicLayout from '@/layouts/PublicLayout.vue'
import { useApiResource } from '@/composables/useApiResource'
import { getProject } from '@/services/projects'

const route = useRoute()
const descriptionExpanded = ref(false)
const { data: project, loading, error, reload } = useApiResource((signal) => getProject(String(route.params.slug), signal))
const descriptionParagraphs = computed(() => {
  const text = project.value?.full_description?.trim()
  if (!text) return []
  const explicitParagraphs = text.split(/\n\s*\n/).map((item) => item.trim()).filter(Boolean)
  if (explicitParagraphs.length > 1) return explicitParagraphs
  const sentences = text.match(/[^.!?]+[.!?]+|[^.!?]+$/g)?.map((item) => item.trim()).filter(Boolean) ?? [text]
  return Array.from({ length: Math.ceil(sentences.length / 3) }, (_, index) => sentences.slice(index * 3, index * 3 + 3).join(' '))
})
const visibleDescription = computed(() => descriptionExpanded.value ? descriptionParagraphs.value : descriptionParagraphs.value.slice(0, 2))
watch(() => route.params.slug, () => { descriptionExpanded.value = false; reload() })
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
            <p v-if="project.tagline" class="mt-6 max-w-2xl text-xl leading-9 text-white/75">{{ project.tagline }}</p>
            <p v-if="project.short_description" class="muted mt-6 max-w-2xl text-base leading-8">{{ project.short_description }}</p>
          </div>
          <aside class="glass-card rounded-3xl p-7 sm:p-9">
            <p class="text-sm font-semibold uppercase tracking-widest text-orange-300">Información del producto</p>
            <dl class="mt-6 divide-y divide-white/8">
              <div v-if="project.status" class="flex items-center justify-between gap-5 py-4 first:pt-0"><dt class="text-sm text-white/45">Estado</dt><dd><span class="rounded-full border border-white/10 px-3 py-1.5 text-xs text-white/70">{{ project.status }}</span></dd></div>
              <div class="flex items-center justify-between gap-5 py-4"><dt class="text-sm text-white/45">Tecnologías</dt><dd class="text-sm text-white/75">{{ project.technologies.length || '—' }}</dd></div>
              <div class="flex items-center justify-between gap-5 py-4"><dt class="text-sm text-white/45">Casos documentados</dt><dd class="text-sm text-white/75">{{ project.case_studies.length || '—' }}</dd></div>
            </dl>
            <div v-if="project.project_url || project.repository_url" class="flex flex-wrap gap-3 border-t border-white/8 pt-6 text-sm"><a v-if="project.project_url" :href="project.project_url" target="_blank" rel="noopener noreferrer" class="rounded-full bg-orange-400 px-4 py-2 font-semibold text-[#091011]">Visitar proyecto <i class="pi pi-arrow-up-right ml-1 text-xs"></i></a><a v-if="project.repository_url" :href="project.repository_url" target="_blank" rel="noopener noreferrer" class="rounded-full border border-white/12 px-4 py-2 text-white/75">Repositorio <i class="pi pi-github ml-1"></i></a></div>
          </aside>
        </div>

        <section v-if="descriptionParagraphs.length" class="mt-16 border-y border-white/8 py-12 sm:py-14">
          <div class="grid gap-7 lg:grid-cols-[.35fr_.65fr]">
            <div><p class="eyebrow">Acerca del producto</p><h2 class="mt-3 text-2xl font-semibold sm:text-3xl">Qué es {{ project.name }}</h2></div>
            <div class="max-w-3xl">
              <div class="space-y-5 text-base leading-8 text-white/65"><p v-for="(paragraph, index) in visibleDescription" :key="index">{{ paragraph }}</p></div>
              <button v-if="descriptionParagraphs.length > 2" class="mt-6 inline-flex items-center gap-2 text-sm font-semibold text-orange-300 hover:text-orange-200" :aria-expanded="descriptionExpanded" @click="descriptionExpanded = !descriptionExpanded">{{ descriptionExpanded ? 'Mostrar menos' : 'Leer descripción completa' }}<i :class="descriptionExpanded ? 'pi pi-angle-up' : 'pi pi-angle-down'"></i></button>
            </div>
          </div>
        </section>

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
