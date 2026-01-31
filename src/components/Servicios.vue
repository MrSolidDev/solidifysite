<script lang="ts" setup>
import Card from 'primevue/card';
import Button from 'primevue/button';
import Tag from 'primevue/tag';
import { scrollToNext } from '@/utilities/scroll';

const servicios = [
  {
    value: '0',
    servicio: '🟣 1. Desarrollo a medida',
    html: `
      <header class="mb-3">
        <h3 class="text-xl font-semibold text-primary-200">Desarrollo a medida</h3>
        <p class="text-sm text-primary-400/80">Aplicaciones web diseñadas específicamente para tus necesidades.</p>
      </header>

      <section class="space-y-3">
        <div>
          <h4 class="font-medium text-surface-100">Descripción general</h4>
          <p class="text-surface-300 leading-relaxed">
            Construimos <strong>aplicaciones web</strong> hechas a tu medida. Desde sistemas empresariales hasta plataformas interactivas,
            desarrollamos soluciones <strong>estables</strong>, <strong>escalables</strong> y con una <strong>experiencia de usuario fluida</strong>.
          </p>
        </div>

        <div>
          <h4 class="font-medium text-surface-100">Qué incluye</h4>
          <ul class="list-disc ml-6 space-y-1 text-surface-300">
            <li><strong>Frontend moderno:</strong> Vue 3, PrimeVue y TypeScript.</li>
            <li><strong>Arquitecturas escalables:</strong> Python, FastAPI o AWS Lambda.</li>
            <li><strong>Integraciones:</strong> REST y OData con SAP, SQL Server y servicios externos.</li>
            <li><strong>Despliegue:</strong> AWS, Vercel o GitHub Pages con pipelines <em>CI/CD</em> automatizados.</li>
          </ul>
        </div>

        <div class="border-l-4 border-violet-500 pl-4 bg-white/5 rounded-sm py-2">
          <h4 class="font-medium text-surface-100">Enfoque Solidify</h4>
          <p class="text-surface-300">
            No creemos en “una app más”. Diseñamos para <strong>resolver problemas reales</strong>, con una interfaz intuitiva y <strong>código sólido</strong>.
          </p>
        </div>
      </section>
    `
  },
  {
    value: '2',
    servicio: '🟠 2. Integraciones empresariales',
    html: `
      <header class="mb-3">
        <h3 class="text-xl font-semibold text-primary-200">Integraciones empresariales</h3>
        <p class="text-sm text-primary-400/80">Hacemos que tus herramientas se hablen entre sí sin fricciones.</p>
      </header>

      <section class="space-y-3">
        <div>
          <h4 class="font-medium text-surface-100">Descripción general</h4>
          <p class="text-surface-300 leading-relaxed">
            Conectamos sistemas que antes trabajaban aislados para que la <strong>información fluya</strong> de forma segura y confiable.
          </p>
        </div>

        <div>
          <h4 class="font-medium text-surface-100">Qué hacemos</h4>
          <ul class="list-disc ml-6 space-y-1 text-surface-300">
            <li><strong>SAP S/4HANA:</strong> Integraciones mediante OData Services.</li>
            <li><strong>Automatización contable/financiera:</strong> anticipos, devoluciones, salidas y reversas.</li>
            <li><strong>Sincronización:</strong> SQL Server / SQL Express.</li>
            <li><strong>APIs seguras:</strong> interoperabilidad entre sistemas internos.</li>
          </ul>
        </div>

        <div class="border-l-4 border-orange-500 pl-4 bg-white/5 rounded-sm py-2">
          <h4 class="font-medium text-surface-100">Enfoque Solidify</h4>
          <p class="text-surface-300">
            La transformación digital ocurre cuando todo tu <strong>ecosistema</strong> se comunica. Nosotros lo hacemos posible.
          </p>
        </div>
      </section>
    `
  },
  {
    value: '1',
    servicio: '🟢 3. Experiencias interactivas',
    html: `
      <header class="mb-3">
        <h3 class="text-xl font-semibold text-primary-200">Experiencias interactivas</h3>
        <p class="text-sm text-primary-400/80">Tecnología + creatividad + emoción para experiencias únicas.</p>
      </header>

      <section class="space-y-3">
        <div>
          <h4 class="font-medium text-surface-100">Descripción general</h4>
          <p class="text-surface-300 leading-relaxed">
            Desde pantallas inteligentes hasta instalaciones con sensores, llevamos tus ideas al <strong>mundo físico</strong>.
          </p>
        </div>

        <div>
          <h4 class="font-medium text-surface-100">Ejemplos y alcances</h4>
          <ul class="list-disc ml-6 space-y-1 text-surface-300">
            <li><strong>QuickplayX:</strong> digital signage con reproducción automática de video/imagen.</li>
            <li><strong>Triggers por sensores:</strong> PIR, cámaras o micrófonos.</li>
            <li><strong>Control de efectos:</strong> iluminación, proyecciones, microcontroladores o Raspberry&nbsp;Pi.</li>
            <li><strong>Instalaciones temáticas:</strong> reactividad a movimiento o sonido.</li>
          </ul>
        </div>

        <div class="border-l-4 border-emerald-500 pl-4 bg-white/5 rounded-sm py-2">
          <h4 class="font-medium text-surface-100">Enfoque Solidify</h4>
          <p class="text-surface-300">
            <strong>Tecnología que se siente viva.</strong> Experiencias que <em>despiertan emociones</em>.
          </p>
        </div>
      </section>
    `
  },
  {
    value: '3',
    servicio: '🔵 4. Consultoría tecnológica',
    html: `
      <header class="mb-3">
        <h3 class="text-xl font-semibold text-primary-200">Consultoría tecnológica</h3>
        <p class="text-sm text-primary-400/80">Decisiones técnicas claras, con estrategia y enfoque humano.</p>
      </header>

      <section class="space-y-3">
        <div>
          <h4 class="font-medium text-surface-100">Descripción general</h4>
          <p class="text-surface-300 leading-relaxed">
            A veces no se trata de construir algo nuevo, sino de <strong>entender mejor</strong> lo que ya tienes.
          </p>
        </div>

        <div>
          <h4 class="font-medium text-surface-100">Qué ofrecemos</h4>
          <ul class="list-disc ml-6 space-y-1 text-surface-300">
            <li>Asesoría en <strong>arquitectura</strong>, <strong>bases de datos</strong> y <strong>despliegue en la nube</strong>.</li>
            <li>Auditoría de código y <strong>revisión de seguridad</strong>.</li>
            <li>Diseño de <strong>procesos</strong> alineados a negocio.</li>
            <li><strong>Capacitación</strong> y acompañamiento en buenas prácticas.</li>
          </ul>
        </div>

        <div class="border-l-4 border-sky-500 pl-4 bg-white/5 rounded-sm py-2">
          <h4 class="font-medium text-surface-100">Enfoque Solidify</h4>
          <p class="text-surface-300">
            Que <strong>entiendas</strong> la tecnología que usas, para crecer con <strong>confianza</strong> y <strong>autonomía</strong>.
          </p>
        </div>
      </section>
    `
  }
]


