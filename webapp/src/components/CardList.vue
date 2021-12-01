<template>
    <div class="card-list">
        <div class="greetings" v-show="$store.state.show">
            <h1>Hej Andy</h1>
            <h1>Your Volvo is ready!</h1>
        </div>
        <li
            v-for="card in cards"
            :key="card.id"
        >
            <main-card v-show="card.cardType === 'main'" :cardStyle="card.cardStyle"></main-card>
            <cluster-card v-show="card.cardType === 'cluster'" :cardStyle="card.cardStyle"></cluster-card>
        </li>
    </div>
</template>

<script>
import MainCard from "./MainCard.vue";
import ClusterCard from "./ClusterCard.vue";

export default {
    components: {
        MainCard,
        ClusterCard
    },
    props: {
        cards: {
            type: Array,
            required: true
        }
    },
    data() {
    return {
      startY: 0, // 触摸位置
      endY: 0, // 结束位置
      disY: 0, // 移动距离
    }
  },
  mounted () {
    this.$el.addEventListener('touchstart', evt => {
      this.startY = evt.targetTouches[0].clientY;
    });
    this.$el.addEventListener('touchmove', evt => {
      this.endY = evt.targetTouches[0].clientY;
    });
    this.$el.addEventListener('touchend', () => {
      this.disY = this.endY - this.startY;

      if (this.startY != Math.abs(this.disY)) {
        //在滑动的距离超过屏幕高度的20%时，做某种操作
        // console.log('滑动',Math.abs(distanceY))
        if (Math.abs(this.disY) > 20) {
          // console.log(this.disY)
          //向下滑实行函数someAction1，向上滑实行函数someAction2
          if (this.disY < 0) {
              this.handleLanding()
          }
        }
      }
      this.startY = 0;
      this.endY = 0;
    });
  },
  methods: {
    handleLanding () {
      const appRect = document.querySelector('#app').getBoundingClientRect()
      const elRect = this.$el.getBoundingClientRect()
      const continent = this.cards
      const rect = {}
      rect.top = elRect.top - appRect.top
      rect.left = elRect.left - appRect.left
      rect.width = elRect.width
      rect.height = elRect.height
      rect.appWidth = appRect.width
      rect.appHeight = appRect.height
      this.$emit('landing', { rect, continent })
    }
  }
}

</script>

<style>
.greetings {
    margin-top: 30px;
    margin-bottom: 70px;
}
.greetings h1 {
    font-size: 30px;
    margin: 10px;
}
.card-list {
    align-items: center;
    background-color: rgba(255, 255, 255, 0.5);
    overflow: auto;
}
.card-list, li, ol {
    list-style: none;
}
</style>
