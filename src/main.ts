import { createApp } from 'vue'
import App from './App.vue'
import PrimeVue from 'primevue/config'
import Aura from '@primeuix/themes/aura'
import { definePreset, palette } from '@primeuix/themes'
import AnimateOnScroll from 'primevue/animateonscroll'
import 'primeicons/primeicons.css'
import router from './router'

const app = createApp(App)

const SoldifyPallete = definePreset(Aura, {
  semantic: {
    primary: palette('#4A3C7B')
  }
})

app.use(PrimeVue, {
    theme: {
        preset: SoldifyPallete,
        options: {
            prefix: 'p',
            darkModeSelector: '',
            cssLayer: {
                name: 'primevue',
                order: 'theme, base, primevue'
            }
        }
    }
})
app.use(router)

app.directive('animateonscroll', AnimateOnScroll)

app.mount('#app')
