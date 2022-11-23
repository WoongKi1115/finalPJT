<template>
  <div>

    <h1>GenreMovie</h1>
    <p>{{ randomGenre }}</p>
    <p>{{ randomGenreMovies }}</p>
  </div>
</template>

<script>
import _ from "lodash";

export default {
  name: "genreMovieitem",
  data() {
    return {
      randomMovies: null,
    };
  },
  computed: {
    randomGenreMovies() {
      const pickedMovies = _.sampleSize(this.$store.state.randomGenreMovies, 20)
      return pickedMovies
    },
    randomGenre(){
      return this.$store.state.randomGenre
    }
  },

  methods: {
  },
  created() {

  },
};
</script>

<style>
</style>