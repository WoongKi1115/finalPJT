<template>
  <div class="recommendpage">
    <h1>영화 추천해주는 페이지</h1>
    <h3>설명란</h3>
    <v-row justify="center" class="mt-5">
      <v-dialog
        v-model="dialog"
        hide-overlay
        height="900px"
        width="700px"
        transition="dialog-bottom-transition"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            color="#E50914"
            dark
            v-bind="attrs"
            v-on="on"
            @click="resetMoods"
          >
            추천받으러가기
          </v-btn>
        </template>
        <v-card dark>
          <v-toolbar dark color="#E50914" class="mb-5">
            <v-btn icon dark @click="dialog = false">
              <v-icon>mdi-close</v-icon>
            </v-btn>
            <v-toolbar-title
              >5가지 상태를 고르고 추천받기 버튼을 눌러주세요!</v-toolbar-title
            >
            <v-spacer></v-spacer>
            <v-toolbar-items>
              <v-btn dark text @click="[save()]" class="my-font2">
                추천받기
              </v-btn>
            </v-toolbar-items>
          </v-toolbar>
          <v-list-item color="#E50914">
            <v-row class="d-flex justify-space-around mb-4">
              <v-col>
                <v-btn
                  @click="clicked.clicked1 = !clicked.clicked1"
                  :color="clicked.clicked1 ? '#E50914' : '#FFCDD2'"
                  :style="clicked.clicked1 ? 'color:white' : 'color:black'"
                  class="my-font"
                >
                  신나는😁
                </v-btn>
              </v-col>
              <v-col>
                <v-btn
                  @click="clicked.clicked2 = !clicked.clicked2"
                  :color="clicked.clicked2 ? '#E50914' : '#FFCDD2'"
                  :style="clicked.clicked2 ? 'color:white' : 'color:black'"
                  class="my-font"
                >
                  활기찬😄
                </v-btn>
              </v-col>
              <v-col>
                <v-btn
                  @click="clicked.clicked3 = !clicked.clicked3"
                  :color="clicked.clicked3 ? '#E50914' : '#FFCDD2'"
                  :style="clicked.clicked3 ? 'color:white' : 'color:black'"
                  class="my-font"
                >
                  지루한😑
                </v-btn>
              </v-col>
              <v-col>
                <v-btn
                  @click="clicked.clicked4 = !clicked.clicked4"
                  :color="clicked.clicked4 ? '#E50914' : '#FFCDD2'"
                  :style="clicked.clicked4 ? 'color:white' : 'color:black'"
                  class="my-font"
                >
                  자랑스러운😃
                </v-btn>
              </v-col>
              <v-col>
                <v-btn
                  @click="clicked.clicked5 = !clicked.clicked5"
                  :color="clicked.clicked5 ? '#E50914' : '#FFCDD2'"
                  :style="clicked.clicked5 ? 'color:white' : 'color:black'"
                  class="my-font"
                >
                  자신감넘치는🤗
                </v-btn>
              </v-col>
              <v-col>
                <v-btn
                  @click="clicked.clicked6 = !clicked.clicked6"
                  :color="clicked.clicked6 ? '#E50914' : '#FFCDD2'"
                  :style="clicked.clicked6 ? 'color:white' : 'color:black'"
                  class="my-font"
                >
                  답답한😤
                </v-btn>
              </v-col>
              <v-col>
                <v-btn
                  @click="clicked.clicked7 = !clicked.clicked7"
                  :color="clicked.clicked7 ? '#E50914' : '#FFCDD2'"
                  :style="clicked.clicked7 ? 'color:white' : 'color:black'"
                  class="my-font"
                >
                  우울한😥
                </v-btn>
              </v-col>
              <v-col>
                <v-btn
                  @click="clicked.clicked8 = !clicked.clicked8"
                  :color="clicked.clicked8 ? '#E50914' : '#FFCDD2'"
                  :style="clicked.clicked8 ? 'color:white' : 'color:black'"
                  class="my-font"
                >
                  웃음이필요한😂
                </v-btn>
              </v-col>
              <v-col>
                <v-btn
                  @click="clicked.clicked9 = !clicked.clicked9"
                  :color="clicked.clicked9 ? '#E50914' : '#FFCDD2'"
                  :style="clicked.clicked9 ? 'color:white' : 'color:black'"
                  class="my-font"
                >
                  짜증나는😡
                </v-btn>
              </v-col>
              <v-col>
                <v-btn
                  @click="clicked.clicked10 = !clicked.clicked10"
                  :color="clicked.clicked10 ? '#E50914' : '#FFCDD2'"
                  :style="clicked.clicked10 ? 'color:white' : 'color:black'"
                  class="my-font"
                >
                  통쾌한😋
                </v-btn>
              </v-col>
              <v-col>
                <v-btn
                  @click="clicked.clicked11 = !clicked.clicked11"
                  :color="clicked.clicked11 ? '#E50914' : '#FFCDD2'"
                  :style="clicked.clicked11 ? 'color:white' : 'color:black'"
                  class="my-font"
                >
                  억울한😯
                </v-btn>
              </v-col>
              <v-col>
                <v-btn
                  @click="clicked.clicked12 = !clicked.clicked12"
                  :color="clicked.clicked12 ? '#E50914' : '#FFCDD2'"
                  :style="clicked.clicked12 ? 'color:white' : 'color:black'"
                  class="my-font"
                >
                  행복한😊
                </v-btn>
              </v-col>
              <v-col>
                <v-btn
                  @click="clicked.clicked13 = !clicked.clicked13"
                  :color="clicked.clicked13 ? '#E50914' : '#FFCDD2'"
                  :style="clicked.clicked13 ? 'color:white' : 'color:black'"
                  class="my-font"
                >
                  편안한😙
                </v-btn>
              </v-col>
              <v-col>
                <v-btn
                  @click="clicked.clicked14 = !clicked.clicked14"
                  :color="clicked.clicked14 ? '#E50914' : '#FFCDD2'"
                  :style="clicked.clicked14 ? 'color:white' : 'color:black'"
                  class="my-font"
                >
                  속상한😫
                </v-btn>
              </v-col>
              <v-col>
                <v-btn
                  @click="clicked.clicked15 = !clicked.clicked15"
                  :color="clicked.clicked15 ? '#E50914' : '#FFCDD2'"
                  :style="clicked.clicked15 ? 'color:white' : 'color:black'"
                  class="my-font"
                >
                  몽환적인🙃
                </v-btn>
              </v-col>
              <v-col>
                <v-btn
                  @click="clicked.clicked16 = !clicked.clicked16"
                  :color="clicked.clicked16 ? '#E50914' : '#FFCDD2'"
                  :style="clicked.clicked16 ? 'color:white' : 'color:black'"
                  class="my-font"
                >
                  현실에서 벗어나고픈🤪
                </v-btn>
              </v-col>
              <v-col>
                <v-btn
                  @click="clicked.clicked17 = !clicked.clicked17"
                  :color="clicked.clicked17 ? '#E50914' : '#FFCDD2'"
                  :style="clicked.clicked17 ? 'color:white' : 'color:black'"
                  class="my-font"
                >
                  지긋지긋한😩
                </v-btn>
              </v-col>
              <v-col>
                <v-btn
                  @click="clicked.clicked18 = !clicked.clicked18"
                  :color="clicked.clicked18 ? '#E50914' : '#FFCDD2'"
                  :style="clicked.clicked18 ? 'color:white' : 'color:black'"
                  class="my-font"
                >
                  설레는😚
                </v-btn>
              </v-col>
              <v-col>
                <v-btn
                  @click="clicked.clicked19 = !clicked.clicked19"
                  :color="clicked.clicked19 ? '#E50914' : '#FFCDD2'"
                  :style="clicked.clicked19 ? 'color:white' : 'color:black'"
                  class="my-font"
                >
                  외로운😶
                </v-btn>
              </v-col>
              <v-col>
                <v-btn
                  @click="clicked.clicked20 = !clicked.clicked20"
                  :color="clicked.clicked20 ? '#E50914' : '#FFCDD2'"
                  :style="clicked.clicked20 ? 'color:white' : 'color:black'"
                  class="my-font"
                >
                  허전한😮
                </v-btn>
              </v-col>
              <v-col>
                <v-btn
                  @click="clicked.clicked21 = !clicked.clicked21"
                  :color="clicked.clicked21 ? '#E50914' : '#FFCDD2'"
                  :style="clicked.clicked21 ? 'color:white' : 'color:black'"
                  class="my-font"
                >
                  더운🥵
                </v-btn>
              </v-col>
              <v-col>
                <v-btn
                  @click="clicked.clicked22 = !clicked.clicked22"
                  :color="clicked.clicked22 ? '#E50914' : '#FFCDD2'"
                  :style="clicked.clicked22 ? 'color:white' : 'color:black'"
                  class="my-font"
                >
                  흥분되는😲
                </v-btn>
              </v-col>
            </v-row>
          </v-list-item>
        </v-card>
      </v-dialog>
    </v-row>
    <br />
    <br />
    <v-sheet class="mx-auto" max-width="1800">
      <v-slide-group
        class="pa-4 recommendmovie"
        active-class="success"
        show-arrows
        dark
      >
        <v-slide-item v-for="(rcdMovie, index) in recommendMovie" :key="index">
          <v-card class="ma-4 pa-1" height="450" width="300">
            <div class="text-center">
              <v-dialog width="1800">
                <template v-slot:activator="{ on, attrs }">
                  <v-img
                    height="440"
                    v-bind="attrs"
                    v-on="on"
                    :src="
                      'https://image.tmdb.org/t/p/original' +
                      rcdMovie.poster_path
                    "
                    @click="getMovieComment(rcdMovie)"
                  >
                  </v-img>
                </template>

                <v-card>
                  <v-card-text class="pa-7 modalstyle">
                    <v-row>
                      <v-col cols="5" class="pa-0">
                        <v-img
                          class="modalimage"
                          :src="
                            'https://image.tmdb.org/t/p/original' +
                            rcdMovie.poster_path
                          "
                        ></v-img>
                      </v-col>
                      <v-col cols="7" class="pa-0" style="color: #eeeeee">
                        <div style="position: relative" class="pe-10">
                          <div
                            style="position: relative; top: 20px; width: 90%"
                          >
                            <h1>{{ rcdMovie.title }}</h1>
                            <br />
                            <br />
                            <v-row>
                              <v-col cols="6" style="font-size: medium">
                                <div class="d-flex">
                                  <label for="genre">장르 : &nbsp;</label>
                                  <span
                                    id="genre"
                                    v-for="(genre, index) in rcdMovie.genre_ids"
                                    :key="index"
                                  >
                                    {{ genre }}&nbsp;&nbsp;&nbsp;
                                  </span>
                                </div>
                                <div class="d-flex my-2">
                                  개봉일 : {{ rcdMovie.release_date }}
                                </div>
                                <div class="d-flex">
                                  감독 : {{ rcdMovie.director }}
                                </div>
                                <div
                                  class="d-flex my-2"
                                  style="text-align: left"
                                >
                                  주연 :
                                  {{
                                    rcdMovie.actors
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
                            <br />
                            <br />
                            <label
                              for="overview"
                              style="font-size: medium; text-align: left"
                              >줄거리 :
                            </label>
                            <span
                              id="overview"
                              style="
                                font-size: medium;
                                text-align: left;
                                line-height: 180%;
                              "
                              >{{ rcdMovie.overview }}</span
                            >
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
                                @keyup.enter="createMovieComment(rcdMovie)"
                                dark
                                class="pa-3"
                                style="background-color: #222222"
                                v-model="recentMovieComment"
                                :rules="nameRules"
                                :counter="50"
                                label="댓글"
                                required
                              ></v-text-field>
                              <v-btn
                                @click="createMovieComment(rcdMovie)"
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
                                <div
                                  class="text-center"
                                  v-show="countComment(movie_comment)"
                                >
                                  <v-pagination
                                    v-model="curPageNum"
                                    :length="numOfPages"
                                  ></v-pagination>
                                </div>
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
// import moviePickitem from "@/components/moviePickitem";
import _ from "lodash";
import StarRating from "vue-star-rating";
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";
export default {
  name: "MoviePickView",
  methods: {
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
      const movie_comment = this.recentMovieComment;
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
          this.recentMovieComment = "";
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
    resetMoods() {
      if (!this.isLoggedIn) {
        alert("로그인 해주세요");
        this.$router.push("login");
        return;
      }
      for (let id in this.clicked) {
        this.clicked[id] = false;
      }
      for (let id in this.moodsCount) {
        this.moodsCount[id] = 0;
      }
    },
    save() {
      this.clickedList = [];
      this.pickedMoods = [];
      this.recommendMovie = [];
      this.recommendMovieId = [];
      for (let id in this.clicked) {
        let picked = this.clicked[id];
        if (picked) {
          this.clickedList.push(id);
        }
      }
      if (this.clickedList.length !== 5) {
        alert("지금 기분을 5개 선택해주세용");
        return;
      }
      for (let clickedKey of this.clickedList) {
        for (let id in this.moods) {
          let oneMoodList = this.moods[id];
          if (oneMoodList.includes(clickedKey)) {
            this.pickedMoods.push(id);
          }
        }
      }
      for (let pickedMood of this.pickedMoods) {
        this.moodsCount[pickedMood] += 1;
      }
      for (let id in this.moodsCount) {
        let count = this.moodsCount[id];
        if (count) {
          let i = 0;
          const recommendedMovie = _.cloneDeep(this.classifyMovie[id]);
          while (i < count * 4) {
            const randomMovie = _.sample(recommendedMovie);
            if (!this.recommendMovieId.includes(randomMovie.id)) {
              this.recommendMovie.push(randomMovie);
              this.recommendMovieId.push(randomMovie.id);
              i += 1;
            }
          }
        }
      }
      this.getGenre();
      this.dialog = false;
    },
    getGenre() {
      // const movieListLen= movies.length
      const genresDic = this.genres;
      for (let movie of this.recommendMovie) {
        let newGenre = [];
        for (let movieGenre of movie.genre_ids) {
          newGenre.push(genresDic[movieGenre]);
        }
        movie.genre_ids = newGenre;
      }
    },
    isLogin() {
      if (window.localStorage.getItem("jwt")) {
        this.isLoggedIn = true;
      } else {
        this.isLoggedIn = false;
      }
    },
  },
  components: {
    StarRating,
    // moviePickitem,
  },
  computed: {
    classifyMovie() {
      return this.$store.state.classifiedMovie;
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
  data() {
    return {
      dataPerPage: 5,
      curPageNum: 1,
      averageRate: null,
      averageStar: null,
      valid: false,
      recentMovieComment: "",
      model: null,
      userId: null,
      rating: 3,
      movie_comment: [],
      pickedMovieId: null,
      nameRules: [(v) => v.length <= 50 || "댓글은 50자 이내로 작성해주세요!"],

      isLoggedIn: false,
      dialog: false,
      clickedCount: 0,
      clicked: {
        clicked1: false,
        clicked2: false,
        clicked3: false,
        clicked4: false,
        clicked5: false,
        clicked6: false,
        clicked7: false,
        clicked8: false,
        clicked9: false,
        clicked10: false,
        clicked11: false,
        clicked12: false,
        clicked13: false,
        clicked14: false,
        clicked15: false,
        clicked16: false,
        clicked17: false,
        clicked18: false,
        clicked19: false,
        clicked20: false,
        clicked21: false,
        clicked22: false,
      },
      moods: {
        28: ["clicked1", "clicked2", "clicked3"],
        12: ["clicked4", "clicked5", "clicked6"],
        35: ["clicked7", "clicked8", "clicked9"],
        80: ["clicked10", "clicked11"],
        10751: ["clicked12", "clicked13", "clicked14"],
        14: ["clicked15", "clicked16", "clicked17"],
        10749: ["clicked18", "clicked19", "clicked20"],
        53: ["clicked21", "clicked22"],
      },
      moodsCount: {
        28: 0,
        12: 0,
        35: 0,
        80: 0,
        10751: 0,
        14: 0,
        10749: 0,
        53: 0,
      },
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
      clickedList: [],
      pickedMoods: [],
      recommendMovie: [],
      recommendMovieId: [],
    };
  },
  created() {
    this.isLogin();
  },
};
</script>

<style>
@font-face {
  font-family: "SANJUGotgam";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2112@1.0/SANJUGotgam.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: "ONE-Mobile-POP";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2105_2@1.0/ONE-Mobile-POP.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: "Katuri";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_13@1.0/Katuri.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}
.recommendpage {
  background-color: #000000;
  color: white;
}
.recommendmovie {
  background-color: black;
}
.my-font {
  font-family: ONE-Mobile-POP;
}
.my-font2 {
  font-family: SANJUGotgam;
  background-color: black;
}
.my-font3 {
  font-family: Katuri;
}
</style>