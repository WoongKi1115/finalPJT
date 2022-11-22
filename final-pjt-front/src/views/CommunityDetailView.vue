<template>
  <v-row>
    <v-col cols="2"></v-col>
    <v-col cols="8">
  <div class="detailpage">
    <v-btn
      style="float: right"
      class=""
      fab
      x-small
      color="gray"
      @click="goCommunity"
    >
      X
    </v-btn>
    <br />
    <h1>{{ article?.title }}</h1>
    <div style="padding-right: 100px; padding-left: 100px">
      <div style="text-align: right; font-size: 16px">
        작성자 : {{ article.username }}
      </div>
      <div style="text-align: right; font-size: 14px">
        작성시간 : {{ article.created_at | moment("YYYY-MM-DD HH:mm:ss") }}
      </div>
      <v-btn v-show="isYouers" color="" @click="deleteArticle" style="float:right">
        글 삭제 </v-btn
      >
      <div style="text-align: left; font-size: 19px" class="mt-10 mb-15">
        내용 : {{ article?.content }}
      </div>
    </div>
    <div class="d-flex justify-content-between">
      <div class="comment" style="width:90%">
        <v-text-field
  
        label="댓글작성"
        v-model="inputComment"
        dark
        style="background-color: #323232; width: 95%; margin: auto;"
        @keyup.enter="createComment"
        ></v-text-field>
      </div>
        <div>
          <v-btn @click="createComment">입력</v-btn>
        </div>
  </div>
    <v-list-item two-line>
      <v-list-item-content style="text-align: left; color: white;">
        <v-list-item-title
        class="mt-2"
          v-for="(comment, index) in this.comments"
          :key="index"
          >
          <span style="font-size:large" class="me-10">{{comment.username}}&nbsp;&nbsp;</span> <span>{{ comment.content }}&nbsp;&nbsp;&nbsp;&nbsp;</span>
          <button v-show="comment.user === userId" @click="deleteComment(comment.id)"><i class="fa-solid fa-trash-can"></i></button>
          <span style="float: right;">{{comment.created_at  | moment("YYYY-MM-DD HH:mm:ss") }}</span>
          <v-divider class="mt-2" dark></v-divider>
        </v-list-item-title>
      </v-list-item-content>
    </v-list-item>
  </div>
</v-col>
  <v-col cols="2"></v-col>
</v-row>
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
      comments: null,
      isYouers: false,
      userId: null,
    };
  },
  computed: {},
  methods: {
    goCommunity() {
      this.$router.push({ name: "community" });
    },
    getArticle(articleId) {
      axios({
        method: "get",
        url: `${API_URL}/community/${articleId}`,
      })
        .then((res) => {
          this.article = res.data;
          if (this.$store.state.loginUser.id === this.article.user.id) {
            this.isYouers = true;
          }
          axios({
            method: "get",
            url: `${API_URL}/community/${this.article.id}/comment_list_create/`,
          }).then((res) => {
            this.comments = res.data;
            this.userId = this.$store.state.loginUser.id;
          });
        })

        .catch((err) => {
          console.log(err);
        });
    },
    createComment() {
      const content = this.inputComment;

      axios({
        method: "post",
        url: `${API_URL}/community/${this.article.id}/comment_list_create/`,
        data: { content },
        headers: {
          Authorization: `Bearer ${window.localStorage.getItem("jwt")}`,
        },
      }).then(() => {
        axios({
          method: "get",
          url: `${API_URL}/community/${this.article.id}/comment_list_create/`,
        }).then((res) => {
          this.comments = res.data;
        });
        this.inputComment = null;
      });
    },
    deleteArticle() {
      axios({
        method: "delete",
        url: `${API_URL}/community/${this.article.id}/del/`,
        headers: {
          Authorization: `Bearer ${window.localStorage.getItem("jwt")}`,
        },
      }).then(() => {
        this.$router.push("community");
      });
    },
    deleteComment(commentId) {
      axios({
        method: "delete",
        url: `${API_URL}/community/${commentId}/comment_delete/`,
        headers: {
          Authorization: `Bearer ${window.localStorage.getItem("jwt")}`,
        },
      }).then(() => {
        console.log('성공')
        this.$router.go()
      });

    }
  },
  created() {
    this.getArticle(this.$route.params.id);
  },
};
</script>

<style>

.detailpage{
  margin: auto;
  margin-top: 90px;
  border-radius: 20px;
  padding: 25px;
  background-color: #323232;
  color: white;
}
</style>