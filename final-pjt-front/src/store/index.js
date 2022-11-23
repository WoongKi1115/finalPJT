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
    randomGenreMovies1:null,
    randomGenre1:null,
    randomGenreMovies2:null,
    randomGenre2:null,
    randomGenreMovies3:null,
    randomGenre3:null,
  },
  getters: {
  },
  mutations: {},
  actions: {},
  modules: {},
});
