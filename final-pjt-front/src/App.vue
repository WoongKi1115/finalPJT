<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
    <div class="d-flex align-center">
      <!-- 로고 들어갈 자리 -->
      </div>
      
      <v-spacer>
        
      </v-spacer>
      
    <router-link :to="{name:'moviepick'}" class="white--text">추천</router-link>
    <router-link :to="{name:'moviepick'}" class="white--text">Login</router-link>
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
