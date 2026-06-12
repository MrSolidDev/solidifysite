<template>
  <section class="section-wrap flex min-h-screen items-center pt-28 pb-16">
    <div class="grid w-full items-center gap-14 lg:grid-cols-[1.2fr_.8fr]">
      <div v-animateonscroll="{ enterClass: 'animate-enter fade-in-10 slide-in-from-b-8 animate-duration-700' }">
        <p class="eyebrow mb-6">Tecnología para operaciones reales</p>
        <h1 class="display-title max-w-4xl">
          Convertimos procesos complejos en
          <span class="text-primary-300">soluciones digitales claras.</span>
        </h1>
        <p class="muted mt-7 max-w-2xl text-lg leading-8">
          Solidify diseña software empresarial, integraciones y experiencias interactivas que conectan personas, información y operación.
        </p>
        <div class="mt-9 flex flex-col gap-3 sm:flex-row">
          <a href="#productos" class="rounded-full bg-orange-400 px-6 py-3.5 text-center font-semibold text-[#091011] transition hover:-translate-y-0.5 hover:bg-orange-300">Explorar soluciones</a>
          <a href="#casos" class="rounded-full border border-white/15 px-6 py-3.5 text-center font-medium transition hover:border-white/35 hover:bg-white/5">Ver casos de éxito <i class="pi pi-arrow-down-right ml-2 text-sm"></i></a>
        </div>
      </div>

      <div class="relative mx-auto w-full max-w-md">
        <div class="absolute -inset-8 rounded-full bg-primary-500/15 blur-3xl"></div>
        <div class="glass-card relative overflow-hidden rounded-[2rem] p-7 sm:p-9">
          <div class="mb-12 flex items-center justify-between">
            <span class="text-xs uppercase tracking-[.18em] text-white/45">Capacidades</span>
            <span class="h-2.5 w-2.5 rounded-full bg-emerald-400 shadow-[0_0_18px_#34d399]"></span>
          </div>
          <div class="space-y-6">
            <div class="flex items-center gap-4"><span class="grid h-11 w-11 place-items-center rounded-xl bg-primary-400/15 text-primary-200"><i class="pi pi-code"></i></span><div><b class="block">Producto digital</b><small class="muted">De la idea a producción</small></div></div>
            <div class="flex items-center gap-4"><span class="grid h-11 w-11 place-items-center rounded-xl bg-orange-400/15 text-orange-300"><i class="pi pi-link"></i></span><div><b class="block">Integración empresarial</b><small class="muted">SAP, AWS, APIs y datos</small></div></div>
            <div class="flex items-center gap-4"><span class="grid h-11 w-11 place-items-center rounded-xl bg-emerald-400/15 text-emerald-300"><i class="pi pi-sparkles"></i></span><div><b class="block">Experiencia interactiva</b><small class="muted">Software, contenido y sensores</small></div></div>
          </div>
          <div class="mt-10 border-t border-white/10 pt-5 text-sm text-white/50">Estrategia · Diseño · Desarrollo · Evolución</div>
        </div>
      </div>
    </div>
  </section>
</template>
