<template>
  <div>
    <h1>Detail</h1>
    <p>번호 : {{ article?.id }}</p>
    <p>제목 : {{ article?.title }}</p>
    <p>내용 : {{ article?.content }}</p>
    <div class="comment">
      <v-text-field
        label="댓글"
        v-model="inputComment"
        filled
        rounded
        dense
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
  background-color: white;
}
</style>