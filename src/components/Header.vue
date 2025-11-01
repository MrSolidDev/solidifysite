<script lang="ts" setup>
    import  {ref} from 'vue'
    import Image  from 'primevue/image';
    import logo from '@/assets/logo.jpg'
</script>

<template>
    <div class="flex gap-5 bg-[#161E21] items-center w-full shadow-[_0_4px_4px_rgba(0,0,0,0.5)] p-4 rounded-b-2xl">
        <Image :src="logo" alt="solidify" width="130"></Image>
        <div class="flex flex-col gap-2">
            <h1 class="text-primary text-5xl">SOLIDIFY</h1>
            <h2 class="text-orange-600 text-2xl">Turning ideas into solid reality</h2>
        </div>
    </div>
</template>

<style scoped>
</style>