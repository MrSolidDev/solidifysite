<template>
  <footer class="border-t border-white/8 bg-[#070c0d] pt-20">
    <div class="section-wrap">
      <div class="grid gap-10 pb-16 lg:grid-cols-[1.2fr_.8fr] lg:items-end">
        <div>
          <p class="eyebrow mb-4">Construyamos algo útil</p>
          <h2 class="section-title max-w-3xl">¿Hay un proceso, producto o experiencia que necesita evolucionar?</h2>
          <a href="mailto:rdgz.d.bryan@gmail.com?subject=Proyecto%20con%20Solidify" class="mt-8 inline-flex items-center gap-3 rounded-full bg-orange-400 px-6 py-3.5 font-semibold text-[#091011] transition hover:bg-orange-300">
            Cuéntanos sobre el proyecto <i class="pi pi-arrow-up-right text-sm"></i>
          </a>
        </div>
        <div class="grid gap-4 text-sm lg:justify-self-end">
          <a href="mailto:rdgz.d.bryan@gmail.com" class="flex items-center gap-3 text-white/65 hover:text-white"><i class="pi pi-envelope text-orange-300"></i>rdgz.d.bryan@gmail.com</a>
          <a href="tel:+5215581100428" class="flex items-center gap-3 text-white/65 hover:text-white"><i class="pi pi-phone text-orange-300"></i>+52 55 8110 0428</a>
          <a href="https://www.linkedin.com/in/bryan-rodriguez-dev" target="_blank" rel="noopener" class="flex items-center gap-3 text-white/65 hover:text-white"><i class="pi pi-linkedin text-orange-300"></i>LinkedIn</a>
          <a href="https://github.com/MrSolidDev" target="_blank" rel="noopener" class="flex items-center gap-3 text-white/65 hover:text-white"><i class="pi pi-github text-orange-300"></i>GitHub</a>
        </div>
      </div>
      <div class="flex flex-col gap-3 border-t border-white/8 py-7 text-xs text-white/35 sm:flex-row sm:items-center sm:justify-between">
        <span>© {{ new Date().getFullYear() }} Solidify. Soluciones digitales.</span>
        <span>Diseño, ingeniería y evolución de producto.</span>
      </div>
    </div>
  </footer>
</template>
