<template>
    <div>
      <v-row>
        <v-col cols='3'></v-col>
        <v-col cols='6'>
      <div class="signuppage">
        <h1>Signup</h1>
        <v-row justify="center" align="center">
          <v-col cols="10">
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
        <v-btn  elevation="2" small outlined @click="signup">회원가입</v-btn>
        </div>
        </v-col>
        <v-col cols='3'></v-col>
        </v-row>
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
<style>
.signuppage{
  margin-top: 90px;
  border-radius: 20px;
  padding: 30px;
  background-color: azure;
  color: black;
}
</style>
  