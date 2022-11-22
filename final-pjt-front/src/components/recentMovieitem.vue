<template>
  <div>
    <h1>RecentMovie</h1>
    <v-sheet class="mx-auto" max-width="1800">
      <v-slide-group
        dark
        style="height: 550px"
        class="pa-4 recentmovie"
        active-class="success"
        show-arrows
      >
        <v-slide-item
          class="mt-6"
          v-for="(recentmovie, index) in recenteMovies"
          :key="index"
        >
          <v-card class="ma-4 pa-1 posterimg" height="450" width="300">
            <div class="text-center">
              <v-dialog width="1800">
                <template v-slot:activator="{ on, attrs }">
                  <v-img
                    v-bind="attrs"
                    v-on="on"
                    :src="
                      'https://image.tmdb.org/t/p/original' +
                      recentmovie.poster_path
                    "
                    height="440"
                    @click="getMovieComment(recentmovie)"
                  >
                  </v-img>
                </template>

                <v-card>
                  <v-card-text class="pa-7 modalstyle">
                    <v-row>
                      <v-col cols="5" class="pa-0">
                        <img
                          class="modalimage"
                          :src="
                            'https://image.tmdb.org/t/p/original' +
                            recentmovie.poster_path
                          "
                        />
                      </v-col>
                      <v-col cols="7" class="pa-0" style="color: #eeeeee">
                        <div style="position: relative" class="pe-10">
                          <div
                            style="position: relative; top: 20px; width: 90%"
                          >
                            <h1>{{ recentmovie.title }}</h1>
                            <br />
                            <br />
                            <div class="d-flex justify-space-around">
                              <div>
                                <label for="genre">장르 : </label>
                                <span
                                  id="genre"
                                  v-for="(
                                    genre, index
                                  ) in recentmovie.genre_ids"
                                  :key="index"
                                >
                                  {{ genre }}&nbsp;&nbsp;&nbsp;
                                </span>
                              </div>
                              <span>평점 : {{ recentmovie.vote_average }}</span>
                              <span
                                >개봉일 : {{ recentmovie.release_date }}</span
                              >
                            </div>
                            <br />
                            <br />
                            <label for="overview">줄거리 : </label>
                            <span id="overview">{{
                              recentmovie.overview
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
                                @keyup.enter="createMovieComment(recentmovie)"
                                dark
                                class="pa-3"
                                style="background-color: #222222"
                                v-model="recentMovieComment"
                                :rules="nameRules"
                                :counter="50"
                                label="댓글"
                                required
                              ></v-text-field>
                            </div>
                            <v-list-item two-line>
                              <v-list-item-content style="text-align: left; color: #eeeeee;">
                                <v-list-item-title
                                  class="mt-2"
                                  v-for="(comment, index) in movie_comment"
                                  :key="index"
                                >
                                  <span style="font-size: large" class="me-10"
                                    >{{ comment.username }}&nbsp;&nbsp;</span
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
            </div>
          </v-card>
        </v-slide-item>
      </v-slide-group>
    </v-sheet>
  </div>
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";
export default {
  name: "recentMovieitem",
  data() {
    return {
      valid: false,
      recentMovieComment: "",
      model: null,
      userId: null,
      rating: 3,
      movie_comment: null,
      pickedMovieId:null,
      nameRules: [(v) => v.length <= 50 || "댓글은 50자 이내로 작성해주세요!"],
    };
  },
  computed: {
    recenteMovies() {
      return this.$store.state.recenteMovie;
    },
  },
  methods: {
    createMovieComment(pickedMovie) {
      const rates = this.rating;
      const movie_comment = this.recentMovieComment;
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
          this.pickedMovieId = pickedMovie.id
          this.userId = this.$store.state.loginUser.id;
        });
        this.recentMovieComment = "";
        this.rating = 3;
      });
    },
    getMovieComment(pickedMovie) {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/${pickedMovie.id}/moviecomment/`,
      }).then((res) => {
        this.movie_comment = res.data;
        this.pickedMovieId = pickedMovie.id
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
      })
      .then(() => {
        axios({
          method: "get",
          url: `${API_URL}/api/v1/${this.pickedMovieId}/moviecomment/`,
        }).then((res) => {
          this.movie_comment = res.data;
      })})

    }
  },
};
</script>

<style>
.recentmovie {
  background-color: black;
}
#next-icon {
  color: rgb(234, 10, 10) !important;
}
.posterimg:hover {
  transform: scale(1.1);
}
.modalstyle {
  background-color: #222222;
  color: #eeeeee;
}
</style>
