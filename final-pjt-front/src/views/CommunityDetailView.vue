<template>
  <div>
    <h1>Detail</h1>
    <p>번호 : {{ article?.id }}</p>
    <p>제목 : {{ article?.title }}</p>
    <p>내용 : {{ article?.content }}</p>
    <v-text-field v-model="createComment" label="comment"></v-text-field>
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
      createComment: null,
    };
  },
  computed: {
  },
  methods: {
    getArticle(articleId) {
      axios({
        method: "get",
        url: `${API_URL}/community/${articleId}`,
      })
      .then((res) =>{
        this.article = res.data
      })
        .catch((err) => {
          console.log(err);
        });
    },

  },

  created() {
    this.getArticle(this.$route.params.id);
  },
};
</script>

<style>
</style>