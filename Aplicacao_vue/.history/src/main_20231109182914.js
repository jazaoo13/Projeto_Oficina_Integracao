import Vue from 'vue'
import App from './App.vue'
import {BootstrapVue, IconsPlugin} from 'bootstrap-vue';
import 'font-awesome/css/font-awesome.css';
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'bootstrap/dist/css/bootstrap.css'

Vue.config.productionTip = false
Vue.use(BootstrapVue);
Vue.use(IconsPlugin);

new Vue({
  render: h => h(App),
}).$mount('#app')
