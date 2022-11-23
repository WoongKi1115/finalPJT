<template>
	<div>
    <v-item-group>
      <v-container>
        <v-row>
          <v-col v-for="movie in searchedMovieList" :key="movie.pk" cols="12" md="3">
            <v-card class="ma-4 pa-1 posterimg" height="500" width="300">
            <div class="text-center">
              <v-dialog width="1800">
                <template v-slot:activator="{ on, attrs }">
                  <v-img
                    v-bind="attrs"
                    v-on="on"
                    :src="
                      'https://image.tmdb.org/t/p/original' +
                      movie.poster_path
                    "
                    height="440"
                    @click="getMovieComment(movie)"
                  >
                  </v-img>
                  <h4 class="mt-2">{{movie.title}}</h4>
                </template>

                <v-card>
                  <v-card-text class="pa-7 modalstyle">
                    <v-row>
                      <v-col cols="5" class="pa-0">
                        <img
                          class="modalimage"
                          :src="
                            'https://image.tmdb.org/t/p/original' +
                            movie.poster_path
                          "
                        />
                      </v-col>
                      <v-col cols="7" class="pa-0" style="color: #eeeeee">
                        <div style="position: relative" class="pe-10">
                          <div
                            style="position: relative; top: 20px; width: 90%"
                          >
                            <h2>{{ movie.title }}</h2>
                            <br />
                            <br />
                            <v-row>
                              <v-col cols="9" style="font-size: medium">
                                <div class="d-flex">
                                <label for="genre">장르 :&nbsp; </label>
                                <span
                                  id="genre"
                                  v-for="(
                                    genre, index
                                  ) in movie.genre_ids"
                                  :key="index"
                                >
                                  {{ genre }}&nbsp;&nbsp;&nbsp;
                                </span>
                              </div>
                              <div class="d-flex my-2"
                              >개봉일 : {{ movie.release_date }}</div
                              >
                              <div class="d-flex">
                                  감독 : {{ movie.director }}
                                </div>
                                <div
                                  class="d-flex my-2"
                                  style="text-align: left"
                                >
                                  주연 :
                                  {{
                                    movie.actors
                                      .replace(/\[/g, "")
                                      .replace(/\]/g, "")
                                      .replace(/\'/g, "")
                                  }}
                                </div>
                              <div class="d-flex"
                              >평점 :
                              <star-rating
                                  class="mx-3"
                                  :increment="0.01"
                                  :rating="averageStar"
                                  :read-only="true"
                                  :show-rating="false"
                                  :star-size="20"
                                  ></star-rating
                                  >{{ averageRate }}</div
                                  >
                                </v-col>
                                </v-row>
                            <v-card height="150" dark class="ms-6 mt-3 overview overflow-auto">
                              <v-card-text  dark>
                                {{ movie.overview }}
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
                                @keyup.enter="createMovieComment(movie)"
                                dark
                                class="pa-3"
                                style="background-color: #222222"
                                v-model="movieComment"
                                :rules="nameRules"
                                :counter="50"
                                label="댓글"
                                required
                              ></v-text-field>
                              <v-btn
                                @click="createMovieComment(movie)"
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
                                <div class="text-center"
                                v-show="countComment(movie_comment)"
                              style="align-item-end">
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
          </v-col>
        </v-row>
      </v-container>
    </v-item-group> 
	</div>
</template>

<script>
import StarRating from "vue-star-rating";
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";
export default {
	name:'SearchView',
  components:{
		StarRating
	},
	data() {
    return {
      dataPerPage: 5,
      curPageNum: 1,
      valid: false,
      movieComment: "",
      model: null,
      userId: null,
      rating: 3,
      movie_comment: [],
      pickedMovieId: null,
      nameRules: [(v) => v.length <= 50 || "댓글은 50자 이내로 작성해주세요!"],
      averageRate: null,
      averageStar: null,
      searchedMovieList : [],
    }
  },

  methods:{
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
      const movie_comment = this.movieComment;
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
      }).then(() => {
        axios({
          method: "get",
          url: `${API_URL}/api/v1/${pickedMovie.id}/moviecomment/`,
        }).then((res) => {
          this.movie_comment = res.data;
          this.pickedMovieId = pickedMovie.id;
          this.userId = this.$store.state.loginUser.id;
          this.getAvg();
        });
        
        
        this.movieComment = "";
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
    serchMykeyword(serchKeyword) {
      const serchKeywordList = serchKeyword.split(" ")
      console.log(serchKeywordList)
      for (let oneWord of serchKeywordList){
        for (let id in this.allMovies) {
          let movietitle = this.allMovies[id].title
          let originTitle = this.allMovies[id].original_title.toLowerCase()
          // console.log(movietitle)
          if (movietitle.includes(oneWord) || originTitle.includes(oneWord.toLowerCase())){
            if (!this.searchedMovieList.includes(this.allMovies[id])) {
              this.searchedMovieList.push(this.allMovies[id])
            }
          }
      }
      }
    }
	},
  computed:{
    allMovies() {
      return this.$store.state.movies
    },
    startOffset() {
        return ((this.curPageNum - 1) * this.dataPerPage);
      },
      endOffset() {
        return (this.startOffset + this.dataPerPage);
      },
      numOfPages() {
        return Math.ceil(this.movie_comment.length / this.dataPerPage);
      },
      calData() {
        return this.movie_comment.slice(this.startOffset, this.endOffset)
      } 
  },
  created() {
    this.serchMykeyword(this.$route.params.keyword)
    // console.log('왔어요')
  }
}

</script>


<style>

</style>