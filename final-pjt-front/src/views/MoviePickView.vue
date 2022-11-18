<template>
  <div>
    <h1>영화 추천해주는 페이지</h1>
    <h3>설명란</h3>
    <v-row justify="center" class="mt-5">
      <v-dialog
        v-model="dialog"
        hide-overlay
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
            <v-btn
              @click="clicked.clicked1 = !clicked.clicked1"
              :color="
                clicked.clicked1
                  ? 'deep-purple darken-1'
                  : 'deep-purple lighten-3'
              "
              rounded
            >
              우울한
            </v-btn>
            <v-btn
              @click="clicked.clicked2 = !clicked.clicked2"
              :color="
                clicked.clicked2
                  ? 'deep-purple darken-1'
                  : 'deep-purple lighten-3'
              "
              rounded
            >
              그리운
            </v-btn>
            <v-btn
              @click="clicked.clicked3 = !clicked.clicked3"
              :color="
                clicked.clicked3
                  ? 'deep-purple darken-1'
                  : 'deep-purple lighten-3'
              "
              rounded
            >
              낙심한
            </v-btn>
            <v-btn
              @click="clicked.clicked4 = !clicked.clicked4"
              :color="
                clicked.clicked4
                  ? 'deep-purple darken-1'
                  : 'deep-purple lighten-3'
              "
              rounded
            >
              외로운
            </v-btn>
            <v-btn
              @click="clicked.clicked5 = !clicked.clicked5"
              :color="
                clicked.clicked5
                  ? 'deep-purple darken-1'
                  : 'deep-purple lighten-3'
              "
              rounded
            >
              좋은
            </v-btn>
            <v-btn
              @click="clicked.clicked6 = !clicked.clicked6"
              :color="
                clicked.clicked6
                  ? 'deep-purple darken-1'
                  : 'deep-purple lighten-3'
              "
              rounded
            >
              재밌는
            </v-btn>
            <v-btn
              @click="clicked.clicked7 = !clicked.clicked7"
              :color="
                clicked.clicked7
                  ? 'deep-purple darken-1'
                  : 'deep-purple lighten-3'
              "
              rounded
            >
              벅찬
            </v-btn>
            <v-btn
              @click="clicked.clicked8 = !clicked.clicked8"
              :color="
                clicked.clicked8
                  ? 'deep-purple darken-1'
                  : 'deep-purple lighten-3'
              "
              rounded
            >
              활기찬
            </v-btn>
          </v-list-item>
        </v-card>
      </v-dialog>
    </v-row>
    <br />
    <br />
    <moviePickitem />
  </div>
</template>

<script>
import moviePickitem from "@/components/moviePickitem";
import _ from "lodash"
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
          console.log(count)
          const recommendedMovie =  _.cloneDeep(this.classifyMovie[id])
          recommendedMovie.splice(count)
          for (let movie of recommendedMovie){
            this.recommendMovie.push(movie)
          }
        }
      }
      this.dialog = false;
      console.log(this.recommendMovie);
    },
  },
  components: {
    moviePickitem,
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
      },
      moods: {
        35: ["clicked1", "clicked2", "clicked3", "clicked4"],
        28: ["clicked5", "clicked6", "clicked7", "clicked8"],
      },
      moodsCount: {
        35: 0,
        28: 0,
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