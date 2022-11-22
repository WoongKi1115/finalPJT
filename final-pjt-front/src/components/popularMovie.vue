<template>
  <div>
    <h1>PopularMovie</h1>
    <v-row class="d-flex justify-center">
      <v-col cols="10">
        <v-carousel
          cycle
          hide-delimiter-background
          height="700"
          class="popular-movie-carousel"
          col="10"
          style="z-index: 0"
        >
          <v-carousel-item
            style="z-index: 1"
            v-for="popularMovie in popularMovies"
            :key="popularMovie.id"
            reverse-transition="fade-transition"
            transition="fade-transition"
            ><v-hover>
              <template>
                <v-card class="mx-auto" max-width="2200" max-height="auto">
                  <v-dialog width="1800">
                    <template v-slot:activator="{ on, attrs }">
                      <div>
                        <v-img
                          v-bind="attrs"
                          v-on="on"
                          class="d-flex"
                          :src="
                            'https://image.tmdb.org/t/p/original' +
                            popularMovie.backdrop_path
                          "
                          style="object-fit: cover"
                          @click="getMovieComment(popularMovie)"
                        >
                          <v-btn
                            class="d-flex align-self-end mt-5"
                            text
                            color="white"
                          >
                            <h1>{{ popularMovie.title }}</h1>
                          </v-btn>
                        </v-img>
                      </div>
                    </template>
                    <!-- 여기부턴 모달 -->
                    <v-card>
                      <v-card-text class="pa-7 modalstyle">
                        <v-row>
                          <v-col cols="5" class="pa-0">
                            <img
                              class="modalimage"
                              :src="
                                'https://image.tmdb.org/t/p/original' +
                                popularMovie.poster_path
                              "
                            />
                          </v-col>
                          <v-col cols="7" class="pa-0" style="color: #eeeeee">
                            <div style="position: relative" class="pe-10">
                              <div
                                style="
                                  position: relative;
                                  top: 20px;
                                  width: 90%;
                                "
                              >
                                <h1>{{ popularMovie.title }}</h1>
                                <br />
                                <br />
                                <div class="d-flex justify-space-around">
                                  <div>
                                    <label for="genre">장르 : </label>
                                    <span
                                      id="genre"
                                      v-for="(
                                        genre, index
                                      ) in popularMovie.genre_ids"
                                      :key="index"
                                    >
                                      {{ genre }}&nbsp;&nbsp;&nbsp;
                                    </span>
                                  </div>
                                  <span
                                    >평점 :
                                    {{ popularMovie.vote_average }}</span
                                  >
                                  <span
                                    >개봉일 :
                                    {{ popularMovie.release_date }}</span
                                  >
                                </div>
                                <br />
                                <br />
                                <label for="overview">줄거리 : </label>
                                <span id="overview">{{
                                  popularMovie.overview
                                }}</span>
                              </div>
                              <div
                                style="
                                  border: 2px solid #e50914;
                                  border-radius: 20px;
                                  height: 50%;
                                  width: 90%;
                                  background-color: #222222;
                                  color: black;
                                  position: absolute;
                                  top: 350px;
                                "
                              >
                                <div
                                  class="
                                    d-flex
                                    justify-content-around
                                    mt-1
                                    pa-5
                                    pb-5
                                    pt-0
                                  "
                                >
                                  <div class="text-center mb-3">
                                    <span
                                      class="text-caption mr-2"
                                      style="color: white"
                                    >
                                      ({{ rating }})
                                    </span>
                                    <v-rating
                                      half-increments
                                      color="yellow"
                                      bg-color="orange-lighten-1"
                                      v-model="rating"
                                      hover
                                    ></v-rating>
                                  </div>
                                  <v-text-field
                                    @keyup.enter="
                                      createMovieComment(popularMovie)
                                    "
                                    dark
                                    class="pa-3"
                                    style="background-color: #222222"
                                    v-model="popularMovieComment"
                                    :rules="nameRules"
                                    :counter="50"
                                    label="댓글"
                                    required
                                  ></v-text-field>
                                </div>
                                <v-list-item two-line>
                                  <v-list-item-content
                                    style="text-align: left; color: #eeeeee"
                                  >
                                    <v-list-item-title
                                      class="mt-2"
                                      v-for="(comment, index) in movie_comment"
                                      :key="index"
                                    >
                                      <span
                                        style="font-size: large"
                                        class="me-10"
                                        >{{
                                          comment.username
                                        }}&nbsp;&nbsp;</span
                                      >
                                      <span
                                        >{{
                                          comment.movie_comment
                                        }}&nbsp;&nbsp;&nbsp;&nbsp;</span
                                      >
                                      <button
                                        v-show="comment.user === userId"
                                        @click="deleteComment(comment.id)"
                                      >
                                        <i class="fa-solid fa-trash-can"></i>
                                      </button>
                                      <span style="float: right">{{
                                        comment.created_at
                                          | moment("YYYY-MM-DD HH:mm:ss")
                                      }}</span>
                                      <v-divider class="mt-2"></v-divider>
                                    </v-list-item-title>
                                  </v-list-item-content>
                                </v-list-item>
                              </div>
                            </div>
                          </v-col>
                        </v-row>
                      </v-card-text>
                    </v-card>
                  </v-dialog>
                </v-card>
              </template>
            </v-hover>
          </v-carousel-item>
        </v-carousel>
      </v-col>
    </v-row>

    <!-- <p>{{ popularMovies }}</p> -->
  </div>
