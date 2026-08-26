<script setup lang="ts">
import { ref } from 'vue'
import { RouterLink, useRoute, type RouteLocationRaw } from 'vue-router'
import logo from '@/assets/logo.jpg'

const open = ref(false)
const route = useRoute()
const links: Array<{ label: string; description: string; to: RouteLocationRaw; active: () => boolean }> = [
  {
    label: 'Soluciones',
    description: 'Qué hacemos y cómo podemos ayudarte',
    to: { name: 'home', hash: '#soluciones' },
    active: () => route.name === 'home' && ['#soluciones', '#servicios'].includes(route.hash),
  },
  {
    label: 'Productos',
    description: 'Catálogo de productos Solidify',
    to: { name: 'projects' },
    active: () => ['projects', 'project-detail'].includes(String(route.name)),
  },
  {
    label: 'Nosotros',
    description: 'Conoce a Solidify',
    to: { name: 'home', hash: '#empresa' },
    active: () => route.name === 'home' && route.hash === '#empresa',
  },
]

function closeMenu() { open.value = false }
</script>

<template>
  <header class="fixed inset-x-0 top-0 z-50 border-b border-white/8 bg-[#091011]/85 backdrop-blur-xl">
    <nav class="section-wrap flex h-20 items-center justify-between" aria-label="Navegación principal">
      <RouterLink :to="{ name: 'home', hash: '#inicio' }" class="flex items-center gap-3" @click="closeMenu">
        <img :src="logo" alt="Solidify" class="h-10 w-10 rounded-xl object-cover" />
        <div>
          <span class="block text-lg font-semibold tracking-[.14em]">SOLIDIFY</span>
          <span class="block text-[10px] uppercase tracking-[.18em] text-white/45">Digital solutions</span>
        </div>
      </RouterLink>

      <div class="hidden items-center gap-7 lg:flex">
        <RouterLink
          v-for="link in links"
          :key="link.label"
          :to="link.to"
          class="relative py-2 text-sm transition after:absolute after:inset-x-0 after:-bottom-1 after:h-0.5 after:origin-left after:scale-x-0 after:bg-orange-300 after:transition-transform hover:text-white hover:after:scale-x-100"
          :class="link.active() ? 'text-white after:scale-x-100' : 'text-white/65'"
          :aria-current="link.active() ? 'page' : undefined"
        >
          {{ link.label }}
        </RouterLink>
        <RouterLink :to="{ name: 'home', hash: '#contacto' }" class="rounded-full bg-orange-400 px-5 py-2.5 text-sm font-semibold text-[#091011] transition hover:bg-orange-300">
          Cuéntanos tu proyecto
        </RouterLink>
      </div>

      <button class="grid h-11 w-11 place-items-center rounded-full border border-white/10 lg:hidden" :aria-label="open ? 'Cerrar menú' : 'Abrir menú'" :aria-expanded="open" aria-controls="mobile-navigation" @click="open = !open">
        <i :class="open ? 'pi pi-times' : 'pi pi-bars'"></i>
      </button>
    </nav>

    <div v-if="open" id="mobile-navigation" class="border-t border-white/8 bg-[#0d1516] px-4 py-5 lg:hidden">
      <div class="flex flex-col gap-1">
        <RouterLink v-for="link in links" :key="link.label" :to="link.to" class="rounded-xl px-4 py-3 hover:bg-white/5" :class="link.active() ? 'bg-white/5 text-white' : 'text-white/75'" :aria-current="link.active() ? 'page' : undefined" @click="closeMenu">
          <span class="block font-medium">{{ link.label }}</span>
          <span class="mt-1 block text-xs text-white/40">{{ link.description }}</span>
        </RouterLink>
        <RouterLink :to="{ name: 'home', hash: '#contacto' }" class="mt-3 rounded-xl bg-orange-400 px-4 py-3 text-center font-semibold text-[#091011]" @click="closeMenu">Cuéntanos tu proyecto</RouterLink>
      </div>
    </div>
  </header>
</template>
