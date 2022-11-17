<template>
  <v-app class="v-app">
    <v-app-bar
      app
      color="primary"
      dark
    >
    <div class="d-flex align-center">
      <!-- 로고 들어갈 자리 -->
      <router-link :to="{name:'mainpage'}" class="white--text">
        <img src="" alt="로고자리">
      </router-link>
      </div>
      
      <v-spacer>
        
      </v-spacer>
    <div>
      <router-link :to="{name:'moviepick'}" class="white--text mx-3">추천</router-link>
      <router-link :to="{name:'login'}" class="white--text mx-3">Login</router-link>
      <router-link :to="{name:'signup'}" class="white--text mx-3">회원가입</router-link>
    </div>
  </v-app-bar>
  
  <v-main>

    <router-view/>
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
    //
  }),
};
</script>

<style>
.v-app {
  text-align: center;
}
</style>
