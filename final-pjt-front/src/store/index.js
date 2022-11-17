import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    movies: null,
  },
  getters: {
    getPopular(state) {
      const popularSorted = state.movies.sort(function (a, b) {
        if (b.popularity > a.popularity) {
          return 1;
        }
        if (b.popularity < a.popularity) {
          return -1;
        }
        // a must be equal to b
        return 0;
      });
      popularSorted.splice(10)
      return popularSorted
    },
    getRecent(state){
      const recentSorted = state.movies.sort(function(a, b){
        a = new Date(a.release_date);
        b = new Date(b.release_date);
        return a>b ? -1 : a<b ? 1 : 0;
      })
      recentSorted.splice(20)
      return recentSorted
    }
  },
  mutations: {},
  actions: {},
  modules: {},
});
