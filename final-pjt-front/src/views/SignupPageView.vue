<template>
  <div>
    <h1>Signup</h1>
    <v-row justify="center" align="center">
      <v-col cols="12" sm="5" md="5" >
        <v-text-field
          label="사용자 이름"
          placeholder="Username"
          v-model="credentials.username"
          filled
          rounded
          dense
        ></v-text-field>

        <v-text-field
          label="비밀번호"
          :type="show1 ? 'text' : 'password'"
          placeholder="Password"
          v-model="credentials.password"
          :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
          @click:append="show1 = !show1"
          filled
          rounded
          dense
        ></v-text-field>

        <v-text-field
          label="비밀번호 확인"
          :type="show2 ? 'text' : 'password'"
          placeholder="Passwordconfirm"
          v-model="credentials.passwordConfirm"
          :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
          @click:append="show2 = !show2"
          @keyup.enter="signup"
          :rules="[matchingPasswords]"
          filled
          rounded
          dense
        ></v-text-field>

        <v-text-field
          label="이메일"
          placeholder="email"
          v-model="credentials.email"
          type="email"
          filled
          rounded
          dense
        ></v-text-field>
      </v-col>
    </v-row>
    <button @click="signup">회원가입</button>
  </div>
</template>
  
  <script>
import axios from "axios";

export default {
  name: "SignupPageView",
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
        passwordConfirm: null,
        email: null,
      },
      show1: false,
      show2: false,
    };
  },
  methods: {
    signup: function () {
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/accounts/signup/",
        data: this.credentials,
      })
        .then(() => {
          alert("회원가입 성공!");
          this.$router.push({ name: "login" });
        })
        .catch((err) => {
          console.log(err);
        });
    },
    matchingPasswords: function () {
      if (this.credentials.password === this.credentials.passwordConfirm) {
        return true;
      } else {
        return "비밀번호가 일치하지 않습니다.";
      }
    },
  },
};
</script>
  