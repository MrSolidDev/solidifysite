<script lang="ts" setup>
    import  {ref} from 'vue'
    import Image  from 'primevue/image';
    import Breadcrumb from 'primevue/breadcrumb';
    import logo from '@/assets/logo.jpg';
    import TieredMenu from 'primevue/tieredmenu'
    import Button from 'primevue/button'

  
  //{ icon: 'pi pi-wallet', label: 'Proyectos' }
  //const items = ref([{ icon: 'pi pi-user', label: 'Sobre mi' },  { icon: 'pi pi-lightbulb', label: 'Solidify'}, { icon: 'pi pi-address-book', label: 'Conatacto' }]);

  function goTo(id: string) {
    const el = document.querySelector(id);
    if (el != null) {
      const y = el.getBoundingClientRect().top + window.scrollY - 200; // altura header
      window.scrollTo({ top: y, behavior: 'smooth' });  
    } else{
      return
    }
  }
  const home = ref({ icon: 'pi pi-home', command: () => goTo('#presentacion') });
  const items = [
    { label: 'Sobre mí',     icon: 'pi pi-user',     command: () => goTo('#about') },
    { label: 'Servicios',    icon: 'pi pi-briefcase', command: () => goTo('#servicios') },
    { label: 'M/V/V',        icon: 'pi pi-heart',     command: () => goTo('#mvv') },
    { label: 'Contacto',        icon: 'pi-address-book',     command: () => goTo('#contacto') }
  ];

  const menu = ref()
  const toggle = (ev: any) => menu.value?.toggle(ev)

</script>

<template>
  <header class="sticky top-0 z-50">
      <div class="flex gap-5 items-center w-full bg-[#161E21] justify-between
                  shadow-[0_4px_12px_rgba(0,0,0,0.4)] p-4 rounded-b-2xl border-b border-white/10">
        <div class="card flex gap-5 items-center">
          <Image :src="logo" alt="solidify" width="130" />
          <div class="flex flex-col gap-1">
            <h1 class="text-primary text-4xl md:text-5xl leading-tight">SOLIDIFY</h1>
            <h2 class="text-orange-600 text-lg md:text-2xl">Turning ideas into solid reality</h2>
          </div>
        </div>
        <div class="card flex justify-center hidden md:flex">
          <Breadcrumb
              :home="home"
              :model="items"
              :pt="{
                root: { class: 'bg-[#161E21] p-2 rounded-lg border border-white/5 shadow' }
              }"
            >
              <template #item="{ item, props }">
                <a
                  href=""
                  v-bind="props.action"
                  @click.prevent
                  class="flex items-center gap-2 px-2 py-1 hover:text-primary-300 transition-colors"
                >
                  <span :class="[item.icon, 'pi-fw', 'text-primary-200']" />
                  <span class="font-semibold text-surface-200">{{ item.label }}</span>
                </a>
              </template>
          </Breadcrumb>
        </div>
        <div class="card justify-center flex md:hidden">
            <Button
              type="button"
              icon="pi pi-bars"
              class="p-button-rounded p-button-text text-primary-200"
              @click="toggle"
              aria-haspopup="true"
              aria-controls="overlay_tmenu"
            />
            <TieredMenu
              ref="menu"
              id="overlay_tmenu"
              :model="items"
              popup
            />
        </div>
      </div>
  </header>
</template>


<style scoped>
</style>