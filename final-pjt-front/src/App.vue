<template>
  <v-app class="v-app">
    <v-app-bar app color="primary" dark>
      <div class="d-flex align-center">
        <!-- 로고 들어갈 자리 -->
        <router-link :to="{ name: 'mainpage' }" class="white--text">
          <img src="" alt="로고자리" />
        </router-link>
      </div>

      <v-spacer> </v-spacer>
      <div>
        <router-link :to="{ name: 'community' }" class="white--text mx-3"
          >Community</router-link
        >
        <router-link :to="{ name: 'moviepick' }" class="white--text mx-3"
          >추천</router-link
        >
        <router-link
          :to="{ name: 'login' }"
          class="white--text mx-3"
          v-show="!this.isLoggedIn"
          >Login</router-link
        >
        <button v-show="this.isLoggedIn" @click="logOut">Loggout</button>
        <router-link :to="{ name: 'signup' }" class="white--text mx-3"
          >회원가입</router-link
        >
      </div>
    </v-app-bar>

    <v-main>
      <router-view @login="isLoggedIn = true" />
    </v-main>
  </v-app>
</template>

<script>
import axios from "axios";
export default {
  name: "App",

  data() {
    return {
      isLoggedIn: false,
      movies: [],
      popularMovies: null,
      genres: {
        28: "액션",
        12: "모험",
        16: "애니메이션",
        35: "코미디",
        80: "범죄",
        99: "다큐멘터리",
        18: "드라마",
        10751: "가족",
        14: "판타지",
        36: "역사",
        27: "공포",
        10402: "음악",
        9648: "미스터리",
        10749: "로맨스",
        878: "SF",
        10770: "TV 영화",
        53: "스릴러",
        10752: "전쟁",
        37: "서부",
      },
    };
  },
  methods: {
    getMovies() {
      axios({
        method: "get",
        url: "http://127.0.0.1:8000/api/v1/",
      })
        .then((res) => {
          this.movies = res.data;
          this.getGenre();
          this.$store.state.movies = this.movies;
          this.getPopular();
          this.$store.state.top10Movie = this.popularMovies;
          // console.log(this.movies)
          // branch test
          // console.log(this.recentMovies)
          // console.log(this.$store.state.movies)
          // console.log(this.$store.getters.getPopular)
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getGenre() {
      // const movieListLen= movies.length
      const genresDic = this.genres;
      for (let movie of this.movies) {
        let newGenre = [];
        for (let movieGenre of movie.genre_ids) {
          newGenre.push(genresDic[movieGenre]);
        }
        movie.genre_ids = newGenre;
      }
    },
    getPopular() {
      const popularSorted = this.$store.state.movies.sort(function (a, b) {
        if (b.popularity > a.popularity) {
          return 1;
        }
        if (b.popularity < a.popularity) {
          return -1;
        }
        return 0;
      });
      popularSorted.splice(10);
      this.popularMovies = popularSorted;
    },
    isLogin() {
      if (window.localStorage.getItem("jwt")) {
        this.isLoggedIn = true;
      } else {
        this.isLoggedIn = false;
      }
    },
    logOut() {
      window.localStorage.removeItem("jwt");
      this.$router.push({ name: "login" });
      this.isLoggedIn = false;
    },
  },

  created() {
    this.getMovies();
    this.isLogin();
  },
};
</script>

<style>
.v-app {
  text-align: center;
}
</style>
