import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'home',
        component: () => import('../views/Home.vue'),
    },
    {
        path: '/reg',
        name: 'registration',
        component: () => import('../views/Reg.vue'),
        beforeEnter (to, from, next) {
            if (localStorage.isAuth) {
                next('/');
            } else {
                next()
            }
        },
    },
    {
        path: '/auth',
        name: 'authorization',
        component: () => import('../views/Auth.vue'),
        beforeEnter (to, from, next) {
            if (localStorage.isAuth) {
                next('/');
            } else {
                next()
            }
        },
    },
    {
        path: '/timetable',
        name: 'timetable',
        component: () => import('../views/Timetable.vue'),
    },
    {
        path: '/profile',
        name: 'profile',
        component: () => import('../views/Profile.vue'),
    }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
