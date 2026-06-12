<script setup lang="ts">
import { processSteps } from '@/data/siteContent'
</script>

<template>
  <section class="section-space border-y border-white/6 bg-[#0c1415]">
    <div class="section-wrap">
      <div class="grid gap-8 lg:grid-cols-[.75fr_1.25fr]">
        <div>
          <p class="eyebrow mb-4">Cómo trabajamos</p>
          <h2 class="section-title">Menos incertidumbre. Más avances visibles.</h2>
          <p class="muted mt-5 max-w-md leading-7">Un proceso colaborativo que mantiene alineadas las decisiones de negocio, la experiencia y la ejecución técnica.</p>
        </div>

        <ol class="grid gap-px overflow-hidden rounded-3xl bg-white/10 sm:grid-cols-2">
          <li v-for="step in processSteps" :key="step.number" class="bg-[#10191a] p-7 sm:p-8">
            <span class="text-sm font-semibold text-orange-300">{{ step.number }}</span>
            <h3 class="mt-8 text-xl font-semibold">{{ step.title }}</h3>
            <p class="muted mt-3 text-sm leading-6">{{ step.text }}</p>
          </li>
        </ol>
      </div>
    </div>
  </section>
</template>
