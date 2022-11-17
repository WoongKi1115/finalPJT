<template>
	<div>
		<h1>PopularMovie</h1>
    <template>
  <v-carousel>
    <v-carousel-item
      v-for="popularMovie in popularMovies"
      :key="popularMovie.id"
      :src="'https://image.tmdb.org/t/p/original' + popularMovie.backdrop_path"
      reverse-transition="fade-transition"
      transition="fade-transition"
    >
  </v-carousel-item>
  </v-carousel>
</template>

    <!-- <p>{{ popularMovies }}</p> -->
	</div>
</template>

<script>
// import popularMovieitem from '@/components/popularMovieitem';
export default {
	name:'popularMovie',
  data() {
    return {
      dialog: false,
    }
  },
  components:{
    // popularMovieitem
  },
  computed:{
    popularMovies() {
      return this.$store.state.top10Movie
    }
  },
}
</script>

<style>
.modalsize{
  width: 100%;
  height: 100%;
}
</style>