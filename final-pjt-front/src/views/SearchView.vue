<template>
	<div>
		<h1>검색페이지</h1> 
	</div>
</template>

<script>
export default {
	name:'SearchView',
	data() {
    return {
      searchedMovieList : [],
    }
  },

  methods:{
    serchMykeyword(serchKeyword) {
      const serchKeywordList = serchKeyword.split(" ")
      console.log(serchKeywordList)
      for (let oneWord of serchKeywordList){
        for (let id in this.allMovies) {
          let movietitle = this.allMovies[id].title
          // console.log(movietitle)
          if (movietitle.includes(oneWord)){
            this.searchedMovieList.push(this.allMovies[id])
          }
      }
      }
      console.log(this.searchedMovieList)
    }
	},
  computed:{
    allMovies() {
      return this.$store.state.movies
    } 
  },
  created() {
    this.serchMykeyword(this.$route.params.keyword)
    // console.log('왔어요')
  }
}

</script>


<style>

</style>