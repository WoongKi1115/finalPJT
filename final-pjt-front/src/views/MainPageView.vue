<template>
  <div class="mainpage">
    <popularMovie/>
    <br>
    <recentMovieitem />
    <genreMovieitem />
    <genreMovieitem1 />
    <genreMovieitem2 />
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