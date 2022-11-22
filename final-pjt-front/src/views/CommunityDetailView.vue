<template>
  <div class="detailpage">
    <v-btn
      style="float: right"
      class=""
      fab
      dark
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
      <v-btn v-show="isYouers" @click="deleteArticle">
        게시글 삭제하기</v-btn
      >
      <div style="text-align: left; font-size: 19px" class="mt-10 mb-15">
        내용 : {{ article?.content }}
      </div>
    </div>
    <div class="comment">
      <v-text-field
        label="댓글작성"
        v-model="inputComment"
        style="background-color: white"
        @keyup.enter="createComment"
      ></v-text-field>
    </div>
    <v-list-item two-line>
      <v-list-item-content style="text-align: left">
        <v-list-item-title
          v-for="(comment, index) in this.comments"
          :key="index"
          >{{ comment.content }}
          <v-btn v-show="comment.user === userId" @click="deleteComment(comment.id)">여긴어디</v-btn>
        </v-list-item-title>
      </v-list-item-content>
    </v-list-item>
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
  width: 80%;
  margin: auto;
  margin-top: 90px;
  border-radius: 20px;
  padding: 25px;
  background-color: azure;
  color: black;
}
</style>