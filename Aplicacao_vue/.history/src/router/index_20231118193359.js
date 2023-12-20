import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../View/Home.vue'
import jazao_component from '../View/jazao.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/jazao',
    name: 'Jazao',
    component: jazao_component
    //component: () => import(/* webpackChunkName: "about" */ '../View/HomeTeste.vue')
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
