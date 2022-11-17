<template>
	<div>
		<h1>PopularMovie</h1>
    <template>
  <v-carousel height="1000">
    <v-carousel-item
      v-for="popularMovie in popularMovies"
      :key="popularMovie.id"
      
      reverse-transition="fade-transition"
      transition="fade-transition"
    ><v-hover>
      <template v-slot:default="{ hover }">
        <v-card
          class="mx-auto"
          max-width="auto"
          max-height="auto"
        >
          <div>
          <v-img class="d-flex" :src="'https://image.tmdb.org/t/p/original' + popularMovie.backdrop_path">
          <v-btn class="d-flex align-self-end mt-5"  text color="white">
            <h2>{{popularMovie.title}}</h2>
            </v-btn>
          </v-img>
          </div>
          <v-fade-transition>
            <v-overlay
              v-if="hover"
              absolute
              color="#036358"
            >
            </v-overlay>
          </v-fade-transition>
        </v-card>
      </template>
    </v-hover>
    
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
      isModalviewed:false
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
.btnsize{
  font-size: 3rem;
}

</style>