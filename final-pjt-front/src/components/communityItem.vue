<template>
	<div style="color:white">
		<div @click="goDetail(article.id)" style="background-color:white; color:black;" class="text-center d-flex align-items-center">
		<v-row>
			<v-col cols="1" style="border-right:1px solid black; border-bottom: 1px solid black;">
				{{article.id}}
			</v-col>
			<v-col cols="8">
				{{article.title}}
			</v-col>
			<v-col cols="2">
				{{article.created_at}}
			</v-col>
			<v-col cols="1">
				추천 수
			</v-col>

		</v-row>
	</div>
	</div>
</template>

<script>
export default {
	name:'communityItem',
	props:{
		article:Object
	},
	methods:{
		goDetail(id) {
			this.$router.push({name:'communityDetail', params:{id}})
		}
	}
}
</script>

<style>

</style>