<template>
  <div>
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
  </div>
</template>

<script>
export default {
    name: 'modalView'
}
</script>

<style>

</style>