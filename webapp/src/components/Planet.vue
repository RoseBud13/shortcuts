<template>
  <div class="planet" v-show="$store.state.show">
    <div class="planet-container">
      <div class="planet-horizon">
        <!-- <img src="../assets/prince.png" alt=""> -->
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
.planet {
    width: 100vw;
    height: 100vh;
    overflow: hidden;
}
.planet-container {
    position: absolute;
    top: 80%;
    height: 100vh;
    width: 100vw;
}
.planet-horizon {
    height: 35px;
    width: 100%;
    background-color: rgb(255, 255, 255);
    border-radius: 50% 50% 0 0 / 50% 50% 0 0;
    border: 0;
    margin-bottom: -6px;
}
.planet-horizon img {
  width: 35%;
  position: absolute;
  left: 60%;
  transform: translateY(-65%)
}
</style>
