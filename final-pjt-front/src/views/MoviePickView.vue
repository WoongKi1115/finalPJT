<template>
  <div>
    <h1>영화 추천해주는 페이지</h1>
    <h3>설명란</h3>
    <v-row justify="center" class="mt-5">
      <v-dialog
        v-model="dialog"
        hide-overlay
        height="auto"
        transition="dialog-bottom-transition"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            color="deep-purple darken-1"
            dark
            v-bind="attrs"
            v-on="on"
            @click="resetMoods"
          >
            추천받으러가기
          </v-btn>
        </template>
        <v-card>
          <v-toolbar dark color="deep-purple darken-1">
            <v-btn icon dark @click="dialog = false">
              <v-icon>mdi-close</v-icon>
            </v-btn>
            <v-toolbar-title>오늘의 기분</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-toolbar-items>
              <v-btn dark text @click="[save()]"> Save </v-btn>
            </v-toolbar-items>
          </v-toolbar>
          <v-list-item>
            <v-row class="d-flex justify-space-around mb-6">
              <v-btn
              @click="clicked.clicked1 = !clicked.clicked1"
              :color="
                clicked.clicked1
                ? 'deep-purple lighten-1'
                  : 'deep-purple lighten-4'
                  "
              rounded
            >
              신나는
            </v-btn>
            <v-btn
            @click="clicked.clicked2 = !clicked.clicked2"
              :color="
                clicked.clicked2
                  ? 'deep-purple lighten-1'
                  : 'deep-purple lighten-4'
                  "
              rounded
            >
              활기찬
            </v-btn>
            <v-btn
            @click="clicked.clicked3 = !clicked.clicked3"
              :color="
                clicked.clicked3
                  ? 'deep-purple lighten-1'
                  : 'deep-purple lighten-4'
              "
              rounded
            >
              지루한
            </v-btn>
            <v-btn
              @click="clicked.clicked4 = !clicked.clicked4"
              :color="
                clicked.clicked4
                  ? 'deep-purple lighten-1'
                  : 'deep-purple lighten-4'
              "
              rounded
            >
            자랑스러운
            </v-btn>
            <v-btn
              @click="clicked.clicked5 = !clicked.clicked5"
              :color="
                clicked.clicked5
                ? 'deep-purple lighten-1'
                : 'deep-purple lighten-4'
                "
              rounded
              >
              자신감넘치는
            </v-btn>
            <v-btn
            @click="clicked.clicked6 = !clicked.clicked6"
            :color="
                clicked.clicked6
                ? 'deep-purple lighten-1'
                  : 'deep-purple lighten-4'
                  "
              rounded
              >
              답답한
            </v-btn>
            <v-btn
              @click="clicked.clicked7 = !clicked.clicked7"
              :color="
                clicked.clicked7
                  ? 'deep-purple lighten-1'
                  : 'deep-purple lighten-4'
              "
              rounded
            >
            우울한
            </v-btn>
            <v-btn
              @click="clicked.clicked8 = !clicked.clicked8"
              :color="
                clicked.clicked8
                ? 'deep-purple lighten-1'
                : 'deep-purple lighten-4'
                "
              rounded
            >
              웃음이필요한
            </v-btn>
            <v-btn
            @click="clicked.clicked9 = !clicked.clicked9"
            :color="
                clicked.clicked9
                ? 'deep-purple lighten-1'
                  : 'deep-purple lighten-4'
              "
              rounded
              >
              짜증나는
            </v-btn>
            <v-btn
              @click="clicked.clicked10 = !clicked.clicked10"
              :color="
                clicked.clicked10
                ? 'deep-purple lighten-1'
                  : 'deep-purple lighten-4'
              "
              rounded
              >
              통쾌한
            </v-btn>
            <v-btn
            @click="clicked.clicked11 = !clicked.clicked11"
              :color="
                clicked.clicked11
                  ? 'deep-purple lighten-1'
                  : 'deep-purple lighten-4'
              "
              rounded
              >
              억울한
            </v-btn>
            <v-btn
              @click="clicked.clicked12 = !clicked.clicked12"
              :color="
                clicked.clicked12
                  ? 'deep-purple lighten-1'
                  : 'deep-purple lighten-4'
              "
              rounded
            >
            행복한
          </v-btn>
            <v-btn
              @click="clicked.clicked13 = !clicked.clicked13"
              :color="
                clicked.clicked13
                  ? 'deep-purple lighten-1'
                  : 'deep-purple lighten-4'
              "
              rounded
              >
              편안한
            </v-btn>
            <v-btn
            @click="clicked.clicked14 = !clicked.clicked14"
            :color="
                clicked.clicked14
                ? 'deep-purple lighten-1'
                  : 'deep-purple lighten-4'
                  "
              rounded
            >
            속상한
            </v-btn>
            <v-btn
            @click="clicked.clicked15 = !clicked.clicked15"
            :color="
                clicked.clicked15
                  ? 'deep-purple lighten-1'
                  : 'deep-purple lighten-4'
              "
              rounded
            >
              몽환적인
            </v-btn>
            <v-btn
              @click="clicked.clicked16 = !clicked.clicked16"
              :color="
                clicked.clicked16
                ? 'deep-purple lighten-1'
                  : 'deep-purple lighten-4'
                  "
              rounded
              >
              현실에서 벗어나고픈
            </v-btn>
            <v-btn
            @click="clicked.clicked17 = !clicked.clicked17"
            :color="
                clicked.clicked17
                  ? 'deep-purple lighten-1'
                  : 'deep-purple lighten-4'
              "
              rounded
            >
              지긋지긋한
            </v-btn>
            <v-btn
              @click="clicked.clicked18 = !clicked.clicked18"
              :color="
                clicked.clicked18
                  ? 'deep-purple lighten-1'
                  : 'deep-purple lighten-4'
              "
              rounded
              >
              설레는
            </v-btn>
            <v-btn
            @click="clicked.clicked19 = !clicked.clicked19"
              :color="
                clicked.clicked19
                  ? 'deep-purple lighten-1'
                  : 'deep-purple lighten-4'
              "
              rounded
            >
              외로운
            </v-btn>
            <v-btn
              @click="clicked.clicked20 = !clicked.clicked20"
              :color="
                clicked.clicked20
                  ? 'deep-purple lighten-1'
                  : 'deep-purple lighten-4'
              "
              rounded
            >
            허전한
            </v-btn>
            <v-btn
            @click="clicked.clicked21 = !clicked.clicked21"
            :color="
                clicked.clicked21
                  ? 'deep-purple lighten-1'
                  : 'deep-purple lighten-4'
              "
              rounded
              >
              더운
            </v-btn>
            <v-btn
              @click="clicked.clicked22 = !clicked.clicked22"
              :color="
                clicked.clicked22
                  ? 'deep-purple lighten-1'
                  : 'deep-purple lighten-4'
              "
              rounded
            >
            흥분되는
          </v-btn>
        </v-row>
        </v-list-item>
      </v-card>
    </v-dialog>
  </v-row>
    <br />
    <br />
    <v-sheet
    class="mx-auto"
    max-width="1800"
  >
    <v-slide-group
      v-model="model"
      class="pa-4"
      active-class="success"
      show-arrows
    >
      <v-slide-item
        v-for="(rcdMovie, index) in recommendMovie"
        :key="index"
      >
        <v-card
          class="ma-4 pa-1"
          height="450"
          width="300"
        >
        <div class="text-center">
    <v-dialog

      width="1800"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-img
          
          v-bind="attrs"
          v-on="on"
          :src="'https://image.tmdb.org/t/p/original' + rcdMovie.poster_path"
        >
        </v-img>
      </template>

      <v-card >
        

        <v-card-text class="pa-5">
          <v-row>
            <v-col cols='5'>
              <v-img class="modalimage" :src="'https://image.tmdb.org/t/p/original' + rcdMovie.poster_path"></v-img>
            </v-col>
            <v-col cols='7'>
              <h1>{{rcdMovie.title}}</h1>
              <br>
              <br>
              <p>{{rcdMovie.overview}}</p>
            </v-col>
          </v-row>
        </v-card-text>
      </v-card>
    </v-dialog>
  </div>
        </v-card>
      </v-slide-item>
    </v-slide-group>
  </v-sheet>
  </div>
