import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'home',
        component: Home
    },
    {
        path: '/reg',
        name: 'registration',
        component: () => import('../views/Reg.vue'),
    },
    {
        path: '/auth',
        name: 'authorization',
        component: () => import('../views/Auth.vue'),
    }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