</template>

<script>
// import popularMovieitem from '@/components/popularMovieitem';
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";
export default {
  name: "popularMovie",
  data() {
    return {
      isModalviewed: false,
      showModal: true,
      valid: false,
      popularMovieComment: "",
      model: null,
      userId: null,
      rating: 3,
      movie_comment: null,
      pickedMovieId: null,
      isLoggedIn: false,
      nameRules: [(v) => v.length <= 50 || "댓글은 50자 이내로 작성해주세요!"],
    };
  },
  components: {
    // popularMovieitem
  },
  computed: {
    popularMovies() {
      return this.$store.state.top10Movie;
    },
  },
  methods: {
    openModal() {
      this.showModal = false;
    },
    closeModal() {
      this.showModal = true;
    },
    createMovieComment(pickedMovie) {
      const rates = this.rating;
      const movie_comment = this.popularMovieComment;
      axios({
        method: "post",
        url: `${API_URL}/api/v1/${pickedMovie.id}/moviecomment/`,
        data: { rates, movie_comment },
        headers: {
          Authorization: `Bearer ${window.localStorage.getItem("jwt")}`,
        },
      }).then(() => {
        axios({
          method: "get",
          url: `${API_URL}/api/v1/${pickedMovie.id}/moviecomment/`,
        }).then((res) => {
          this.movie_comment = res.data;
          this.pickedMovieId = pickedMovie.id;
          this.userId = this.$store.state.loginUser.id;
        });
        this.popularMovieComment = "";
        this.rating = 3;
      }).catch(() =>{
        alert('로그인해!')
        this.$router.push("login");

      })
    },
    getMovieComment(pickedMovie) {
      this.popularMovieComment = "";
      this.rating = 3;
      axios({
        method: "get",
        url: `${API_URL}/api/v1/${pickedMovie.id}/moviecomment/`,
      }).then((res) => {
        this.movie_comment = res.data;
        this.pickedMovieId = pickedMovie.id;
        this.userId = this.$store.state.loginUser.id;
      });
    },
    deleteComment(pickedComment) {
      axios({
        method: "delete",
        url: `${API_URL}/api/v1/${pickedComment}/del/`,
        headers: {
          Authorization: `Bearer ${window.localStorage.getItem("jwt")}`,
        },
      }).then(() => {
        axios({
          method: "get",
          url: `${API_URL}/api/v1/${this.pickedMovieId}/moviecomment/`,
        }).then((res) => {
          this.movie_comment = res.data;
        });
      });
    },
    isLogin() {
      if (window.localStorage.getItem("jwt")) {
        this.isLoggedIn = true;
      } else {
        this.isLoggedIn = false;
      }
    },
  },
  created() {
    this.isLogin();
  },
};
</script>

<style>
.popular-movie-carousel {
  height: 1000px;
  width: 1777px;
}

.modalimg {
  width: 500px;
}
.modalimage {
  width: 600px;
  height: 810px;
  border-radius: 10px;
  object-fit: fit;
  display: block;
}
</style>