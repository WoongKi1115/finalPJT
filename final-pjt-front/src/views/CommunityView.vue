<template>
	<div>
		<h1>Community</h1>
		<v-btn @click="moveCreate">create</v-btn>
		<communityItem
		v-for="article in articles"
		:key="article.id"
		:article="article"
		/>
	</div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
import communityItem from '@/components/communityItem'

export default {
	name:'CommunityView',
	data() {
		return {
			articles:null
		}
	},
	components: {
		communityItem
	},
	methods:{
		moveCreate() {
			this.$router.push('create')
		},
		getArticle() {
			axios({
          method: 'get',
          url: `${API_URL}/community/`,
          headers:{
            Authorization: `Bearer ${window.localStorage.getItem('jwt')}`
          }
				})
				.then((res) => {
					this.articles = res.data
					console.log(res)
				})
				.catch((err) => {
					console.log(err)
				})
			}
	},
	created() {
		this.getArticle()
		console.log()
	}
}
</script>

<style>

</style>