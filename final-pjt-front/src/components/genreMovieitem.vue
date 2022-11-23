<template>
  <div>

    <h1>GenreMovie</h1>
    <p>{{ randomGenreMovies }}</p>
  </div>
</template>

<script>
// import _ from "lodash";

export default {
  name: "genreMovieitem",
  data() {
    return {
      randomMovies: null,
    };
  },
  computed: {
    randomGenreMovies() {
      return this.$store.state.randomGenreMovies;
    },
  },

  methods: {
  },
  created() {
    
  },
};
</script>

<style>
</style>