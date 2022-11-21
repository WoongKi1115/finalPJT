<template>
	<div style="color:white">
		<v-divider></v-divider>
		<div style="background-color:white; color:black;" class="text-center d-flex align-items-center">
		<v-row>
			<v-col cols="1" style="border-right:1px solid black;" class="pe-0 d-flex align-self-center justify-center">
				{{article.id}}
			</v-col>
			<v-col @click="goDetail(article.id)"  style="
                border-right: 1px solid black;
              " cols="6" class="d-flex align-self-center justify-center">
				{{article.title}}
			</v-col>
			<v-col style="border-right: 1px solid black;"
			cols="2" class="d-flex align-self-center justify-center">
				{{article.created_at | moment('YYYY-MM-DD HH:mm:ss')}}
			</v-col>
			<v-col style="
                border-right: 1px solid black;
              " cols="2" class="d-flex align-self-center justify-center">
				{{article.username}}
			</v-col>
			<v-col  cols="1" class="ps-0">
				댓글 수
			</v-col>

		</v-row>
	</div>
	</div>
</template>

<script>
import Vue from 'vue'
import vueMoment from 'vue-moment'
Vue.use(vueMoment)
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