<template>
  <div>
    <h1>RecentMovie</h1>
    <v-sheet
    class="mx-auto"
    max-width="1800"
  >
    <v-slide-group
      dark
      style="height:550px"
      class="pa-4 recentmovie"
      active-class="success"
      show-arrows
    >
      <v-slide-item
        class="mt-6"
        v-for="(recentmovie, index) in recenteMovies"
        :key="index"
      >
        <v-card 
          class="ma-4 pa-1 posterimg"
          height="450"
          width="300"
        >
        <div class="text-center">
    <v-dialog

      width="1800"
    >
      <template v-slot:activator="{ on, attrs }" >
        <v-img
          
          v-bind="attrs"
          v-on="on"
          :src="'https://image.tmdb.org/t/p/original' + recentmovie.poster_path"
          height="440"
        >
        </v-img>
      </template>

      <v-card >
        

        <v-card-text class="pa-7 modalstyle">
          <v-row>
            <v-col cols='5' class="pa-0">
              <img class="modalimage" :src="'https://image.tmdb.org/t/p/original' + recentmovie.poster_path">
            </v-col>
            <v-col cols='7' class="pa-0" style="color:#EEEEEE">
              <h1>{{recentmovie.title}}</h1>
              <br>
              <br>
              <div class="d-flex justify-space-around">
                <div>
                  <label for="genre">장르 : </label>
                  <span id="genre" v-for="(genre, index) in recentmovie.genre_ids" :key="index"> {{genre}}&nbsp;&nbsp;&nbsp; </span>
                </div>
              <span>평점 : {{recentmovie.vote_average}}</span>
              <span>개봉일 : {{recentmovie.release_date}}</span>
              </div>
              <br>
              <br>
              <label for="overview">줄거리 : </label>
              <span id="overview">{{recentmovie.overview}}</span>
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
export default {
  name: "recentMovieitem",
  data() {
    return {
      model:null,
      
    }
  },
  computed: {
    recenteMovies() {
      return this.$store.state.recenteMovie;
    },
  },
  
};
</script>

<style>
.recentmovie{
  background-color: black;
}
#next-icon
{
    color: rgb(234, 10, 10)!important;

}
.posterimg:hover {
  transform: scale(1.1);
}
.modalstyle {
  background-color:#222222;
  color: #EEEEEE;
}

</style>