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
                        <h1>{{ rcdMovie.title }}</h1>
                        <br />
                        <br />
                        <div class="d-flex justify-space-around">
                          <div>
                            <label for="genre">장르 : </label>
                            <span
                              id="genre"
                              v-for="(genre, index) in rcdMovie.genre_ids"
                              :key="index"
                            >
                              {{ genre }}&nbsp;&nbsp;&nbsp;
                            </span>
                          </div>
                          <span>평점 : {{ rcdMovie.vote_average }}</span>
                          <span>개봉일 : {{ rcdMovie.release_date }}</span>
                        </div>
                        <br />
                        <br />
                        <label for="overview">줄거리 : </label>
                        <span id="overview">{{ rcdMovie.overview }}</span>
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
export default {
  name: "MoviePickView",
  methods: {
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
          while (i < count*2) {
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
    // moviePickitem,
  },
  computed: {
    classifyMovie() {
      return this.$store.state.classifiedMovie;
    },
  },
  data() {
    return {
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
    font-family: 'ONE-Mobile-POP';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2105_2@1.0/ONE-Mobile-POP.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
@font-face {
    font-family: 'Katuri';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_13@1.0/Katuri.woff') format('woff');
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
.my-font3{
  font-family:Katuri;
}
</style>