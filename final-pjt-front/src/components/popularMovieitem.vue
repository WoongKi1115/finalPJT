<template>
	<div>
		<p>{{popularMovie}}</p>
		<!-- <v-row
			class="fill-height"
			align="center"
			justify="center"
		>
			<img :src="'https://image.tmdb.org/t/p/original' + movie.poster_path" alt="">
		</v-row> -->
	</div>
</template>

<script>
export default {
	name:'popularMovieItem',
	props:{
		popularMovie:Object,
	}
}
</script>

<style>

</style>