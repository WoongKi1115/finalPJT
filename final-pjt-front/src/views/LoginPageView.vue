<template>
	<div>
		<h1>Login</h1>
		<form>
			<div>
				<label for="username">username</label>
				<input type="text" id="username">

				<label for="password">password</label>
				<input type="text" id="password">
			</div>
		</form>
		<br>
		<v-btn
  elevation="2"
	small
  outlined
>회원가입</v-btn>
	</div>
</template>

<script>
export default {
	name: 'LoginPageView'
}
</script>

<style>

</style>