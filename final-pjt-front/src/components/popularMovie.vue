<template>
	<div>
		<h1>PopularMovie</h1>
    
    <!-- <v-carousel
    cycle
    height="400"
    hide-delimiter-background
    show-arrows-on-hover
    >
  </v-carousel> -->
    <!-- <popularMovieItem
    v-for="popularMovie in popularMovies"
    :key="popularMovie.pk"
    :popularMovie='popularMovie'
    /> -->
    <p>{{popularMovies}}</p>
	</div>
</template>

<script>
// import popularMovieItem from '@/components/popularMovieItem';
export default {
	name:'popularMovie',
  components:{
    // popularMovieItem
  },
  computed:{
    popularMovies() {
      return this.$store.getters.getPopular
    }
  },
  methods:{

  }
}
</script>

<style>

</style>