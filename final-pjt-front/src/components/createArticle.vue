<template>
    <div>
      <input 
        type="text" 
        v-model.trim="title" 
        @keyup.enter="createTodo"
      >
      <input 
        type="text" 
        v-model.trim="title" 
        @keyup.enter="createTodo"
      >
      <button @click="createTodo">+</button>
    </div>
  </template>
  
  <script>
  import axios from'axios'
  
  const API_URL = 'http://127.0.0.1:8000'
  
  export default {
    name: 'CreateTodo',
    data: function () {
      return {
        title: null,
      }
    },
    methods: {
      createTodo() {
        const title = this.title
        if (!title) {
          alert('입력을해!!!!')
          return
        }
        axios({
          method: 'post',
          url: `${API_URL}/todos/`,
          data: { title },
          headers:{
            Authorization: `Bearer ${window.localStorage.getItem('jwt')}`
          }
  
        
        })
        .then(() => {
          this.$router.push({ name: 'TodoList' })
        })
      }
    }
  }
  </script>
  