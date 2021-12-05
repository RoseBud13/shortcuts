<template>
  <transition name="grow">
    <button
      class="floating-button"
      v-if="!!selected && !!editorType"
      :class="{ 'floating-button__editing': !!editing }"
      :style="{ background: gradientColor }"
      @click="toggleEditing"
    ></button>
  </transition>
</template>

<script>
import { mapState, mapGetters, mapMutations } from 'vuex'
export default {
  computed: {
    ...mapState(['selected', 'editing', 'editorType']),
    ...mapGetters(['currentSlider']),
    gradientColor () {
      const colorLeft = `color-stop(30%, ${this.currentSlider.colors[0]})`
      const colorRight = `to(${this.currentSlider.colors[1]})`
      return `-webkit-gradient(linear, left bottom, right top, ${colorLeft}, ${colorRight})`
    }
  },
  methods: {
    ...mapMutations(['toggleEditing'])
  }
}
</script>

<style lang="scss">
.floating-button {
  position: fixed;
  right: 44px;
  bottom: 64px;
  margin: 0;
  padding: 0;
  border: none;
  outline: none;
  border-radius: 44px;
  width: 44px;
  height: 44px;
  color: white;
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
  transition: all 0.5s ease;
  z-index: 2;
}
.floating-button::before,
.floating-button::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  display: block;
  width: 20px;
  height: 2px;
  background-color: white;
  transform: translate(-50%, -50%);
}
.floating-button::after {
  transform: translate(-50%, -50%) rotate(90deg);
}
.floating-button__editing {
  right: 0;
  bottom: 0;
  width: 100%;
  border-radius: 0;
}
.grow-leave-to,
.grow-enter {
  transform: scale(0);
}
.grow-enter-to,
.grow-leave {
  transform: scale(1);
}
.grow-enter-active {
  transition: all 0.2s 0.3s ease;
}
.grow-leave-active {
  transition: all 0.3s ease;
}
</style>
