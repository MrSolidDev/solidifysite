<script lang="ts" setup>
    import  {ref} from 'vue'
    import Image  from 'primevue/image';
    import logo from '@/assets/logo.jpg'
</script>

<template>
  <header class="sticky top-0 z-50">
    <div class="flex gap-5 items-center w-full bg-[#161E21]
                shadow-[0_4px_12px_rgba(0,0,0,0.4)] p-4 rounded-b-2xl border-b border-white/10">
      <Image :src="logo" alt="solidify" width="130" />
      <div class="flex flex-col gap-1">
        <h1 class="text-primary text-4xl md:text-5xl leading-tight">SOLIDIFY</h1>
        <h2 class="text-orange-600 text-lg md:text-2xl">Turning ideas into solid reality</h2>
      </div>
    </div>
  </header>
</template>


<style scoped>
</style>