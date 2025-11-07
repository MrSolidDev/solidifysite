<script lang="ts" setup>
    import  {ref} from 'vue'
    import Image  from 'primevue/image';
    import Breadcrumb from 'primevue/breadcrumb';
    import logo from '@/assets/logo.jpg';

  const home = ref({ icon: 'pi pi-home' });
  const items = ref([{ icon: 'pi pi-user', label: 'Sobre mi' },  { icon: 'pi pi-lightbulb', label: 'Solidify'}, { icon: 'pi pi-wallet', label: 'Proyectos' }, { icon: 'pi pi-address-book', label: 'Conatacto' }]);
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
        <div class="card flex justify-center">
          <Breadcrumb :home="home" :model="items"
          :pt="{
              root: { class: 'bg-[#161E21] p-2 rounded-lg' }
          }">
            <template #item="{item, props}">
              <router-link v-if="item.route" v-slot="{ href, navigate }" :to="item.route" custom>
                    <a :href="href" v-bind="props.action" @click="navigate">
                        <span :class="[item.icon, 'pi-fw', 'text-surface-0']" />
                        <span class="text-surface-800 font-semibold">{{ item.label }}</span>
                    </a>
              </router-link>
                    <a v-else :href="item.url" :target="item.target" v-bind="props.action">
                        <span :class="[item.icon, 'pi-fw', 'text-surface-0']" />
                        <span class="text-surface-700 dark:text-surface-0">{{ item.label }}</span>
                    </a>
            </template>
          </Breadcrumb>
        </div>
      </div>
  </header>
</template>


<style scoped>
</style>