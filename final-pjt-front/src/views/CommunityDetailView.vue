<template>
  <div>
    <h1>Detail</h1>
    <p>번호 : {{ article?.id }}</p>
    <p>제목 : {{ article?.title }}</p>
    <p>내용 : {{ article?.content }}</p>
  </div>
</template>

<script>
export default {
  name: "CommunityDetailView",
  data() {
    return {
      article: null,
    };
  },
  computed: {
    articles() {
      return this.$store.state.articles;
    },
  },
  methods: {
    getArticleId(pickid) {
      for (let articleId in this.articles) {
        if (this.articles[articleId].id === pickid) {
          this.article = this.articles[articleId]
          // console.log("성공");
          break
          // }
        }
      }
    },
  },
  created() {
    this.getArticleId(this.$route.params.id);
  },
};
</script>

<style>
</style>