<script lang="ts" setup>
    import  {ref} from 'vue'
    import Image  from 'primevue/image';
</script>

<template>
    <div class="flex gap-5 bg-[#161E21] items-center w-full">
        <Image src="src/assets/logo.jpg" alt="solidify" width="130"></Image>
        <div class="flex flex-col gap-2">
            <h1 class="text-primary text-5xl">SOLIDIFY</h1>
            <h2 class="text-orange-600 text-2xl">Turning ideas into solid reality</h2>
        </div>
    </div>
</template>

<style scoped>
</style>