import Vue from 'vue'
import VueRouter from 'vue-router'
import MainPageView from '@/views/MainPageView'
import MoviePickView from '@/views/MoviePickView'
import LoginPageView from '@/views/LoginPageView'
import SignupPageView from '@/views/SignupPageView'
import CommunityView from '@/views/CommunityView'
import createArticle from '@/views/createArticle'
import MyPageView from '@/views/MyPageView'
import CommunityDetailView from '@/views/CommunityDetailView'

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
    path: '/mypage',
    name: 'mypage',
    component: MyPageView
  },
  {
    path: '/:id',
    name: 'communityDetail',
    component: CommunityDetailView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
