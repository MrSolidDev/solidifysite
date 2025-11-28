<script lang="ts" setup>
import { scrollToNext } from '@/utilities/scroll';
</script>
<template>
    <div class="flex flex-col items-center text-center w-full min-h-screen gap-10 scroll-mt-20">
        <div class="flex flex-col w-[90%] justify-center items-center text-center py-10 px-6 gap-4 bg-gradient-to-b from-[#161E21] to-[#0e1315] rounded-2xl shadow-[0_4px_8px_rgba(0,0,0,0.3)]">
            <h2 class="text-3xl sm:text-4xl font-bold text-primary-200 tracking-wide">
            Creemos en las ideas que se vuelven realidad
            </h2>

            <div class="h-[3px] w-20 bg-gradient-to-r from-purple-500 via-orange-400 to-pink-400 rounded-full my-2"></div>

            <p class="text-surface-300 text-lg sm:text-xl max-w-[800px] leading-relaxed font-light">
            En <strong class="text-primary-300">Solidify</strong> creemos que cada proyecto comienza con una 
            <strong class="text-orange-400">visión</strong>.  
            Nuestro propósito es acompañarte desde la idea hasta el resultado final, 
            construyendo <strong class="text-primary-200">soluciones tecnológicas</strong> 
            <em> claras</em>, <em>confiables</em> y <em>hechas a tu medida</em>.
            </p>
        </div>
        <div
        class="mt-10 animate-bounce text-orange-400 text-6xl cursor-pointer drop-shadow-[0_0_10px_rgba(255,138,0,0.5)] hover:drop-shadow-[0_0_15px_rgba(255,138,0,0.8)] transition-all"
        @click="scrollToNext"
        >
            <i class="pi pi-angle-down"></i>
        </div>
    </div>
</template>

