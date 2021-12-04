<template>
  <div class="slider" :class="{ slider__selected: selected }">
    <div class="slider_head" @click="handleClick">
      <div class="slider_icon" :style="{ color }">
        <i :class="['fa', `fa-${slider.icon}`]"></i>
      </div>
      <div class="slider_menu"><i class="fa fa-ellipsis-v"></i></div>
    </div>
    <div class="slider_body">
      <p class="slider_tips">{{ slider.tasks.length }} Tasks</p>
      <h3 class="slider_title">{{ slider.name }}</h3>
      <div class="slider_progress">
        <span class="slider_progress_line">
          <i :style="{ width: progress, backgroundImage: progressColor }"></i>
        </span>
        <span class="slider_progress_num">{{ progress }}</span>
      </div>
      <div class="slider_tasks">
        <h4 class="slider_subtitle" v-if="todayTasks.length">Today</h4>
        <ul>
          <li v-for="task in todayTasks" :key="task.id">
            <task :slider="slider" :task="task" />
          </li>
        </ul>
        <h4 class="slider_subtitle" v-if="tomorrowTasks.length">Tomorrow</h4>
        <ul>
          <li v-for="task in tomorrowTasks" :key="task.id">
            <task :slider="slider" :task="task" />
          </li>
        </ul>
        <h4 class="slider_subtitle" v-if="outdatedTasks.length">Outdated</h4>
        <ul>
          <li v-for="task in outdatedTasks" :key="task.id">
            <task :slider="slider" :task="task" />
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import Task from './Task.vue'
import { today, tomorrow } from '../utils/timechecker'
export default {
  components: {
    Task
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
    },
    progress () {
      const totalCount = this.slider.tasks.filter(t => !t.deleted).length
      const doneCount = this.slider.tasks.filter(t => !t.deleted && t.done).length
      return `${Math.round((doneCount / totalCount) * 100)}%`
    },
    progressColor () {
      const colorLeft = `color-stop(30%, ${this.slider.colors[0]})`
      const colorRight = `to(${this.slider.colors[1]})`
      return `-webkit-gradient(linear, left bottom, right bottom, ${colorLeft}, ${colorRight})`
    },
    todayTasks () {
      return this.slider.tasks.filter(task => {
        return task.date >= today && task.date < tomorrow
      })
    },
    tomorrowTasks () {
      return this.slider.tasks.filter(task => {
        return task.date >= tomorrow
      })
    },
    outdatedTasks () {
      return this.slider.tasks.filter(task => {
        return task.date < today
      })
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
  padding: 0 20px;
  transform: translate3d(0, 189px, 0);
  will-change: transform;
}
.slider_icon {
  display: flex;
  width: 44px;
  height: 44px;
  border: 1px solid #eee;
  border-radius: 100%;
  justify-content: center;
  align-items: center;
  font-size: 18px;
}
.slider_menu {
  color: #eee;
}
.slider_tips {
  opacity: 0.6;
  font-size: 13px;
  font-weight: 600;
}
.slider_title {
  margin-top: 6px;
  font-size: 32px;
}
.slider_progress {
  display: flex;
  align-items: center;
  margin-top: 30px;
}
.slider_progress_line {
  margin-right: 10px;
  flex: 1;
  height: 3px;
  background-color: #eee;

  i {
    display: block;
    height: 100%;
    transition: all 0.3s ease;
  }
}
.slider_progress_num {
  font-size: 12px;
}
.slider_tasks {
  opacity: 0;
  transform: scale3d(1, 0, 1);
  // transform-origin: top;
  // will-change: transform opacity;
}
.slider_subtitle {
  margin-top: 32px;
  margin-bottom: 8px;
  color: #999;
}
</style>