</template>

<script>
// import moviePickitem from "@/components/moviePickitem";
import _ from "lodash";
export default {
  name: "MoviePickView",
  methods: {
    resetMoods() {
      for (let id in this.clicked) {
        this.clicked[id] = false;
      }
      for (let id in this.moodsCount) {
        this.moodsCount[id] = 0;
      }
    },
    save() {
      this.clickedList = [];
      this.pickedMoods = [];
      for (let id in this.clicked) {
        let picked = this.clicked[id];
        if (picked) {
          this.clickedList.push(id);
        }
      }
      if (this.clickedList.length !== 5) {
        alert("지금 기분을 5개 선택해주세용");
        return;
      }
      for (let clickedKey of this.clickedList) {
        for (let id in this.moods) {
          let oneMoodList = this.moods[id];
          if (oneMoodList.includes(clickedKey)) {
            this.pickedMoods.push(id);
          }
        }
      }
      for (let pickedMood of this.pickedMoods) {
        this.moodsCount[pickedMood] += 1;
      }
      // console.log(this.moodsCount)
      for (let id in this.moodsCount) {
        let count = this.moodsCount[id];
        if (count) {
          const recommendedMovie = _.cloneDeep(this.classifyMovie[id]);
          recommendedMovie.splice(count);
          for (let movie of recommendedMovie) {
            this.recommendMovie.push(movie);
          }
        }
      }
      this.dialog = false;
      console.log(this.recommendMovie);
    },
  },
  components: {
    // moviePickitem,
  },
  computed: {
    classifyMovie() {
      return this.$store.state.classifiedMovie;
    },
  },
  data() {
    return {
      dialog: false,
      clickedCount: 0,
      clicked: {
        clicked1: false,
        clicked2: false,
        clicked3: false,
        clicked4: false,
        clicked5: false,
        clicked6: false,
        clicked7: false,
        clicked8: false,
        clicked9: false,
        clicked10: false,
        clicked11: false,
        clicked12: false,
        clicked13: false,
        clicked14: false,
        clicked15: false,
        clicked16: false,
        clicked17: false,
        clicked18: false,
        clicked19: false,
        clicked20: false,
        clicked21: false,
        clicked22: false,
      },
      moods: {
        28: ["clicked1", "clicked2", "clicked3"],
        12: ["clicked4", "clicked5", "clicked6"],
        35: ["clicked7", "clicked8", "clicked9"],
        80: ["clicked10", "clicked11"],
        10751: ["clicked12", "clicked13", "clicked14"],
        14: ["clicked15", "clicked16", "clicked17"],
        10749: ["clicked18", "clicked19", "clicked20"],
        53: ["clicked21", "clicked22"],
      },
      moodsCount: {
        28: 0,
        12: 0,
        35: 0,
        80: 0,
        10751: 0,
        14: 0,
        10749: 0,
        53: 0,
      },
      clickedList: [],
      pickedMoods: [],
      recommendMovie: [],
    };
  },
};
</script>

<style>
</style>