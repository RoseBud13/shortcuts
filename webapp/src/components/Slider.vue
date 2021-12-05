<template>
  <div class="slider" :class="{ slider__selected: selected }">
    <div class="slider_head" @click="handleClick">
      <div class="slider_icon" :style="{ color }">
        <i :class="['fas', `fa-${slider.icon}`]"></i>
      </div>
      <div class="slider_menu"><i class="fa fa-ellipsis-v"></i></div>
    </div>
    <div class="slider_body">
      <h3 class="slider_title">{{ slider.name }}</h3>
      <todo v-show="slider.type === 'todo'" :content="slider.content"></todo>
      <shortcuts v-show="slider.type === 'shortcuts'" :content="slider.content"></shortcuts>
    </div>
  </div>
</template>

<script>
import Todo from './Todo.vue'
import Shortcuts from './Shortcuts.vue'

export default {
  components: {
    Todo,
    Shortcuts
  },
  props: {
    slider: {
      type: Object,
      required: true
    },
    selected: {
      type: Boolean
    }
  },
  computed: {
    color () {
      return this.slider.colors[0]
    }
  },
  methods: {
    handleClick () {
      const appRect = document.querySelector('#app').getBoundingClientRect()
      const elRect = this.$el.getBoundingClientRect()
      const slider = this.slider
      const rect = {}
      rect.top = elRect.top - appRect.top
      rect.left = elRect.left - appRect.left
      rect.width = elRect.width
      rect.height = elRect.height
      rect.appWidth = appRect.width
      rect.appHeight = appRect.height
      this.$emit('select', { rect, slider })
      this.$store.state.editorType = this.slider.type
    }
  }
}
</script>

<style lang="scss">
.slider {
  flex: 1;
  margin: 0 8px;
  overflow: hidden;
  box-shadow: 0 10px 10px rgba(0, 0, 0, 0.2);
  color: #666;
}
.slider__selected {
  visibility: hidden;
}
.slider_head {
  display: flex;
  padding: 20px;
  height: 44px;
  justify-content: space-between;
  align-items: flex-start;
  transform: translate3d(0, 0, 0);
  will-change: transform;
}
.slider_body {
  transform: translate3d(0, 189px, 0);
  will-change: transform;
}
.slider_icon {
  display: flex;
  width: 44px;
  height: 44px;
  // border: 2px solid #eee;
  // border-radius: 100%;
  justify-content: center;
  align-items: center;
  font-size: 22px;
}
.slider_menu {
  color: #eee;
}
.slider_title {
  margin-top: 6px;
  font-size: 32px;
  padding: 0 20px;
}
</style>
