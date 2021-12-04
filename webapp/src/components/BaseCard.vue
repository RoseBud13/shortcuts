<template>
  <div class="base-card" v-show="$store.state.show">
    <div class="base-card-container">
      <div class="base-card-horizon">
        <img src="../assets/img/v90.png" alt="">
      </div>
      <card-list
          :cards="cardsData"
          @landing="landedCon"
        />
    </div>
  </div>
</template>

<script>
import { mapMutations } from 'vuex'
import CardList from './CardList.vue'
import { fetchCardStyle } from "../api"

export default {
  components: {
    CardList
  },
  data() {
    return {
      cardsData: []
    }
  },
  methods: {
    ...mapMutations(['landedCon']),

    getCardStyle() {
        fetchCardStyle().then(response => {
            this.cardsData = response.cardsInfo;
        }).catch(error => {
            console.log(error);
        });
    },
  },
  created() {
    this.getCardStyle();
  }
}
</script>

<style lang="scss">
.base-card {
    width: 100vw;
    height: 100vh;
    overflow: hidden;
    z-index: 1;
}
.base-card-container {
    position: absolute;
    top: 70%;
    height: 100vh;
    width: 100vw;
}
.base-card-horizon {
    height: 35px;
    width: 100%;
    background-color: rgb(255, 255, 255);
    border-radius: 50% 50% 0 0 / 50% 50% 0 0;
    border: 0;
    margin-bottom: -6px;
}
.base-card-horizon img {
  width: 80%;
  position: absolute;
  left: 1%;
  transform: translateY(-60%)
}
</style>
