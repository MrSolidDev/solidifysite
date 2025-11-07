<script lang="ts" setup>

import Fieldset  from 'primevue/fieldset';
import Tabs from 'primevue/tabs';
import TabList from 'primevue/tablist';
import Tab from 'primevue/tab';
import TabPanels from 'primevue/tabpanels';
import TabPanel from 'primevue/tabpanel';
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
    <div v-animateonscroll="{ enterClass: 'animate-enter fade-in-10 slide-in-from-l-8 animate-duration-1000', leaveClass: 'animate-leave fade-out-0' }"
     class="flex flex-col w-full justify-center items-center gap-5 min-h-screen">
        <Fieldset legend="Servicios - Lo que hacemos, lo hacemos con propósito" class="w-[90%] text-primary rounded-b-2xl p-4 shadow-[_0_4px_4px_rgba(0,0,0,0.5)]">
            <div class="flex flex-col gap-4 min-h-full">
                <h2 class="text-primary-400 ">En Solidify no solo desarrollamos software; creamos soluciones que conectan, facilitan y potencian el crecimiento de tu proyecto o empresa.</h2>
                <Tabs class="flex flex-col flex-1 bg-[#161E21]" value="0">
                    <TabList class="bg-[#161E21] flex-shrink-0 border-b border-surface-700">
                        <Tab 
                        class="text-orange-500 font-medium hover:text-orange-400 transition-colors" 
                        v-for="servicio in servicios" :key="servicio.servicio" :value="servicio.value">
                                <h2 class="font-semibold text-sm sm:text-base">{{ servicio.servicio }}</h2>
                        </Tab>
                    </TabList>
                    <TabPanels class="bg-[#161E21] rounded-b-2xl h-full">
                        <TabPanel v-for="servicio in servicios" :key="servicio.html" :value="servicio.value">
                            <div class="rich text-surface-100 text-base leading-relaxed space-y-3" v-html="servicio.html"></div>
                        </TabPanel>
                    </TabPanels>
                </Tabs>
            </div>
        </Fieldset>
        <div
        class="mt-10 animate-bounce text-orange-400 text-6xl cursor-pointer drop-shadow-[0_0_10px_rgba(255,138,0,0.5)] hover:drop-shadow-[0_0_15px_rgba(255,138,0,0.8)] transition-all"
        @click="scrollToNext"
        >
            <i class="pi pi-angle-down"></i>
        </div>
    </div>
</template>
