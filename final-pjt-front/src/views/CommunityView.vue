<template>
	<div>
		<h1>Community</h1>
		<v-btn @click="moveCreate">create</v-btn>
		<v-row>
			<v-col cols="1"></v-col>
			<v-col cols="10">
		<div style="background-color:white; color:black" class="text-center d-flex align-items-center">
		<v-row>
			<v-col cols="1" style="border-right:1px solid black; border-bottom: 1px solid black">
				ID
			</v-col>
			<v-col cols="8">
				TITLE
			</v-col>
			<v-col cols="2">
				작성시간
			</v-col>
			<v-col cols="1">
				추천 수
			</v-col>
		</v-row>
	</div>
		<communityItem
		v-for="article in articles"
		:key="article.id"
		:article="article"
		/>
	</v-col>
	<v-col cols="1"></v-col>
	</v-row>
	</div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
import communityItem from '@/components/communityItem'

export default {
	name:'CommunityView',
	computed: {
		articles() {
			return this.$store.state.articles
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
					this.$store.state.articles = res.data
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