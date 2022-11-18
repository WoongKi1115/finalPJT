<template>
  <div>
    <h1>RecentMovie</h1>
    <v-sheet
    class="mx-auto"
    max-width="1800"
  >
    <v-slide-group
      v-model="model"
      class="pa-4"
      active-class="success"
      show-arrows
    >
      <v-slide-item
        v-for="(recentmovie, index) in recenteMovies"
        :key="index"
      >
        <v-card
          class="ma-4 pa-1"
          height="450"
          width="300"
        >
        <div class="text-center">
    <v-dialog
      v-model="dialog"
      width="1800"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-img
          v-bind="attrs"
          v-on="on"
          :src="'https://image.tmdb.org/t/p/original' + recentmovie.poster_path"
        >
        </v-img>
      </template>

      <v-card>
        <!-- <v-card-title class="text-h5 grey lighten-2">
          {{recentmovie.title}}
        </v-card-title> -->

        <v-card-text class="pa-5">
          <v-row>
            <v-col cols='6'>
              <v-img :src="'https://image.tmdb.org/t/p/original' + recentmovie.poster_path"></v-img>
            </v-col>
            <v-col>
              <h1>{{recentmovie.title}}</h1>
              <br>
              <br>
              <p>{{recentmovie.overview}}</p>
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
</style>