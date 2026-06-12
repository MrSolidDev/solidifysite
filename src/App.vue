<script setup lang="ts">
import Header from '@/components/Header.vue'
import Presentacion from '@/components/Presentacion.vue'
import Servicios from '@/components/Servicios.vue'
import Proyectos from '@/components/Proyectos.vue'
import AboutMe from '@/components/AboutMe.vue'
import MisionVisionValores from '@/components/misionVisionValores.vue'
import Contacto from '@/components/Contacto.vue'
</script>

<template>
  <div class="site-shell">
    <Header />
    <main>
      <Presentacion id="inicio" />
      <Servicios id="soluciones" />
      <Proyectos id="casos" />
      <MisionVisionValores id="proceso" />
      <AboutMe id="empresa" />
    </main>
    <Contacto id="contacto" />
  </div>
</template>

<style>
@import "tailwindcss";
@import "tailwindcss-primeui";
@import "@fontsource/poppins/400.css";
@import "@fontsource/poppins/500.css";
@import "@fontsource/poppins/600.css";

:root {
  color-scheme: dark;
  font-family: "Poppins", ui-sans-serif, system-ui, sans-serif;
  background: #091011;
  color: #edf3ef;
  scroll-behavior: smooth;
}

* { box-sizing: border-box; }
body { margin: 0; min-width: 320px; background: #091011; }
a { color: inherit; text-decoration: none; }
button, a { -webkit-tap-highlight-color: transparent; }

.site-shell {
  min-height: 100vh;
  overflow: hidden;
  background:
    radial-gradient(circle at 85% 8%, rgba(126, 63, 242, .16), transparent 28rem),
    radial-gradient(circle at 10% 40%, rgba(255, 138, 0, .08), transparent 26rem),
    #091011;
}

.section-wrap { width: min(1180px, calc(100% - 2rem)); margin-inline: auto; }
.section-space { padding-block: clamp(5rem, 9vw, 8rem); scroll-margin-top: 5rem; }
.eyebrow { color: #ff9d2e; font-size: .75rem; font-weight: 600; letter-spacing: .2em; text-transform: uppercase; }
.display-title { font-size: clamp(2.25rem, 5vw, 4.8rem); line-height: 1.04; letter-spacing: -.045em; font-weight: 600; }
.section-title { font-size: clamp(2rem, 4vw, 3.5rem); line-height: 1.08; letter-spacing: -.035em; font-weight: 600; }
.muted { color: #9ba9a4; }
.glass-card { background: rgba(20, 30, 31, .72); border: 1px solid rgba(255,255,255,.09); backdrop-filter: blur(14px); }
.accent-line { width: 3.5rem; height: 2px; background: linear-gradient(90deg, #ff9d2e, #9a6cff); }

@media (max-width: 640px) {
  .section-wrap { width: min(100% - 1.25rem, 1180px); }
}
</style>
