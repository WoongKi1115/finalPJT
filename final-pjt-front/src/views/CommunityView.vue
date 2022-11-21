<template>
	<div>
		<h1>Community</h1>
		<v-btn @click="moveCreate">create</v-btn>
	</div>
</template>

<script>

export default {
	name:'CommunityView',
	methods:{
		moveCreate() {
			this.$router.push('@/components/createArticle')
		}
	}
}
</script>

<style>

</style>