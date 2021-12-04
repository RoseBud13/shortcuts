<template>
  <transition name="show" @enter="handleEnter" @leave="handleLeave">
    <div class="slider-detail" v-if="selected">
      <app-bar :title="selected.slider.name" @left="unselectSlider" />
      <slider :slider="selected.slider" :active="true" @close="unselectSlider" />
    </div>
  </transition>
</template>

<script>
import { mapState, mapMutations } from 'vuex'
import AppBar from './AppBar.vue'
import Slider from './Slider.vue'
export default {
  components: {
    AppBar,
    Slider
  },
  computed: {
    ...mapState(['selected', 'unselect'])
  },
  methods: {
    ...mapMutations(['unselectSlider']),
    handleEnter (el) {
      Object.assign(el.style, {
        top: `${this.selected.rect.top}px`,
        left: `${this.selected.rect.left}px`,
        width: `${this.selected.rect.width}px`,
        height: `${this.selected.rect.height}px`
      })
      setTimeout(() => {
        Object.assign(el.style, {
          top: 0,
          left: 0,
          width: `${this.selected.rect.appWidth}px`,
          height: `${this.selected.rect.appHeight}px`
        })
      }, 0)
    },
    handleLeave (el) {
      Object.assign(el.style, {
        top: 0,
        left: 0,
        width: `${this.unselect.rect.appWidth}px`,
        height: `${this.unselect.rect.appHeight}px`
      })
      setTimeout(() => {
        Object.assign(el.style, {
          top: `${this.unselect.rect.top}px`,
          left: `${this.unselect.rect.left}px`,
          width: `${this.unselect.rect.width}px`,
          height: `${this.unselect.rect.height}px`
        })
      }, 0)
    }
  }
}
</script>

<style lang="scss">
.slider-detail {
  position: fixed;
  display: flex;
  flex-direction: column;
  border-radius: 0;
  background-color: white;
  color: #666;
  will-change: top, left, width, height;
  z-index: 2;

  .slider {
    margin: 0;
    margin-top: -80px;
    padding: 0 20px;
    box-shadow: none;
  }
  .slider_head,
  .slider_body {
    transform: translate3d(0, 88px, 0);
  }
  .slider_menu {
    opacity: 0;
  }
  // .slider_tasks {
  //   opacity: 1;
  //   transform: scaleY(1);
  // }
  .app-bar {
    opacity: 1;
    transform: translate3d(0, 0, 0);
  }
}
.show-enter-to,
.show-leave {
  border-radius: 0;

  .slider {
    padding: 0 20px;
  }
  .slider_head,
  .slider_body {
    transform: translate3d(0, 88px, 0);
  }
  .slider_menu {
    opacity: 0;
  }
  // .slider_tasks {
  //   opacity: 1;
  //   transform: scale3d(1, 1, 1);
  // }
  .app-bar {
    opacity: 1;
    transform: translate3d(0, 0, 0);
  }
}
.show-leave-to,
.show-enter {
  border-radius: 8px;

  .slider {
    padding: 0;
  }
  .slider_head {
    transform: translate3d(0, 0, 0);
  }
  .slider_body {
    transform: translate3d(0, 189px, 0);
  }
  .slider_menu {
    opacity: 1;
  }
  // .slider_tasks {
  //   opacity: 0;
  //   transform: scale3d(1, 0, 1);
  // }
  .app-bar {
    opacity: 0;
    transform: translate3d(0, -100%, 0);
  }
}
.show-enter-active,
.show-leave-active {
  transition: all 0.5s ease;

  .slider,
  .slider_head,
  .slider_body,
  .slider_menu,
  // .slider_tasks,
  .app-bar {
    transition: all 0.5s ease;
  }
}
</style>
