<template>
  <div class="communitypage">
    <h1>Community</h1>
    <v-btn
    color="#E50914"
    dark
    @click="moveCreate">create</v-btn>
    <div class="board_list_wrap">
      <div class="board_list">
        <div class="board_list_head">
          <div class="articles_id" style="border-top: 2px solid #E50914;
  border-bottom: 2px solid #E50914;">#</div>
          <div class="articles_title" style="border-top: 2px solid #E50914;
  border-bottom: 2px solid #E50914;">제목</div>
          <div class="articles_username" style="border-top: 2px solid #E50914;
  border-bottom: 2px solid #E50914;">작성자</div>
          <div class="articles_created_at" style="border-top: 2px solid #E50914;
  border-bottom: 2px solid #E50914;">작성일</div>
          <div class="articles_views" style="border-top: 2px solid #E50914;
  border-bottom: 2px solid #E50914;">조회</div>
        </div>
        <div >
        <communityItem
          v-for="article in articles"
          :key="article.id"
          :article="article"
          class="board_list_body1"
        />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";
import communityItem from "@/components/communityItem";
export default {
  name: "CommunityView",
  data() {
    return {

    };
  },
  computed: {
    articles() {
      return this.$store.state.articles;
    },    
  },
  components: {
    communityItem,
  },
  methods: {
    getArticle() {
      axios({
        method: "get",
        url: `${API_URL}/community/`,
      })
        .then((res) => {
          this.$store.state.articles = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    moveCreate() {
      if (!this.isLoggedIn) {
        alert("로그인 해주세요");
        this.$router.push("login");
        return;
      }
      this.$router.push("create");
    },
    isLogin() {
      if (window.localStorage.getItem("jwt")) {
        this.isLoggedIn = true;
      } else {
        this.isLoggedIn = false;
      }
    },
  },
  created() {
    this.isLogin();
    this.getArticle();
  },
};
</script>

<style>


.board_list_wrap {
  padding: 50px;
}
.board_list_head > div {
  display: inline-block;
  font-weight: 600;
}
.board_list_head {
  padding: 10px 0;
}
.board_list_body1 {
  display: block
}
.board_list_head .articles_title {
  text-align: center;
}
.articles_id {
  width: 10%;
}
.articles_title {
  width: 55%;
}
.articles_username {
  width: 10%;
}
.articles_created_at {
  width: 15%;
}
.articles_views {
  width: 10%;
}
</style>