import Vue from 'vue'
import VueRouter from 'vue-router'
import MainPageView from '@/views/MainPageView'
import MoviePickView from '@/views/MoviePickView'

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
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
