<template>
	<div>
		<h1>MainPage</h1>
	</div>
</template>

<script>
import axios from 'axios'
export default {
	name:'MainPageView',
	methods:{
		getMovies() {
			axios({
				method: 'get',
				url: 'http://127.0.0.1:8000/api/v1/',
			})
			.then((res) => {
				console.log(res)
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