<template>
  <div class="mainpage">
    <popularMovie/>
    <br>
    <recentMovieitem />
    <genreMovieitem />
    <genreMovieitem1 />
    <genreMovieitem2 />
    <v-footer
    dark
    padless
    class="d-flex"
  >
    <v-card
      style="flex:100%"
      flat
      tile
      class="lighten-1 white--text text-center"
      
    >
      <v-card-text  >
        <v-btn
          v-for="icon in icons"
          :key="icon"
          class="mx-4 white--text"
          icon
          :href="icon[1]"
        >
          <v-icon size="24px">
            {{ icon[0] }}
          </v-icon>
        </v-btn>
      </v-card-text>

      <v-card-text class="white--text pt-0" >
        Copyright 2022 Moong
      </v-card-text>

      <v-divider></v-divider>

      <v-card-text class="white--text">
        {{ new Date().getFullYear() }} — <strong>SSAFY</strong>
      </v-card-text>
    </v-card>
  </v-footer>
  </div>
  
</template>

<script>
import popularMovie from "@/components/popularMovie";
import recentMovieitem from "@/components/recentMovieitem";
import genreMovieitem from "@/components/genreMovieitem";
import genreMovieitem1 from "@/components/genreMovieitem1";
import genreMovieitem2 from "@/components/genreMovieitem2";

export default {
  name: "MainPageView",
  components: {
    popularMovie,
    recentMovieitem,
    genreMovieitem,
    genreMovieitem1,
    genreMovieitem2,
  },
  data() {
    return {
      icons: [
        ['mdi-gitlab', 'https://lab.ssafy.com/nwk2222'],
        ['mdi-github','https://github.com/WoongKi1115'],
        ['mdi-vuetify','https://next.vuetifyjs.com/en/'],
        ['mdi-instagram','https://www.instagram.com/moooo_nam/']
      ],
    };
  },
  methods: {},

};
</script>

<style>
.mainpage{
  background-color: #000000;
  color: white;
  }
</style>