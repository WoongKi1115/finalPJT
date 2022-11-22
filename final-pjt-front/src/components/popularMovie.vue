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
                    <v-card
                      style="
                         {
                          background: 'https://image.tmdb.org/t/p/original' +
                            popularMovie.backdrop_path;
                        }
                      "
                    >
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
                          <v-col cols="7" style="color: #eeeeee" class="pa-0">
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
                                >평점 : {{ popularMovie.vote_average }}</span
                              >
                              <span
                                >개봉일 : {{ popularMovie.release_date }}</span
                              >
                            </div>
                            <br />
                            <br />
                            <label for="overview">줄거리 : </label>
                            <span id="overview">{{
                              popularMovie.overview
                            }}</span>
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

export default {
  name: "popularMovie",
  data() {
    return {
      isModalviewed: false,
      showModal: true,
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
      console.log();
    },
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