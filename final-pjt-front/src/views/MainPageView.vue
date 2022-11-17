<template>
	<div>
		<h1>MainPage</h1>
		<popularMovieitem/>
		<recentMovieitem/>
		<genreMovieitem/>
	</div>
</template>

<script>

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
	
}
</script>

<style>

</style>