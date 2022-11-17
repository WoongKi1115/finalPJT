<template>
	<div>
		<v-sheet
        height="100%"
        tile
      >
		<v-row
		class="fill-height"
		align="center"
		justify="center"
		>
		<img :src="'https://image.tmdb.org/t/p/original' + popularMovie.poster_path" alt="">
		</v-row>
		</v-sheet>
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
img{
	height: auto;	
}
</style>