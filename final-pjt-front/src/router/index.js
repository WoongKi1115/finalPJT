import Vue from 'vue'
import VueRouter from 'vue-router'
import MainPageView from '@/views/MainPageView'
import MoviePickView from '@/views/MoviePickView'
import LoginPageView from '@/views/LoginPageView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'mainpage',
    component: MainPageView
  },
  {
    path: '/moviepick',
    name: 'moviepick',
    component: MoviePickView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginPageView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
