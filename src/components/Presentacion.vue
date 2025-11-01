<script lang="ts" setup>
import { content } from '@primeuix/themes/aura/accordion';
import Card from 'primevue/card'
import Fieldset  from 'primevue/fieldset';
import Tabs from 'primevue/tabs';
import TabList from 'primevue/tablist';
import Tab from 'primevue/tab';
import TabPanels from 'primevue/tabpanels';
import TabPanel from 'primevue/tabpanel';


const cards = [
    {
        title: 'Transformamos ideas en realidades sólidas', 
        content:    `En Solidify creemos que cada proyecto empieza con una visión.
                    Nuestro propósito es acompañarte desde la idea hasta el resultado final,
                    construyendo soluciones tecnológicas claras, confiables y hechas a tu medida.`
    },
    {
        title: 'Una empresa joven, con pensamiento sólido y corazón humano', 
        content:    `Solidify nació con la idea de combinar la creatividad con la ingeniería.
                    Somos un equipo liderado por Bryan Rodríguez, ingeniero de software y apasionado por transformar conceptos en soluciones funcionales y bellas.

                    No creemos en los desarrollos genéricos. Creemos en escuchar, entender y crear tecnología que realmente aporte valor.`
    },
]

const servicios = [
    {
        servicio: "Desarrollo a medida",
        descripcion: `Aplicaciones web modernas con Vue, PrimeVue y TypeScript, integradas con Python y AWS Lambda para un backend rápido, seguro y escalable`,
        value: '0'
    },
    {
        servicio: "Experiencias interactivas",
        descripcion: `Creamos experiencias digitales e instalaciones con sensores, pantallas y automatización — tecnología que se siente viva.`,
        value: '1'
    },
    {
        servicio: "Integraciones empresariales",
        descripcion: `Conectamos tu negocio con sistemas como SAP, OData, y SQL Server, optimizando procesos financieros y operativos.`,
        value: '2'  
    },
    {
        servicio: "Consultoría tecnológica",
        descripcion: `Te ayudamos a definir la arquitectura, elegir tecnologías y llevar tus ideas al siguiente nivel`,
        value: '3'
    },
]

</script>
<template>
    <div class="flex flex-col w-full justify-center items-center gap-5">
        <p class="m-0 text-2xl text-primary-900 max-w-[90%] text-center rounded-b-xl p-4">
            En Solidify creemos que cada proyecto empieza con una visión.
            Nuestro propósito es acompañarte desde la idea hasta el resultado final, 
            construyendo soluciones tecnológicas claras, confiables y hechas a tu medida.
        </p>
        <div class="flex w-full gap-4 justify-center">
            <Card
            v-for="(card, i) in cards"
            :key="i"
            class="w-full sm:w-[30%] bg-[#161E21] text-primary-400 shadow-[_0_4px_4px_rgba(0,0,0,0.5)] rounded-b-2xl p-4">
                <template #title>
                    <h2 class="font-semibold mb-6 text-2xl">{{card.title}}</h2>
                    
                </template>
                <template #content>
                    <p class="m-0 leading-relaxed text-lg whitespace-pre-line leading-relaxed text-surface-300 ">
                        {{ card.content }}
                    </p>
                </template>
            </Card>
        </div>
        <Fieldset legend="Servicios - Lo que hacemos, lo hacemos con propósito" class="w-[90%] text-primary rounded-b-2xl p-4 shadow-[_0_4px_4px_rgba(0,0,0,0.5)]">
            <div class="flex flex-col">
                <Tabs class="bg-[#161E21]" value="0">
                    <TabList class="bg-[#161E21]">
                        <Tab class="text-orange-600" v-for="servicio in servicios" :key="servicio.servicio" :value="servicio.value">
                                <h2>{{ servicio.servicio }}</h2>
                        </Tab>
                    </TabList>
                    <TabPanels class="bg-[#161E21] rounded-b-2xl">
                        <TabPanel v-for="servicio in servicios" :key="servicio.descripcion" :value="servicio.value">
                            <p class="m-0 leading-relaxed text-lg whitespace-pre-line leading-relaxed text-surface-100">
                                {{ servicio.descripcion }}
                            </p>
                        </TabPanel>
                    </TabPanels>
                </Tabs>
            </div>
        </Fieldset>
    </div>
</template>
