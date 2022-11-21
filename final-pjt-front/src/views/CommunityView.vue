<template>
  <div>
    <h1>Community</h1>
    <v-btn @click="moveCreate">create</v-btn>
    <v-row>
      <v-col cols="1"></v-col>
      <v-col cols="10">
        <div
          style="background-color: white; color: black"
          class="text-center d-flex align-items-center"
        >
          <v-row>
            <v-col
              cols="1"
              style="
                border-right: 1px solid black;
                border-bottom: 1px solid black;
              "
            >
              ID
            </v-col>
            <v-col cols="8"> TITLE </v-col>
            <v-col cols="2"> 작성시간 </v-col>
            <v-col cols="1"> 추천 수 </v-col>
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
import communityItem from "@/components/communityItem";

export default {
  name: "CommunityView",
  data(){
    return {
      isLoggedIn: false,
    }
  },
  computed: {
    articles() {
      return this.$store.state.articles;
    },
  },
  components: {
    communityItem,
  },
  methods: {
    moveCreate() {
      if (!this.isLoggedIn){
        alert("로그인 해주세요");
        this.$router.push("login");
        return;
      }
      this.$router.push("create");
    },
    isLogin() {
      if (window.localStorage.getItem("jwt")) {
        this.isLoggedIn = true;
      } else {
        this.isLoggedIn = false;
      }
    },
  },
  created() {
    this.isLogin();
  },
};
</script>

<style>
</style>