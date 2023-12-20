import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../View/Home.vue'
import HomeTeste from '../View/HomeTeste.vue'
import jazao_component from '../View/jazao.vue'
import test_component from '../View/Teste.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeTeste
  },
  {
    path: '/about',
    name: 'HomeTeste',
    component: Home
    //component: () => import(/* webpackChunkName: "about" */ '../View/HomeTeste.vue')
  },
  {
    path: '/jazao',
    name: 'Jazao',
    component: jazao_component
    //component: () => import(/* webpackChunkName: "about" */ '../View/HomeTeste.vue')
  },
  {
    path: '/teste',
    name: 'Teste',
    component: test_component
    //component: () => import(/* webpackChunkName: "about" */ '../View/HomeTeste.vue')
  }

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
