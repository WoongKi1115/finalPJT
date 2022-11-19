<template>
  <div class="mainpage">
    <popularMovie/>
    <br>
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
.mainpage{
  background-color: #000000;
  color: white;
  }
</style>