<script setup lang="ts">
import PublicLayout from '@/layouts/PublicLayout.vue'
import { useApiResource } from '@/composables/useApiResource'
import { listProjects } from '@/services/projects'

const { data: projects, loading, error, reload } = useApiResource(listProjects)
</script>

<template>
  <PublicLayout>
    <section class="section-space pt-36">
      <div class="section-wrap">
        <p class="eyebrow mb-4">Productos Solidify</p>
        <h1 class="display-title max-w-4xl">Tecnología construida para operar en el mundo real.</h1>
        <p class="muted mt-6 max-w-2xl text-lg leading-8">Explora nuestras soluciones, sus capacidades y los escenarios donde generan valor.</p>

        <div v-if="loading" class="mt-14 grid gap-6 md:grid-cols-2" aria-label="Cargando productos">
          <div v-for="item in 2" :key="item" class="glass-card h-72 animate-pulse rounded-3xl"></div>
        </div>
        <div v-else-if="error" class="glass-card mt-14 rounded-3xl p-8 text-center"><p class="text-white/75">{{ error }}</p><button class="mt-5 text-sm font-semibold text-orange-300" @click="reload">Intentar de nuevo</button></div>
        <div v-else-if="projects?.length" class="mt-14 grid gap-6 md:grid-cols-2">
          <RouterLink
            v-for="project in projects"
            :key="project.id"
            :to="{ name: 'project-detail', params: { slug: project.slug } }"
            class="glass-card group rounded-3xl p-7 transition hover:-translate-y-1 hover:border-orange-300/40 sm:p-9"
          >
            <div class="flex items-start justify-between gap-5">
              <i class="pi pi-box text-3xl text-orange-300"></i>
              <span v-if="project.status" class="rounded-full border border-white/10 px-3 py-1 text-xs text-white/55">{{ project.status }}</span>
            </div>
            <h2 class="mt-10 text-3xl font-semibold">{{ project.name }}</h2>
            <p class="muted mt-4 leading-7">{{ project.short_description }}</p>
            <span v-if="project.case_studies.length" class="mt-6 inline-flex items-center gap-2 rounded-full border border-emerald-300/20 bg-emerald-300/8 px-3 py-1.5 text-xs font-medium text-emerald-200"><i class="pi pi-chart-line"></i>{{ project.case_studies.length }} {{ project.case_studies.length === 1 ? 'caso de éxito' : 'casos de éxito' }}</span>
            <span class="mt-8 inline-flex items-center gap-2 text-sm font-semibold text-orange-300">
              Conocer el producto <i class="pi pi-arrow-right transition group-hover:translate-x-1"></i>
            </span>
          </RouterLink>
        </div>
        <p v-else class="muted mt-14">Próximamente publicaremos nuevos productos.</p>
      </div>
    </section>
  </PublicLayout>
</template>
