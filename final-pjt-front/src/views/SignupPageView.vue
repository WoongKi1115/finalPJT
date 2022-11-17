<template>
  <div>
    <h1>Signup</h1>
    <div>
      <v-text-field
        label="사용자 이름"
        placeholder="Username"
        v-model="credentials.username"
      ></v-text-field>
    </div>
    <div>
      <v-text-field
        label="비밀번호"
		type="password"
        placeholder="Passwordconfirm"
        v-model="credentials.password"
      ></v-text-field>
    </div>
    <div>
      <v-text-field
        label="비밀번호 확인"
		type="password"
		placeholder="Passwordconfirm"
        v-model="credentials.passwordConfirm"
        @keyup.enter="signup"
      ></v-text-field>
    </div>
    <div>
      <v-text-field label="이메일" v-model="credentials.email" type="email"></v-text-field>
    </div>
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
        passwordConfir: null,
        email: null,
      },
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
  },
};
</script>
  