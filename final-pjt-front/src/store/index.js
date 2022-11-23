import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    articles:null,
    unprocessedMovies:null,
    movies: null,
    top10Movie: null,
    recenteMovie: null,
    classifiedMovie:null,
    loginUser: null,
    randomGenreMovies:null
  },
  getters: {
  },
  mutations: {},
  actions: {},
  modules: {},
});
