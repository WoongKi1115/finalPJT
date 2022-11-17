<template>
  <div>
    <h1>MainPage</h1>
    <popularMovie />
    <recentMovieitem />
    <genreMovieitem />
  </div>
</template>

<script>
import popularMovie from "@/components/popularMovie";
import recentMovieitem from "@/components/recentMovieitem";
import genreMovieitem from "@/components/genreMovieitem";

export default {
  name: "MainPageView",
  components: {
    popularMovie,
    recentMovieitem,
    genreMovieitem,
  },
  data() {
    return {
      
    };
  },
  methods: {},

};
</script>

<style>
</style>