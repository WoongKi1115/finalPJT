<template>
	<div>
		<h1>Detail</h1>
		<p>번호 : {{article?.id}}</p>
		<p>제목 : {{article?.title}}</p>
	</div>
</template>

<script>
export default {
	name:"CommunityDetailView",
	data() {
		return {
			article:null
		}
	},
	computed:{
		articles() {
			return this.$store.state.articles
		}
	},
	methods:{
	getArticleId(id) {
		for (const article of this.aritcles) {
			if (article.id === Number(id)) {
				this.article = article
				break
			}
		}
		}
	},
	created() {
		this.getArticleId(this.$route.params.id)
	}
}
</script>

<style>

</style>