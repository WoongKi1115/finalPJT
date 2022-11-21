<template>
  <v-row>
    <v-col cols="3"></v-col>
    <v-col cols="6">
  <div class="loginpage">
    <h1>Login</h1>
    <v-row justify="center" align="center">
      <v-col cols="10">
        <v-text-field
          label="사용자 이름"
          placeholder="Username"
          v-model="username"
          filled
          rounded
          dense
        ></v-text-field>
        <v-text-field
          label="비밀번호"
          :type="show1 ? 'text' : 'password'"
          :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
          @click:append="show1 = !show1"
          placeholder="Password"
          v-model="password"
          filled
          rounded
          dense
          @keyup.enter="login"
        ></v-text-field>
      </v-col>
    </v-row>
    <br />
    <v-btn elevation="2" small outlined @click="login">로그인</v-btn>
  </div>
  </v-col>
  <v-col cols="3"></v-col>
  </v-row>
</template>

<script>
import axios from "axios";
export default {
  name: "LoginPageView",
  data: function () {
    return {
      username: null,
      password: null,
      show1: null,
    };
  },
  methods: {
    login: function () {
      const username = this.username;
      const password = this.password;
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/api/token/",
        data: { username, password },
      }).then((res) => {
        localStorage.setItem("jwt", res.data.access);
        this.$emit("login");
        this.$router.push({ name: "mainpage" });
      })
        .catch(() => alert('틀렸어!'))
    },
  },
};
</script>

<style>
.loginpage{
  margin-top: 90px;
  border-radius: 20px;
  padding: 30px;
  background-color: azure;
  color: black;
}
</style>