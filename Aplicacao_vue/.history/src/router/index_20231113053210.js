import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../View/Home.vue'
import HomeTeste from '../View/HomeTeste.vue'
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
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
