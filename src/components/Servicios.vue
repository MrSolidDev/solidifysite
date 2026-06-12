<script setup lang="ts">
import { products, services } from '@/data/siteContent'
</script>

<template>
  <section class="section-space border-y border-white/6 bg-white/[.025]">
    <div class="section-wrap">
      <div class="grid gap-8 lg:grid-cols-2 lg:items-end">
        <div>
          <p class="eyebrow mb-4">Soluciones</p>
          <h2 class="section-title">Productos listos para operar y servicios para construir lo que sigue.</h2>
        </div>
        <p class="muted max-w-xl text-lg leading-8 lg:justify-self-end">
          Nuestros productos resuelven necesidades concretas con una base reutilizable. Los servicios adaptan, integran y desarrollan tecnología alrededor de cada operación.
        </p>
      </div>

      <div id="productos" class="scroll-mt-28 pt-16">
        <div class="mb-7 flex flex-col gap-2 sm:flex-row sm:items-end sm:justify-between">
          <div>
            <p class="eyebrow mb-2">Productos</p>
            <h3 class="text-2xl font-semibold sm:text-3xl">Productos listos para utilizar y adaptar a cada experiencia</h3>
          </div>
          <span class="text-sm text-white/40">Catálogo en crecimiento</span>
        </div>

        <article v-for="product in products" :key="product.id" :id="`producto-${product.id}`" class="glass-card overflow-hidden rounded-3xl">
          <div class="grid lg:grid-cols-[.9fr_1.1fr]">
            <div class="relative overflow-hidden border-b border-white/8 p-7 lg:border-r lg:border-b-0 sm:p-10">
              <div class="absolute inset-0 bg-[radial-gradient(circle_at_20%_10%,rgba(255,138,0,.18),transparent_52%),radial-gradient(circle_at_90%_90%,rgba(126,63,242,.2),transparent_48%)]"></div>
              <div class="relative flex h-full flex-col">
                <div class="flex items-center justify-between gap-4">
                  <span class="inline-flex items-center gap-2 rounded-full border border-emerald-300/20 bg-emerald-300/8 px-3 py-1.5 text-xs font-medium text-emerald-200">
                    <span class="h-1.5 w-1.5 rounded-full bg-emerald-300"></span>{{ product.status }}
                  </span>
                  <span class="grid h-12 w-12 place-items-center rounded-2xl bg-white/8 text-xl text-orange-300"><i :class="product.icon"></i></span>
                </div>
                <h4 class="mt-10 text-3xl font-semibold leading-tight sm:text-4xl">{{ product.title }}</h4>
                <p class="mt-5 text-base leading-7 text-white/70">{{ product.shortDescription }}</p>
                <div class="mt-8 flex flex-wrap gap-2">
                  <span v-for="audience in product.audiences" :key="audience" class="rounded-full border border-white/10 px-3 py-1.5 text-xs text-white/50">{{ audience }}</span>
                </div>
                <a href="#contacto" class="mt-10 inline-flex w-fit items-center gap-3 rounded-full bg-orange-400 px-6 py-3.5 font-semibold text-[#091011] transition hover:bg-orange-300">
                  Solicitar demostración <i class="pi pi-arrow-up-right text-sm"></i>
                </a>
              </div>
            </div>

            <div class="grid gap-8 p-7 sm:p-10">
              <div>
                <span class="text-xs font-semibold uppercase tracking-widest text-primary-300">Descripción comercial</span>
                <p class="muted mt-4 leading-7">{{ product.description }}</p>
              </div>

              <div class="rounded-2xl border border-orange-300/15 bg-orange-300/[.04] p-5">
                <span class="text-xs font-semibold uppercase tracking-widest text-orange-300">Propuesta de valor</span>
                <p class="mt-3 leading-7 text-white/85">{{ product.salesFocus }}</p>
              </div>

              <div class="grid gap-7 sm:grid-cols-2">
                <div>
                  <h5 class="font-semibold">Beneficios</h5>
                  <ul class="mt-4 space-y-3 text-sm text-white/65">
                    <li v-for="point in product.valuePoints" :key="point" class="flex gap-3"><i class="pi pi-check-circle mt-1 text-xs text-emerald-300"></i><span>{{ point }}</span></li>
                  </ul>
                </div>
                <div>
                  <h5 class="font-semibold">Funcionalidades</h5>
                  <ul class="mt-4 space-y-3 text-sm text-white/65">
                    <li v-for="feature in product.features" :key="feature" class="flex gap-3"><i class="pi pi-angle-right mt-1 text-xs text-primary-300"></i><span>{{ feature }}</span></li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </article>
      </div>

      <div id="servicios" class="scroll-mt-28 pt-20">
        <div class="mb-7">
          <p class="eyebrow mb-2">Servicios</p>
          <h3 class="text-2xl font-semibold sm:text-3xl">Capacidades para diseñar, integrar y evolucionar</h3>
        </div>

        <div class="grid gap-px overflow-hidden rounded-3xl bg-white/10 md:grid-cols-2">
          <article v-for="service in services" :id="`servicio-${service.id}`" :key="service.id" class="group bg-[#0d1516] p-7 transition hover:bg-[#121d1e] sm:p-9">
            <div class="flex items-start justify-between">
              <span class="grid h-12 w-12 place-items-center rounded-2xl bg-white/5 text-xl text-orange-300"><i :class="service.icon"></i></span>
              <span class="text-sm text-white/25">{{ service.number }}</span>
            </div>
            <h4 class="mt-8 text-2xl font-semibold">{{ service.title }}</h4>
            <p class="mt-2 text-sm font-medium text-primary-300">{{ service.tagline }}</p>
            <p class="muted mt-5 leading-7">{{ service.description }}</p>
            <ul class="mt-6 space-y-3 text-sm text-white/75">
              <li v-for="item in service.deliverables" :key="item" class="flex gap-3"><i class="pi pi-check mt-1 text-xs text-orange-300"></i>{{ item }}</li>
            </ul>
            <a href="#casos" class="mt-8 inline-flex items-center gap-2 text-sm font-semibold text-white transition group-hover:text-orange-300">Ver casos relacionados <i class="pi pi-arrow-right text-xs"></i></a>
          </article>
        </div>
      </div>
    </div>
  </section>
</template>
