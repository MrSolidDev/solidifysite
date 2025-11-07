<script setup lang="ts">
import  Timeline  from 'primevue/timeline';
import  Card  from 'primevue/card';
import Image from 'primevue/image';
import bryanr from '@/assets/bryanr.jpeg'
import { ref } from "vue";

import { scrollToNext } from '@/utilities/scroll';


const descripcion_html = `
  <section class="space-y-4 w-full">
    <p class="text-surface-600 leading-relaxed">
      Soy <strong class="text-primary-300">Bryan Rodríguez</strong>, 
      desarrollador de software con una pasión genuina por 
      <strong class="text-orange-400">crear tecnología con propósito</strong>.
    </p>

    <p class="text-surface-600 leading-relaxed">
      A lo largo de mi camino profesional he tenido la oportunidad de 
      trabajar en proyectos que combinan 
      <strong>ingeniería</strong>, <strong>diseño</strong> y <strong>experiencia humana</strong>: 
      desde sistemas <em>interactivos para retail y señalización digital</em>, 
      hasta <em>soluciones empresariales integradas con SAP</em> 
      y <em>plataformas web completas</em>.
    </p>

    <p class="text-surface-600 leading-relaxed">
      Mi experiencia abarca tanto el 
      <strong>desarrollo Full Stack</strong> 
      <span class="text-surface-400">(Python, Vue, React, Django, AWS)</span> 
      como la <strong>gestión de proyectos tecnológicos</strong>, 
      liderando equipos y propuestas de preventa con enfoque en 
      <span class="text-primary-400 font-medium">comunicación</span>, 
      <span class="text-primary-400 font-medium">claridad</span> 
      y <span class="text-primary-400 font-medium">resultados reales</span>.
    </p>
  </section>
`

