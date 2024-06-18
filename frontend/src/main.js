import './assets/main.css'
import ToastPlugin from 'vue-toast-notification';
import 'vue-toast-notification/dist/theme-bootstrap.css';
import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import axios from 'axios'
import "bootstrap/dist/css/bootstrap.css"
import "bootstrap-vue/dist/bootstrap-vue.css"

axios.defaults.baseURL = 'http://localhost:8000'


const app = createApp(App)


app
    .use(createPinia())
    .use(ToastPlugin)
    .use(router, axios)
    .mount('#app')
