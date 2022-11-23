import Vue from 'vue'
import VueRouter from 'vue-router'
import MainPageView from '@/views/MainPageView'
import MoviePickView from '@/views/MoviePickView'
import LoginPageView from '@/views/LoginPageView'
import SignupPageView from '@/views/SignupPageView'
import CommunityView from '@/views/CommunityView'
import createArticle from '@/views/createArticle'
import CommunityDetailView from '@/views/CommunityDetailView'
import SearchView from '@/views/SearchView'

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
  {
    path: '/signup',
    name: 'signup',
    component: SignupPageView
  },
  {
    path: '/community',
    name: 'community',
    component: CommunityView
  },
  {
    path: '/create',
    name: 'createArticle',
    component: createArticle
  },
  {
    path: '/:id',
    name: 'communityDetail',
    component: CommunityDetailView
  },
  {
    path: '/search/:keyword',
    name: 'search',
    component: SearchView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
