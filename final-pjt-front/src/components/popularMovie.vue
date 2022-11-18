<template>
	<div>
		<h1>PopularMovie</h1>
  <v-row class="d-flex justify-center">
  <v-carousel height="1000" class="popular-movie-carousel" col=10 style="z-index: 0">
    <v-carousel-item style="z-index:1"
      v-for="popularMovie in popularMovies"
      :key="popularMovie.id"
      
      reverse-transition="fade-transition"
      transition="fade-transition"
    ><v-hover>
      <template>
        <v-card
          class="mx-auto"
          max-width="auto"
          max-height="auto"
        >
          <div>
          <v-img  v-on:click.native='openModal' class="d-flex" :src="'https://image.tmdb.org/t/p/original' + popularMovie.backdrop_path" style="object-fit:cover">
          <v-btn class="d-flex align-self-end mt-5" text color="white" >
            <h1>{{popularMovie.title}}</h1>
            </v-btn>
          </v-img>
          </div>
          <!-- 여기부턴 모달 -->
          <div class='popular-modal'  :class="{hidden:showModal}">
            <div class='modal_overlay' @click="closeModal"></div>
            <div class="modal_content">
              <h1> {{popularMovie.title}} </h1>
              <v-row class="mt-3">
                <v-col cols="6">
                  <span v-for="(genre, index) in popularMovie.genre_ids" :key="index">{{genre}}      </span>
                  <p>{{popularMovie.overview}}</p>
                </v-col>
                <v-col cols="6">
                  <img :src="'https://image.tmdb.org/t/p/original' + popularMovie.poster_path" alt="" class="modalimg">
                </v-col>
              </v-row>
            </div>
          </div>
        </v-card>
      </template>
    </v-hover>
    
  </v-carousel-item>
  </v-carousel>
</v-row>

    <!-- <p>{{ popularMovies }}</p> -->
	</div>
</template>

<script>
// import popularMovieitem from '@/components/popularMovieitem';

export default {
	name:'popularMovie',
  data() {
    return {
      isModalviewed:false,
      showModal:false

    }
  },
  components:{
    // popularMovieitem

  },
  computed:{
    popularMovies() {
      return this.$store.state.top10Movie
    }
  },
  methods:{
    openModal() {
      this.showModal = false
    },
    closeModal() {
      this.showModal = true
      console.log()
    }
  }
}
</script>

<style>
.btnsize{
  font-size: 3rem;
}
.popular-movie-carousel{
  height: 1000px;
  width: 1777px;
  ;
}
.popular-modal{
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  
}
.modal_overlay{
  background-color: rgba(0, 0, 0, 0.6);
  width: 100%;
  height: 100%;
  position: absolute;
}
.modal_content{
  background-color: white;
  padding: 50px;
  text-align: center;
  position: relative;
  width: 90%;
  top: 0px;
  border-radius: 10px;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.19), 0, 6px 6px rgba(0, 0, 0, 0.23);
  z-index: 2;
}
.hidden{
  display:none
}
.modalimg{
  width: 500px;
  
}

</style>