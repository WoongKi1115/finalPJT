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
    <p>{{ popularMovies }}</p>
	</div>
</template>

<script>
export default {
	name:'popularMovie',
  props:{

  },
  components:{
   
  },
  computed:{
    popularMovies() {
      return this.$store.state.top10Movie
    }
  },
  methods:{
 
  },
 
}
</script>

<style>

</style>