<template>
  <div>
    <h1>RecentMovie</h1>
    <p>{{ recenteMovies }}</p>
  </div>
</template>

<script>
export default {
  name: "recentMovieitem",
  computed: {
    recenteMovies() {
      return this.$store.state.recenteMovie;
    },
  },
};
</script>

<style>
</style>