<template>
	<div style="color:white">
		<span>{{article.title}}</span>
		<span>{{article.username}}</span>
	</div>
</template>

<script>
export default {
	name:'communityItem',
	props:{
		article:Object
	}
}
</script>

<style>

</style>