<template>
    <div>
      <input 
        type="text" 
        v-model.trim="title" 
      >
      <input 
        type="text" 
        v-model.trim="content" 
        @keyup.enter="createArticle"
      >
      <button @click="createArticle">+</button>
    </div>
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
  