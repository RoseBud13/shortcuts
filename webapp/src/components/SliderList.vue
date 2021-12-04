<template>
  <div class="slider-list" :class="{ 'slider-list__selected': !!selected }">
    <ul :style="{ width: `${sliders.length * 100}%` }">
      <li
        v-for="slider in sliders"
        :key="slider.name"
        :style="{ transform: `translate3d(-${currentIndex * 100}%, 0, 0)` }"
      >
        <slider
          :slider="slider"
          :selected="selected && slider === selected.slider"
          @select="selectSlider"
        />
      </li>
    </ul>
  </div>
</template>

<script>
import { mapState, mapMutations } from 'vuex'
import Slider from './Slider.vue'

export default {
  components: {
    Slider
  },
  mounted () {
    let touch = {}
    this.$el.addEventListener('touchstart', evt => {
      touch.startX = evt.touches[0].clientX
      touch.endX = 0
    })
    this.$el.addEventListener('touchmove', evt => {
      touch.endX = evt.touches[0].clientX
    })
    this.$el.addEventListener('touchend', () => {
      if (!touch.endX || Math.abs(touch.endX - touch.startX) < 10) {
        return
      }
      if (touch.endX < touch.startX) {
        this.nextSlider()
      } else {
        this.prevSlider()
      }
    })
  },
  computed: {
    ...mapState(['sliders', 'currentIndex', 'selected'])
  },
  methods: {
    ...mapMutations(['selectSlider', 'nextSlider', 'prevSlider'])
  }
}
</script>

<style lang="scss">
.slider-list {
  padding: 0 23px;
  height: 200px;
  transition: all 0.5s ease;
  margin-top: 55%;

  > ul,
  > ul > li {
    display: flex;
    height: 100%;
  }
  > ul > li {
    flex: 1;
    transition: transform 0.5s ease;
  }
  .slider {
    border-radius: 20px;
    background-color: white;
  }
}
.slider-list__selected {
  transform: scaleX(1.25);
}
</style>
