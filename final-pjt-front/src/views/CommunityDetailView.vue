<template>
  <div class="detailpage">
    <v-btn
      style="float:right"
      class=""
      fab
      dark
      x-small
      color="gray"
      @click="goCommunity"
    >
    X
    </v-btn>
    <br>
    <h1>{{ article?.title }}</h1>
    <div style="padding-right:100px; padding-left:100px;">
    <div style="text-align:right; font-size:16px;">작성자 : {{article.username}}</div>
    <div style="text-align:right; font-size:14px;">작성시간 : {{article.created_at | moment('YYYY-MM-DD HH:mm:ss')}}</div>
    <div style="text-align:left; font-size:19px;" class="mt-10 mb-15">내용 : {{ article?.content }}</div>
    </div>
    <div class="comment">
      <v-text-field
        label="댓글"
        v-model="inputComment"
        filled
        rounded
        dense
        style="background-color:white;"
        @keyup.enter="createComment"
      ></v-text-field>
    </div>
  </div>
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";
export default {
  name: "CommunityDetailView",
  data() {
    return {
      article: null,
      inputComment: null,
    };
  },
  computed: {},
  methods: {
    goCommunity() {
      this.$router.push({name:"community"})
    },
    getArticle(articleId) {
      axios({
        method: "get",
        url: `${API_URL}/community/${articleId}`,
      })
        .then((res) => {
          this.article = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    createComment() {
      const content = this.inputComment
      
        // if (!this.content) {
        //   alert('입력을해!!!!')
        //   return
        // }
        axios({
          method: 'post',
          url: `${API_URL}/community/${this.article.id}/comment_list_create/`,
          data: { content },
          headers:{
            Authorization: `Bearer ${window.localStorage.getItem('jwt')}`
          }
        })
        .then(() => {
          console.log('성공')
          // this.$router.push({name:'communityDetail', params:{id}})
        })
    },
  },

  created() {
    this.getArticle(this.$route.params.id);
  },
};
</script>

<style>
.comment {


  
}
.detailpage{
  width: 80%;
  margin : auto;
  margin-top: 90px;
  border-radius: 20px;
  padding: 25px;
  background-color: azure;
  color: black;
}
</style>