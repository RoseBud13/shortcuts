<template>
  <div class="gradient">
    <gradient-color
      v-for="(slider, index) in sliders"
      :key="slider.name"
      :colors="slider.colors"
      :active="index <= currentIndex"
    />
  </div>
</template>

<script>
import { mapState } from 'vuex'
import GradientColor from './GradientColor.vue'
export default {
  components: {
    GradientColor
  },
  computed: {
    ...mapState(['sliders', 'currentIndex'])
  }
}
</script>

<style lang="scss">
.gradient {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: -1;
}
</style>
