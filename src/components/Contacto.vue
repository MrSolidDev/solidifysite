<script lang="ts" setup>
    import  {ref} from 'vue'
    import Image  from 'primevue/image';
    import Breadcrumb from 'primevue/breadcrumb';
    import logo from '@/assets/logo.jpg';


</script>


<template>
  <footer
    class="w-full bg-[#161E21] border-t border-white/10 shadow-[0_-4px_12px_rgba(0,0,0,0.3)]
           text-surface-300 flex flex-col items-center justify-center text-center px-6 py-10
           rounded-t-2xl mt-20"
           v-animateonscroll="{ enterClass: 'animate-enter fade-in-10 slide-in-from-b-20 animate-duration-1000' }"
  >
    <!-- Logo + lema -->
    <div class="flex flex-col md:flex-row gap-4 md:gap-8 items-center justify-center">
      <div class="flex flex-col gap-1 justify-center items-center md:items-start">
        <h1 class="text-primary text-4xl md:text-5xl font-bold tracking-wide text-center">SOLIDIFY</h1>
        <h2 class="text-orange-500 text-lg md:text-2xl italic font-light">
          Turning ideas into solid reality
        </h2>
      </div>
    </div>

    <!-- Línea divisoria -->
    <div class="h-[2px] w-24 bg-gradient-to-r from-purple-500 via-orange-400 to-pink-400 rounded-full my-6"></div>

    <!-- Información de contacto -->
    <div class="flex flex-col md:flex-row gap-6 md:gap-10 items-center justify-center text-sm md:text-base">
      <div class="flex items-center gap-2">
        <i class="pi pi-envelope text-orange-400"></i>
        <a href="mailto:rdgz.d.bryan@gmail.com" class="hover:text-primary-300 transition-all">rdgz.d.bryan@gmail.com</a>
      </div>
      <div class="flex items-center gap-2">
        <i class="pi pi-phone text-orange-400"></i>
        <a href="tel:+5215581100428" class="hover:text-primary-300 transition-all">+52 55 8110 0428</a>
      </div>
      <div class="flex items-center gap-2">
        <i class="pi pi-linkedin text-orange-400"></i>
        <a href="https://www.linkedin.com/in/bryan-rodriguez-dev" target="_blank" class="hover:text-primary-300 transition-all">LinkedIn</a>
      </div>
      <div class="flex items-center gap-2">
        <i class="pi pi-github text-orange-400"></i>
        <a href="https://github.com/MrSolidDev" target="_blank" class="hover:text-primary-300 transition-all">GitHub</a>
      </div>
    </div>

    <!-- Derechos reservados -->
    <p class="text-surface-500 text-xs md:text-sm mt-8">
      © {{ new Date().getFullYear() }} Solidify — Todos los derechos reservados.
    </p>
  </footer>
</template>




<style scoped>
</style>