<script setup lang="ts">
import { ref } from 'vue'
import logo from '@/assets/logo.jpg'

const open = ref(false)
const links = [
  { label: 'Productos', href: '#productos' },
  { label: 'Servicios', href: '#servicios' },
  { label: 'Casos de éxito', href: '#casos' },
  { label: 'Proceso', href: '#proceso' },
  { label: 'Empresa', href: '#empresa' },
]

function closeMenu() { open.value = false }
</script>

<template>
  <header class="fixed inset-x-0 top-0 z-50 border-b border-white/8 bg-[#091011]/85 backdrop-blur-xl">
    <nav class="section-wrap flex h-20 items-center justify-between" aria-label="Navegación principal">
      <a href="#inicio" class="flex items-center gap-3" @click="closeMenu">
        <img :src="logo" alt="Solidify" class="h-10 w-10 rounded-xl object-cover" />
        <div>
          <span class="block text-lg font-semibold tracking-[.14em]">SOLIDIFY</span>
          <span class="block text-[10px] uppercase tracking-[.18em] text-white/45">Digital solutions</span>
        </div>
      </a>

      <div class="hidden items-center gap-7 lg:flex">
        <a v-for="link in links" :key="link.href" :href="link.href" class="text-sm text-white/65 transition hover:text-white">
          {{ link.label }}
        </a>
        <a href="#contacto" class="rounded-full bg-orange-400 px-5 py-2.5 text-sm font-semibold text-[#091011] transition hover:bg-orange-300">
          Hablemos
        </a>
      </div>

      <button class="grid h-11 w-11 place-items-center rounded-full border border-white/10 lg:hidden" aria-label="Abrir menú" @click="open = !open">
        <i :class="open ? 'pi pi-times' : 'pi pi-bars'"></i>
      </button>
    </nav>

    <div v-if="open" class="border-t border-white/8 bg-[#0d1516] px-4 py-5 lg:hidden">
      <div class="flex flex-col gap-1">
        <a v-for="link in links" :key="link.href" :href="link.href" class="rounded-xl px-4 py-3 text-white/75 hover:bg-white/5" @click="closeMenu">
          {{ link.label }}
        </a>
        <a href="#contacto" class="mt-2 rounded-xl bg-orange-400 px-4 py-3 text-center font-semibold text-[#091011]" @click="closeMenu">Hablemos</a>
      </div>
    </div>
  </header>
</template>
