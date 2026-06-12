<script setup lang="ts">
import {
  productFamilies,
  products,
  serviceFamilies,
  services,
} from '@/data/siteContent'

const productsByFamily = (familyId: string) => products.filter((product) => product.familyId === familyId)
const servicesByFamily = (familyId: string) => services.filter((service) => service.familyId === familyId)
</script>

<template>
  <section class="section-space border-y border-white/6 bg-white/[.025]">
    <div class="section-wrap">
      <div class="grid gap-8 lg:grid-cols-2 lg:items-end">
        <div>
          <p class="eyebrow mb-4">Soluciones</p>
          <h2 class="section-title">Un ecosistema organizado por familias, productos y capacidades.</h2>
        </div>
        <p class="muted max-w-xl text-lg leading-8 lg:justify-self-end">
          Cada familia responde a un propósito común. Los productos están listos para utilizar y personalizar; los servicios permiten construir, integrar y evolucionar cada solución.
        </p>
      </div>

      <div id="productos" class="scroll-mt-28 pt-16">
        <div class="mb-8 flex flex-col gap-2 sm:flex-row sm:items-end sm:justify-between">
          <div>
            <p class="eyebrow mb-2">Productos</p>
            <h3 class="text-2xl font-semibold sm:text-3xl">Ideas convertidas en soluciones listas para generar impacto.</h3>
          </div>
          <span class="text-sm text-white/40">Catálogo en crecimiento</span>
        </div>

        <section v-for="family in productFamilies" :key="family.id" :id="`familia-${family.id}`" class="overflow-hidden rounded-[2rem] border border-white/10 bg-[#0b1314]">
          <header class="relative overflow-hidden border-b border-white/8 p-7 sm:p-10">
            <div class="absolute inset-0 bg-[radial-gradient(circle_at_15%_0%,rgba(255,138,0,.17),transparent_44%),radial-gradient(circle_at_90%_100%,rgba(126,63,242,.16),transparent_42%)]"></div>
            <div class="relative grid gap-7 lg:grid-cols-[.75fr_1.25fr] lg:items-end">
              <div class="flex items-center gap-4">
                <span class="grid h-14 w-14 shrink-0 place-items-center rounded-2xl border border-orange-300/15 bg-orange-300/10 text-xl text-orange-300"><i :class="family.icon"></i></span>
                <div>
                  <p class="text-xs font-semibold uppercase tracking-[.18em] text-orange-300">{{ family.eyebrow }}</p>
                  <h4 class="mt-2 text-3xl font-semibold sm:text-4xl">{{ family.name }}</h4>
                </div>
              </div>
              <p class="muted max-w-2xl text-base leading-7 lg:justify-self-end">{{ family.description }}</p>
            </div>
          </header>

          <div class="space-y-px bg-white/8">
            <article v-for="product in productsByFamily(family.id)" :key="product.id" :id="`producto-${product.id}`" class="grid bg-[#10191a] lg:grid-cols-[.9fr_1.1fr]">
              <div class="relative overflow-hidden border-b border-white/8 p-7 lg:border-r lg:border-b-0 sm:p-10">
                <div class="absolute inset-0 bg-[radial-gradient(circle_at_20%_10%,rgba(255,138,0,.1),transparent_52%),radial-gradient(circle_at_90%_90%,rgba(126,63,242,.12),transparent_48%)]"></div>
                <div class="relative flex h-full flex-col">
                  <div class="flex items-center justify-between gap-4">
                    <span class="inline-flex items-center gap-2 rounded-full border border-emerald-300/20 bg-emerald-300/8 px-3 py-1.5 text-xs font-medium text-emerald-200">
                      <span class="h-1.5 w-1.5 rounded-full bg-emerald-300"></span>{{ product.status }}
                    </span>
                    <span class="grid h-12 w-12 place-items-center rounded-2xl bg-white/8 text-xl text-orange-300"><i :class="product.icon"></i></span>
                  </div>
                  <h5 class="mt-10 text-3xl font-semibold leading-tight sm:text-4xl">{{ product.title }}</h5>
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
                    <h6 class="font-semibold">Beneficios</h6>
                    <ul class="mt-4 space-y-3 text-sm text-white/65">
                      <li v-for="point in product.valuePoints" :key="point" class="flex gap-3"><i class="pi pi-check-circle mt-1 text-xs text-emerald-300"></i><span>{{ point }}</span></li>
                    </ul>
                  </div>
                  <div>
                    <h6 class="font-semibold">Funcionalidades</h6>
                    <ul class="mt-4 space-y-3 text-sm text-white/65">
                      <li v-for="feature in product.features" :key="feature" class="flex gap-3"><i class="pi pi-angle-right mt-1 text-xs text-primary-300"></i><span>{{ feature }}</span></li>
                    </ul>
                  </div>
                </div>
                <div class="border-t border-white/8 pt-6">
                  <h6 class="text-sm font-semibold">Casos de uso</h6>
                  <div class="mt-4 flex flex-wrap gap-2">
                    <span v-for="useCase in product.useCases" :key="useCase" class="rounded-full bg-white/5 px-3 py-1.5 text-xs text-white/55">{{ useCase }}</span>
                  </div>
                </div>
              </div>
            </article>
          </div>
        </section>
      </div>

      <div id="servicios" class="scroll-mt-28 pt-20">
        <div class="mb-8">
          <p class="eyebrow mb-2">Servicios</p>
          <h3 class="text-2xl font-semibold sm:text-3xl">Capacidades organizadas según el resultado buscado</h3>
        </div>

        <div class="grid gap-6 xl:grid-cols-2">
          <section v-for="family in serviceFamilies" :key="family.id" class="overflow-hidden rounded-3xl border border-white/10 bg-[#0d1516]">
            <header class="border-b border-white/8 bg-white/[.025] p-7 sm:p-8">
              <div class="flex items-start gap-4">
                <span class="grid h-12 w-12 shrink-0 place-items-center rounded-2xl bg-primary-300/10 text-primary-200"><i :class="family.icon"></i></span>
                <div>
                  <p class="text-xs font-semibold uppercase tracking-[.16em] text-primary-300">{{ family.eyebrow }}</p>
                  <h4 class="mt-2 text-2xl font-semibold">{{ family.name }}</h4>
                  <p class="muted mt-3 text-sm leading-6">{{ family.description }}</p>
                </div>
              </div>
            </header>

            <div class="divide-y divide-white/8">
              <article v-for="service in servicesByFamily(family.id)" :id="`servicio-${service.id}`" :key="service.id" class="group p-7 transition hover:bg-white/[.025] sm:p-8">
                <div class="flex items-start justify-between gap-4">
                  <span class="grid h-11 w-11 place-items-center rounded-xl bg-white/5 text-orange-300"><i :class="service.icon"></i></span>
                  <span class="text-xs text-white/25">{{ service.number }}</span>
                </div>
                <h5 class="mt-6 text-xl font-semibold">{{ service.title }}</h5>
                <p class="mt-2 text-sm font-medium text-primary-300">{{ service.tagline }}</p>
                <p class="muted mt-4 text-sm leading-6">{{ service.description }}</p>
                <ul class="mt-5 grid gap-3 text-sm text-white/70 sm:grid-cols-2">
                  <li v-for="item in service.deliverables" :key="item" class="flex gap-3"><i class="pi pi-check mt-1 text-xs text-orange-300"></i><span>{{ item }}</span></li>
                </ul>
                <a href="#casos" class="mt-6 inline-flex items-center gap-2 text-sm font-semibold text-white transition group-hover:text-orange-300">Ver casos relacionados <i class="pi pi-arrow-right text-xs"></i></a>
              </article>
            </div>
          </section>
        </div>
      </div>
    </div>
  </section>
</template>