</script>

<template>
  <div
    class="flex flex-col w-full justify-center items-center gap-6 min-h-screen py-12 px-4"
  >
    <h2 class="text-3xl text-center sm:text-4xl font-bold text-primary-400 tracking-wide">
      Servicios
    </h2>
    <div class="h-[3px] w-20 bg-gradient-to-r from-purple-500 via-orange-400 to-pink-400 rounded-full mx-auto"></div>

    <div class="grid grid-cols-1 w-full max-w-6xl gap-5 md:grid-cols-2">
      <Card
        v-for="servicio in servicios"
        :key="servicio.servicio"
        class="bg-[#161E21] border border-white/10 rounded-2xl text-surface-200 shadow-[0_6px_18px_rgba(0,0,0,0.45)] hover:-translate-y-1 hover:shadow-[0_12px_28px_rgba(0,0,0,0.55)] transition-all duration-300"
      >
        <template #title>
          <div class="flex items-center gap-2 justify-between">
            <h3 class="text-xl font-semibold">{{ servicio.servicio.replace(/^[^ ]+\s/, '') }}</h3>
            <Tag value="Servicio" severity="info" class="text-xs" />
          </div>
        </template>
        <template #subtitle>
          <span class="text-sm text-primary-300">Incluye alcances y enfoque</span>
        </template>
        <template #content>
          <div
            class="rich text-surface-100 text-base leading-relaxed space-y-3 prose prose-invert bg-transparent !bg-transparent"
            v-html="servicio.html"
          ></div>
        </template>
        <template #footer>
          <div class="flex gap-2 flex-wrap">
            <Button
              label="Agendar llamada"
              icon="pi pi-calendar"
              class="p-button-sm p-button-rounded bg-orange-500 border-orange-500 text-[#0e1315]"
              as="a"
              href="#contacto"
            />
            <Button
              label="Ver proyectos relacionados"
              icon="pi pi-briefcase"
              class="p-button-sm p-button-rounded p-button-outlined text-primary-200 border-primary-300/70"
              as="a"
              href="#proyectos"
            />
          </div>
        </template>
      </Card>
    </div>

    <div
      class="mt-10 animate-bounce text-orange-400 text-6xl cursor-pointer drop-shadow-[0_0_10px_rgba(255,138,0,0.5)] hover:drop-shadow-[0_0_15px_rgba(255,138,0,0.8)] transition-all"
      @click="scrollToNext"
    >
      <i class="pi pi-angle-down"></i>
    </div>
  </div>
</template>
