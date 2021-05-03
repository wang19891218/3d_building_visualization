import { createApp } from 'vue'
import "./index.css"
import Header from "./Header.vue"
import AppMap from "./AppMap.vue"
// createApp(App).mount('#app')

createApp(Header).mount("#AppHeader")
createApp(AppMap).mount("#AppMap")