const events = ref([
  {
    status: 'Hermas Suministros y Servicios',
    date: '2021–2022 · Soporte Técnico Remoto',
    icon: 'pi pi-headphones',
    color: '#7e3ff2', // morado Solidify
    html: `
      <p class="text-surface-300 leading-relaxed">
        Brindé <strong>soporte técnico remoto</strong> a más de <strong>400 sucursales</strong>, 
        gestionando sistemas de <em>señalización digital</em> y optimizando tiempos de respuesta entre equipos técnicos y operativos.
      </p>
      <ul class="list-disc ml-5 mt-2 text-surface-300 space-y-1">
        <li>Monitoreo, diagnóstico y coordinación de incidencias.</li>
        <li>Mejora de tiempos de atención y comunicación inter-áreas.</li>
      </ul>
      <div class="mt-3 border-l-4 border-[#7e3ff2] pl-3">
        <p class="text-surface-300">
          Primera gran lección: la tecnología <strong>solo tiene sentido</strong> cuando
          <strong>mejora la vida de las personas</strong>.
        </p>
      </div>
    `
  },
  {
    status: 'Multimedia Corporativa',
    date: '2022–2023 · Desarrollador Full Stack',
    icon: 'pi pi-code',
    color: '#ff8a00', // naranja acento
    html: `
      <p class="text-surface-300 leading-relaxed">
        Desarrollé <strong>soluciones interactivas</strong> para retail y entretenimiento,
        integrando <em>sensores</em>, <em>APIs</em> y <em>experiencias visuales</em>.
      </p>
      <ul class="list-disc ml-5 mt-2 text-surface-300 space-y-1">
        <li>Integración de hardware (PIR, cámaras, micrófonos) como <em>triggers</em>.</li>
        <li>Backends y APIs para sincronizar contenidos y métricas.</li>
      </ul>
      <div class="mt-3 border-l-4 border-[#ff8a00] pl-3">
        <p class="text-surface-300">
          Aprendí a unir el código con la <strong>creatividad</strong>: software que <strong>funciona</strong> y que <strong>conecta</strong>.
        </p>
      </div>
    `
  },
  {
    status: 'Multimedia Corporativa',
    date: '2023–2025 · Ingeniero de Preventa / Project Manager',
    icon: 'pi pi-briefcase',
    color: '#cbd5e1', // plata/gris claro
    html: `
      <p class="text-surface-300 leading-relaxed">
        Diseñé <strong>soluciones tecnológicas</strong> a la medida y lideré procesos de 
        <em>preventa</em>, documentación y <em>demos</em> para clientes empresariales.
      </p>
      <ul class="list-disc ml-5 mt-2 text-surface-300 space-y-1">
        <li>Levantamiento de necesidades y traducción a propuestas técnicas.</li>
        <li>Gestión de roadmap, entregables y comunicación con stakeholders.</li>
      </ul>
      <div class="mt-3 border-l-4 border-[#cbd5e1] pl-3">
        <p class="text-surface-300">
          Descubrí el valor de <strong>escuchar</strong>, entender y convertir <strong>ideas</strong> en propuestas tangibles.
        </p>
      </div>
    `
  },
  {
    status: 'MAVI de Occidente S.A. de C.V.',
    date: '2025-Actualidad · Desarrollador Full Stack',
    icon: 'pi pi-database',
    color: '#7e3ff2',
    html: `
      <p class="text-surface-300 leading-relaxed">
        Desarrollo <strong>soluciones empresariales</strong> para el ecosistema 
        <strong>SAP / AWS</strong>, incluyendo <em>dashboards financieros</em>, 
        herramientas de <em>control interno</em> y <em>automatizaciones</em> 
        basadas en <strong>Lambda Functions</strong>.
      </p>

      <ul class="list-disc ml-5 mt-2 text-surface-300 space-y-1">
        <li>
          Implementación con <strong>Vue 3</strong>, <strong>TypeScript</strong>, 
          <strong>PrimeVue</strong>, <strong>Tailwind</strong>, 
          <strong>Pinia</strong> y <strong>Axios</strong>.
        </li>
        <li>
          Integraciones con <strong>APIs OData</strong> y <strong>servicios REST</strong> 
          sobre infraestructura <strong>AWS (S3, CodePipeline, Lambdas, Code Commit, etc.)</strong>.
        </li>
        <li>
          Diseño de <strong>componentes reutilizables</strong> y 
          <strong>composables personalizados</strong> para optimizar flujos.
        </li>
        <li>
          Arquitectura modular enfocada en <strong>eficiencia operativa</strong> 
          para áreas <em>financieras</em> y <em>logísticas</em>.
        </li>
      </ul>

      <div class="mt-3 border-l-4 border-[#7e3ff2] pl-3 bg-white/5 rounded-sm py-2">
        <p class="text-surface-300 leading-relaxed">
          Esta experiencia me ha permitido conectar la 
          <strong>ingeniería del software</strong> con la 
          <strong>realidad empresarial</strong>, 
          creando soluciones que <strong>aportan valor tangible</strong> al negocio.
        </p>
      </div>
    `
}
])

</script>

