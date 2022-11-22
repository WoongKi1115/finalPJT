<template>
  <v-row>
    <v-col cols="2"></v-col>
    <v-col cols="8" class="createArticle">
      <v-btn
      style="float:right"
      class=""
      fab
      x-small
      color="gray"
      @click="goCommunity"
    >
    X
    </v-btn>
      <h1>Create</h1>
    <div>
      <form>
    <v-text-field
      dark
      v-model="title"
      
      label="Title"
    ></v-text-field>
    <v-textarea
          dark
          background-color="#222222"
          solo
          v-model="content"
          label="Content"
        ></v-textarea>
    <v-btn
      class="mr-4"
      @click="createArticle"
    >
      submit
    </v-btn>
  </form>
    </div>
  </v-col>
    <v-col cols="2"></v-col>
  </v-row>
  </template>
  
  <script>
  import axios from'axios'
  
  const API_URL = 'http://127.0.0.1:8000'
  
  export default {
    name: 'createArticle',
    data: function () {
      return {
        title: null,
        content:null,
      }
    },
    methods: {
      goCommunity() {
      this.$router.push({name:"community"})
    },
      createArticle() {
        const title = this.title
        const content = this.content
        if (!title) {
          alert('입력을해!!!!')
          return
        }
        axios({
          method: 'post',
          url: `${API_URL}/community/`,
          data: { title, content },
          headers:{
            Authorization: `Bearer ${window.localStorage.getItem('jwt')}`
          }
  
        
        })
        .then(() => {
          console.log('성공')
          this.$router.push('community')
        })
      }
    }
  }
  </script>
  <style>
    .createArticle{
      margin-top: 90px;
      border-radius: 20px;
      padding: 30px;
      background-color: #323232;
      color: white;
    }
  </style>