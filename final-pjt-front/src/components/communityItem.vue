<template>
	<div style="color:white">
		<v-divider></v-divider>
		<div @click="goDetail(article.id)" style="background-color:white; color:black;" class="text-center d-flex align-items-center">
		<v-row>
			<v-col cols="1" style="border-right:1px solid black;" class="pe-0">
				{{article.id}}
			</v-col>
			<v-col style="
                border-right: 1px solid black;
              " cols="6">
				{{article.title}}
			</v-col>
			<v-col style="
                border-right: 1px solid black;
              " cols="2">
				{{datetime}}
			</v-col>
			<v-col style="
                border-right: 1px solid black;
              " cols="2">
				{{article.username}}
			</v-col>
			<v-col  cols="1">
				댓글 수
			</v-col>

		</v-row>
	</div>
	</div>
</template>

<script>
export default {
	name:'communityItem',
	data() {
		return {
			datetime:null,
		}
	},
	props:{
		article:Object
	},
	methods:{
		goDetail(id) {
			this.$router.push({name:'communityDetail', params:{id}})
		},
	}
}
</script>

<style>

</style>