<template>
    <div class="flex flex-col w-full justify-center items-center gap-8">
      <div class="flex flex-col w-full items-center min-h-screen">
        <div v-animateonscroll="{ enterClass: 'animate-enter fade-in-10 animate-duration-1000', leaveClass: 'animate-leave fade-out-0' }"
        class="flex flex-col w-full items-center text-center gap-2 sm:gap-3 py-6">
            <h2 class="text-3xl sm:text-4xl font-bold text-primary-500 tracking-wide">
                Mi trayectoria
            </h2>

            <div class="h-[3px] w-16 bg-gradient-to-r from-purple-500 via-orange-400 to-pink-400 rounded-full my-2"></div>

            <h4 class="text-surface-600 text-base sm:text-lg max-w-[700px] leading-relaxed font-light">
                Una carrera construida sobre <strong class="text-primary-300 font-medium">curiosidad</strong>, 
                <strong class="text-orange-400 font-medium">propósito</strong> 
                y <strong class="text-primary-400 font-medium">evolución constante</strong>.
            </h4>
        </div>
        <div class="flex justify-center w-full items-center gap-8">
            <Image v-animateonscroll="{ enterClass: 'animate-enter fade-in-10 slide-in-from-l-8 animate-duration-1000', leaveClass: 'animate-leave fade-out-0' }"
             :src="bryanr" alt="BryanRodriguez" width="250px" class="shadow-[0_4px_8px_rgba(0,0,0,0.5)]" preview></Image>
            <div class="max-w-3xl text-lg space-y-3" 
            v-animateonscroll="{ enterClass: 'animate-enter fade-in-10 slide-in-from-r-8 animate-duration-1000', leaveClass: 'animate-leave fade-out-0' }"
            v-html="descripcion_html"></div>
            
        </div>
        <div
            class="mt-10 animate-bounce text-orange-400 text-6xl cursor-pointer drop-shadow-[0_0_10px_rgba(255,138,0,0.5)] hover:drop-shadow-[0_0_15px_rgba(255,138,0,0.8)] transition-all"
            @click="scrollToNext"
            >
            <i class="pi pi-angle-down"></i>
          </div>
      </div>
      <div class="flex flex-col w-[90%] items-center justify-center items-center gap-8 min-h-screen">
        <div v-animateonscroll="{ enterClass: 'animate-enter fade-in-10 slide-in-from-b-20 animate-duration-1000' }">
          <h2 class="text-3xl sm:text-4xl text-center font-bold text-primary-500 tracking-wide">
                  Mi experiencia
          </h2>
        </div>
        <div class="card ">
           <Timeline :value="events" align="alternate" class="customized-timeline">
                <!-- Marcador (icono circular con color del evento) -->
                <template #marker="slotProps">
                    <span
                    class="flex w-9 h-9 items-center justify-center text-white rounded-full z-10 shadow-sm ring-2 ring-white/10"
                    :style="{ backgroundColor: slotProps.item.color }"
                    >
                    <i :class="slotProps.item.icon"></i>
                    </span>
                </template>

                <!-- Contenido (Card con título, fecha y html rico) -->
                <template #content="slotProps">
                    <Card 
                    v-animateonscroll="{ enterClass: 'animate-enter fade-in-10 slide-in-from-t-20 animate-duration-1000' }"
                    class="mt-4 bg-[#161E21] text-surface-100 border border-white/5 rounded-2xl overflow-hidden">
                        <template #title>
                            <div class="flex items-center gap-2">
                                <i :class="slotProps.item.icon" class="opacity-80"></i>
                                <span class="font-semibold">{{ slotProps.item.status }}</span>
                            </div>
                        </template>

                        <template #subtitle>
                            <span class="text-surface-400 ">{{ slotProps.item.date }}</span>
                        </template>

                        <template #content>
                            <div class="rich text-base leading-relaxed space-y-3 text-left" v-html="slotProps.item.html"></div>
                        </template>
                    </Card>
                </template>
            </Timeline>
        </div>
        <div
            class="mt-10 animate-bounce text-orange-400 text-6xl cursor-pointer drop-shadow-[0_0_10px_rgba(255,138,0,0.5)] hover:drop-shadow-[0_0_15px_rgba(255,138,0,0.8)] transition-all"
            @click="scrollToNext"
            >
            <i class="pi pi-angle-down"></i>
          </div>
      </div>
    </div>
</template>

<style scoped>
/* Evita centrado en items alternos del timeline */
.customized-timeline .p-timeline-event-content { text-align: left; }

/* Listas: viñetas coherentes y sin sangrías extrañas */
.customized-timeline .rich ul {
  list-style: disc;
  list-style-position: inside; /* la viñeta “entra” al mismo bloque del texto */
  padding-left: 0;             /* evita doble sangría */
  margin: .5rem 0;
}
.customized-timeline .rich li { margin: .25rem 0; }

/* (Opcional) Color de la viñeta acorde a tu paleta */
.customized-timeline .rich li::marker { color: #7e3ff2; } /* morado Solidify */
@media screen and (max-width: 960px) {
    ::v-deep(.customized-timeline) {
        .p-timeline-event:nth-child(even) {
            flex-direction: row;

            .p-timeline-event-content {
                text-align: left;
            }
        }

        .p-timeline-event-opposite {
            flex: 0;
        }
    }
}
</style>