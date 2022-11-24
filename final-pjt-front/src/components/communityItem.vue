<template>
  <div
    @click="goDetail(article.id)"
    class="selectArticle board_list_body pa-4 d-flex align-items-center"
    :class="{ id_hol: checkId }"
  >
    <div class="articles_id">
      {{ article.id }}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    </div>
    <div class="articles_title ms-15">{{ article.title }} ({{ commentsLengh }})</div>
    <div class="articles_username">{{ article.username }}</div>
    <div class="articles_created_at">
      {{ article.created_at | moment("YYYY-MM-DD HH:mm:ss") }}
    </div>
  </div>
</template>

<script>
import Vue from "vue";
import vueMoment from "vue-moment";
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";

Vue.use(vueMoment);
export default {
  name: "communityItem",
  data() {
    return {
      datetime: null,
      checkId: false,
      commentsLengh: 0,
    };
  },
  props: {
    article: Object,
  },
  methods: {
    goDetail(id) {
      this.$router.push({ name: "communityDetail", params: { id } });
    },
    getCommentLengh() {
      axios({
        method: "get",
        url: `${API_URL}/community/${this.article.id}/comment_list_create/`,
      }).then((res) => {
        this.commentsLengh = res.data.length;
      });
    },
  },
  created() {
    this.getCommentLengh()
  },
};
</script>

<style>
.selectArticle:hover {
  background-color: #333333;
}

.board_list_body {
  display: inline-block;
  font-size: 19px;
  border-bottom: 1px solid;
}
.id_hol {
  background-color: gary;
}
.id_hod {
  background-color: black;
}

.articles_id {
  float: left;
  width: 10%;
}
.articles_title {
  float: left;
  width: 60%;
  text-align: left;
}
.articles_username {
  float: left;
  width: 15%;
}
.articles_created_at {
  float: left;
  width: 15%;
}
.articles_views {
  float: left;
  width: 10%;
}
</style>