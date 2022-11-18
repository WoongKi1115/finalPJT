import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    
    unprocessedMovies:null,
    movies: null,
    top10Movie: null,
    recenteMovie: null,
    classifiedMovie:null,
  },
  getters: {
  },
  mutations: {},
  actions: {},
  modules: {},
});
