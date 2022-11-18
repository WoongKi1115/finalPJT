import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    movies: null,
    top10Movie: null,
    recenteMovie: null,
  },
  getters: {
    // getRecent(state){
    //   const recentSorted = state.movies.sort(function(a, b){
    //     a = new Date(a.release_date);
    //     b = new Date(b.release_date);
    //     return a>b ? -1 : a<b ? 1 : 0;
    //   })
    //   recentSorted.splice(20)
    //   return recentSorted
    // }
  },
  mutations: {},
  actions: {},
  modules: {},
});
