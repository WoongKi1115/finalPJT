<template>
  <v-app class="v-app">
    <v-app-bar app color="#E50914" >
      <div class="d-flex align-center">
        <!-- 로고 들어갈 자리 -->
        <router-link :to="{ name: 'mainpage' }" class="white--text">
          <img style="width:60px" src="@/assets/1212.jpg" alt="로고자리" />
        </router-link>
      </div>
      <v-spacer> </v-spacer>
      <div><v-text-field
        v-model="searchKeyword"
        append-icon="mdi-magnify"
        label="Search"
        single-line
        hide-details
        dark
        class="ms-15"
        @click:append="doSearch()"
        @keyup.enter="doSearch()"
      ></v-text-field></div>
      <div>
        <router-link style="text-decoration:none"  :to="{ name: 'community' }" class="white--text mx-3"
          >Community</router-link
        >
        <router-link style="text-decoration:none" :to="{ name: 'moviepick' }" class="white--text mx-3"
          >Recommend</router-link
        >
        <router-link
        style="text-decoration:none"
          :to="{ name: 'login' }"
          class="white--text mx-3"
          v-show="!this.isLoggedIn"
          >Login</router-link
        >
        <button v-show="this.isLoggedIn" @click="logOut" style="text-decoration:none; color:white">Logout</button>
        <router-link  v-show="!this.isLoggedIn" style="text-decoration:none" :to="{ name: 'signup' }" class="white--text mx-3"
          >Signup</router-link
        >
      </div>
    </v-app-bar>

    <v-main class="v-mains mt-5">
      <router-view :key="$route.fullPath" @login="isLoggedIn = true" />
    </v-main>
    
  </v-app>
</template>

<script>
import axios from "axios";
import _ from "lodash"
const API_URL = "http://127.0.0.1:8000";

export default {
  name: "App",

  data() {
    return {
      
      searchKeyword:null,
      isLoggedIn: false,
      movies: [],
      popularMovies: null,
      recenteMovies: null,
      randomMovies: null,
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
      calssifiedGenres:{
        28: [],
        12: [],
        16: [],
        35: [],
        80: [],
        99: [],
        18: [],
        10751: [],
        14: [],
        36: [],
        27: [],
        10402: [],
        9648: [],
        10749: [],
        878: [],
        10770: [],
        53: [],
        10752: [],
        37: [],


      }
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
          this.$store.state.unprocessedMovies = _.cloneDeep(this.movies)
          this.getGenre();
          this.$store.state.movies = this.movies;
          this.getPopular();
          this.$store.state.top10Movie = this.popularMovies;
          this.getRecent();
          this.$store.state.recenteMovie = this.recenteMovies
          this.classifyGenre()
          this.getArticle();
          this.getRandomGenre()
         
        })
        .then(() => {
          
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
      this.popularMovies = _.cloneDeep(this.$store.state.movies)
      const popularSorted = this.popularMovies.sort(function (a, b) {
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
    getRecent(){
      this.recenteMovies = _.cloneDeep(this.$store.state.movies)
      const recentSorted = this.recenteMovies.sort(function(a, b){
        a = new Date(a.release_date);
        b = new Date(b.release_date);
        return a>b ? -1 : a<b ? 1 : 0;
      })
      recentSorted.splice(20)
      this.recenteMovies = recentSorted
    },
    classifyGenre(){
      const unprocessed =  _.cloneDeep(this.$store.state.unprocessedMovies)
      // console.log(unprocessed)
      for (let movie of unprocessed) {
        for (let genre of movie.genre_ids){
          this.calssifiedGenres[genre].push(movie)
        }
      }
      this.$store.state.classifiedMovie = this.calssifiedGenres
    },
    getRandomGenre() {
		const genres = [12, 14, 16, 18, 27, 28, 35, 36, 37, 53, 80, 99, 878, 9648, 10402, 10749, 10751, 10752, 10770]
    const randomGenre = _.samplesize(genres, 3)
    console.log(randomGenre)
    console.log(randomGenre[0])
    this.$store.state.randomGenre1 = randomGenre[0]
    this.$store.state.randomGenre2 = randomGenre[1]
    this.$store.state.randomGenre3 = randomGenre[2]
    this.$store.state.randomGenreMovies1 = this.calssifiedGenres[randomGenre[0]]
    this.$store.state.randomGenreMovies2 = this.calssifiedGenres[randomGenre[1]]
    this.$store.state.randomGenreMovies3 = this.calssifiedGenres[randomGenre[2]]
    },
    getArticle() {
      axios({
        method: "get",
        url: `${API_URL}/community/`,
      })
        .then((res) => {
          this.$store.state.articles = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    doSearch() {
      const keyword = this.searchKeyword
      this.$router.push({ name: "search", params: {keyword} });
      this.searchKeyword = null
    },

    // 로그인쪽
    isLogin() {
      if (window.localStorage.getItem("jwt")) {
        this.isLoggedIn = true;
        axios({
          method: "get",
          url: "http://127.0.0.1:8000/accounts/whoareyou/",
          headers:{
            Authorization: `Bearer ${window.localStorage.getItem('jwt')}`
          }
        })
        .then((res) =>{
          this.$store.state.loginUser = res.data
        })
      } else {
        this.isLoggedIn = false;
      }
    },
    logOut() {
      window.localStorage.removeItem("jwt");
      this.$router.push({ name: "login" });
      this.isLoggedIn = false;
      this.$store.state.loginUser = null
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
.v-main {
  background-color: #000000;
  color: white;

}
</style>
