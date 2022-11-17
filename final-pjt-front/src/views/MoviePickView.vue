<template>
	<div>
		<h1>MoviePickView</h1>
		<div>
			<p>여기는 설명칸</p>
		</div>
		<v-btn
  elevation="2"
  large
  outlined
>추천용 버튼</v-btn>
<br>
<br>
<moviePickitem/>
	</div>
</template>

<script>
import moviePickitem from '@/components/moviePickitem';
export default {
	name:'MoviePickView',
	components:{
		moviePickitem
	}
}
</script>

<style>

</style>