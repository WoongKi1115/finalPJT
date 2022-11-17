<template>
	<div>
		<h1>MainPage</h1>
		<popularMovieitem/>
		<recentMovieitem/>
		<genreMovieitem/>
	</div>
</template>

<script>
import axios from 'axios'
import popularMovieitem from '@/components/popularMovieitem'
import recentMovieitem from '@/components/recentMovieitem'
import genreMovieitem from '@/components/genreMovieitem'
export default {
	name:'MainPageView',
	components:{
		popularMovieitem,
		recentMovieitem,
		genreMovieitem
	},
	data() {
		return {
			allMovies:null,
		}
	},
	methods:{
		getMovies() {
			axios({
				method: 'get',
				url: 'http://127.0.0.1:8000/api/v1/',
			})
			.then((res) => {
				this.allMovies = res.data
				this.$store.state.allMovies = res.data
				console.log(this.$store.state.allMovies)
			})
			.catch((err) => {
				console.log(err)
			})
		}
	},
	created() {
		this.getMovies()
	}
}
</script>

<style>

</style>