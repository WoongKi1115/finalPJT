<template>
  <div>
    <h1>{{ randomGenre3 }}</h1>
    <v-sheet class="mx-auto" max-width="1800">
      <v-slide-group
        style="height: 550px"
        class="pa-4 recentmovie"
        active-class="success"
        show-arrows
      ><template v-slot:next>
            <v-icon color="white" large>fa-light fa-chevron-right</v-icon>
          </template>
              <template v-slot:prev>
            <v-icon color="white" large>fa-light fa-angle-left</v-icon>
            </template>
        <v-slide-item
          class="mt-6"
          v-for="(randomMovie3, index) in randomGenreMovies3"
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
                      randomMovie3.poster_path
                    "
                    height="440"
                    @click="getMovieComment(randomMovie3)"
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
                            randomMovie3.poster_path
                          "
                        />
                      </v-col>
                      <v-col cols="7" class="pa-0" style="color: #eeeeee">
                        <div style="position: relative" class="pe-10">
                          <div
                            style="position: relative; top: 20px; width: 90%"
                          >
                            <h2>{{ randomMovie3.title }}</h2>
                            <br />
                            <br />
                            <v-row>
                              <v-col cols="9" style="font-size: medium">
                                <div class="d-flex">
                                  <label for="genre">장르 :&nbsp;</label>
                                  <span
                                    id="genre"
                                    v-for="(
                                      genre, index
                                    ) in getGenre(randomMovie3)"
                                    :key="index"
                                  >
                                    {{ genre }}&nbsp;&nbsp;&nbsp;
                                  </span>
                                </div>
                                <div class="d-flex my-2">
                                  개봉일 : {{ randomMovie3.release_date }}
                                </div>
                                <div class="d-flex">
                                  감독 : {{ randomMovie3.director }}
                                </div>
                                <div
                                  class="d-flex my-2"
                                  style="text-align: left"
                                >
                                  주연 :
                                  {{
                                    randomMovie3.actors
                                      .replace(/\[/g, "")
                                      .replace(/\]/g, "")
                                      .replace(/\'/g, "")
                                  }}
                                </div>
                                <div class="d-flex">
                                  평점 :
                                  <star-rating
                                    class="mx-3"
                                    :increment="0.01"
                                    :rating="averageStar"
                                    :read-only="true"
                                    :show-rating="false"
                                    :star-size="20"
                                  ></star-rating
                                  >{{ averageRate }}
                                </div>
                              </v-col>
                            </v-row>
                            <v-card height="150" dark class="ms-6 mt-3 overview overflow-auto">
                              <v-card-text  dark>
                                {{ randomMovie3.overview }}
                              </v-card-text>
                            </v-card>
                          </div>
                          <div
                            style="
                              height: 50%;
                              width: 90%;
                              background-color: #222222;
                              color: black;
                              position: absolute;
                              top: 420px;
                            "
                          >
                            <div
                              style="
                                border: 2px solid #e50914;
                                border-radius: 20px;
                              "
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
                                  ({{ rating * 2 }})
                                </span>
                                <star-rating
                                  :increment="0.5"
                                  v-model="rating"
                                  :star-size="35"
                                  :show-rating="false"
                                  :glow="5"
                                  :animate="true"
                                ></star-rating>
                              </div>
                              <v-text-field
                                @keyup.enter="createMovieComment(randomMovie3)"
                                dark
                                class="pa-3"
                                style="background-color: #222222"
                                v-model="randomMovie3Comment"
                                :rules="nameRules"
                                :counter="50"
                                label="댓글"
                                required
                              ></v-text-field>
                              <v-btn
                                @click="createMovieComment(randomMovie3)"
                                class="align-self-center"
                              >
                                입력
                              </v-btn>
                            </div>
                            <v-list-item two-line>
                              <v-list-item-content style="color: #eeeeee">
                                <v-list-item-title
                                  class="mt-2"
                                  style="display: float"
                                  v-for="(comment, index) in calData"
                                  :key="index"
                                >
                                  <div>
                                    <div
                                      style="
                                        font-size: large;
                                        float: left;
                                        width: 5%;
                                      "
                                      class="me-10"
                                    >
                                      {{ comment.username }}&nbsp;&nbsp;
                                    </div>
                                    <div style="float: left; width: 20%">
                                      <star-rating
                                        :increment="0.5"
                                        :rating="comment.rates"
                                        :read-only="true"
                                        :show-rating="false"
                                        :star-size="20"
                                      ></star-rating>
                                    </div>
                                    <div
                                      style="float: left; width: 45%"
                                      class="mt-1"
                                    >
                                      {{
                                        comment.movie_comment
                                      }}&nbsp;&nbsp;&nbsp;&nbsp;
                                      <button
                                        v-show="comment.user === userId"
                                        @click="deleteComment(comment.id)"
                                      >
                                        <i class="fa-solid fa-trash-can"></i>
                                      </button>
                                    </div>
                                    <div
                                      style="float: left; width: 15%"
                                      class="mt-1"
                                    >
                                      {{
                                        comment.created_at
                                          | moment("YYYY-MM-DD HH:mm:ss")
                                      }}
                                    </div>
                                  </div>
                                  <br />
                                  <v-divider class="mt-2" dark></v-divider>
                                </v-list-item-title>
                              </v-list-item-content>
                            </v-list-item>
                            <div
                              class="text-center"
                              v-show="countComment(movie_comment)"
                              style="align-item-end"
                            >
                              <v-pagination
                                v-model="curPageNum"
                                :length="numOfPages"
                              ></v-pagination>
                            </div>
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
import StarRating from "vue-star-rating";
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";
import _ from "lodash";

export default {
  name: "genreMovieitem2",
  components: {
    StarRating,
  },
  data() {
    return {
      dataPerPage: 5,
      curPageNum: 1,
      valid: false,
      randomMovie3Comment: "",
      model: null,
      userId: null,
      rating: 3,
      movie_comment: [],
      pickedMovieId: null,
      nameRules: [(v) => v.length <= 50 || "댓글은 50자 이내로 작성해주세요!"],
      averageRate: null,
      averageStar: null,
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
      genres2: {
        28: "Action",
        12: "Adventure",
        16: "Animation",
        35: "Comedy",
        80: "Crime",
        99: "Documentary",
        18: "Drama",
        10751: "Family",
        14: "Fantasy",
        36: "History",
        27: "Horror",
        10402: "Music",
        9648: "Mystery",
        10749: "Romance",
        878: "SF",
        10770: "TV Movie",
        53: "Thriller",
        10752: "War",
        37: "Western",
      },
    };
  },
  computed: {
    randomGenreMovies3() {
      const pickedMovies = _.sampleSize(
        this.$store.state.randomGenreMovies3,
        20
      );
      return pickedMovies;
    },
    randomGenre3() {
      const genresId = this.$store.state.randomGenre3;
      return this.genres2[genresId];
    },
    startOffset() {
      return (this.curPageNum - 1) * this.dataPerPage;
    },
    endOffset() {
      return this.startOffset + this.dataPerPage;
    },
    numOfPages() {
      return Math.ceil(this.movie_comment.length / this.dataPerPage);
    },
    calData() {
      return this.movie_comment.slice(this.startOffset, this.endOffset);
    },
  },

  methods: {
     getGenre(rendommovie) {
      const genresDic = this.genres;
        let newGenre = [];
        for (let movieGenre of rendommovie.genre_ids) {
          newGenre.push(genresDic[movieGenre]);
        }
        return newGenre
    },
    countComment(comment) {
      if (comment.length < 1) {
        return false;
      } else {
        return true;
      }
    },
    getAvg() {
      let summ = 0;
      for (const rate in this.movie_comment) {
        summ += this.movie_comment[rate].rates * 2;
      }
      let result = summ / this.movie_comment.length;
      if (this.movie_comment.length === 0) {
        this.averageRate = 0;
        this.averageStar = 0;
        return;
      }
      this.averageRate = result.toFixed(1) * 1;
      this.averageStar = (result.toFixed(1) / 2) * 1;
    },
    createMovieComment(pickedMovie) {
      const rates = this.rating;
      const movie_comment = this.randomMovie3Comment;
      if (movie_comment == "") {
        alert("글을 입력하세요");
        return;
      }
      axios({
        method: "post",
        url: `${API_URL}/api/v1/${pickedMovie.id}/moviecomment/`,
        data: { rates, movie_comment },
        headers: {
          Authorization: `Bearer ${window.localStorage.getItem("jwt")}`,
        },
      })
        .then(() => {
          axios({
            method: "get",
            url: `${API_URL}/api/v1/${pickedMovie.id}/moviecomment/`,
          }).then((res) => {
            this.movie_comment = res.data;
            this.pickedMovieId = pickedMovie.id;
            this.userId = this.$store.state.loginUser.id;
            this.getAvg();
          });

          this.randomMovie3Comment = "";
          this.rating = 3;
        })
        .catch(() => {
          alert("로그인해!");
          this.$router.push("login");
        });
    },
    getMovieComment(pickedMovie) {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/${pickedMovie.id}/moviecomment/`,
      }).then((res) => {
        this.movie_comment = res.data;
        this.pickedMovieId = pickedMovie.id;
        this.userId = this.$store.state.loginUser.id;
        this.getAvg();
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
          this.getAvg();
        });
      });
    },
  },
  created() {},
};
</script>

<style>
details {
  margin-bottom: 1rem;
  background-color: transparent;
}

details > summary {
  background-color: transparent;
  padding: 1rem;
  cursor: pointer;
}

details > summary::-webkit-details-marker {
  color: transparent;
  transform: rotate3d(0, 0, 1, 90deg);
  transition: transform 0.25s;
  background-color: transparent;
}

details[open] > summary::-webkit-details-marker {
  transform: rotate3d(0, 0, 1, 180deg);
}

details[open] > summary {
  background-color: transparent;
}

details[open] > summary ~ * {
  animation: reveal 0.5s;
}

@keyframes reveal {
  from {
    opacity: 0;
    transform: translate3d(0, -10px, 0);
  }

  to {
    opacity: 1;
    transform: translate3d(0, 0, 0);
  }
}
</style>