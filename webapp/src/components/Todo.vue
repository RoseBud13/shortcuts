<template>
    <div class="todo">
        <p class="todo_tips">{{ content.tasks.length }} Tasks</p>
        <div class="todo_progress">
            <span class="todo_progress_line">
                <i :style="{ width: progress, backgroundImage: progressColor }"></i>
            </span>
            <span class="todo_progress_num">{{ progress }}</span>
        </div>
        <div class="todo_tasks">
            <h4 class="todo_subtitle" v-if="todayTasks.length">Today</h4>
            <ul>
                <li v-for="task in todayTasks" :key="task.id">
                    <task :content="content" :task="task" />
                </li>
            </ul>
            <h4 class="todo_subtitle" v-if="tomorrowTasks.length">Tomorrow</h4>
            <ul>
                <li v-for="task in tomorrowTasks" :key="task.id">
                    <task :content="content" :task="task" />
                </li>
            </ul>
            <h4 class="todo_subtitle" v-if="outdatedTasks.length">Outdated</h4>
            <ul>
                <li v-for="task in outdatedTasks" :key="task.id">
                    <task :content="content" :task="task" />
                </li>
            </ul>
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
    content: {
      type: Object,
      required: true
    }
  },
  computed: {
    progress () {
      const totalCount = this.content.tasks.filter(t => !t.deleted).length
      const doneCount = this.content.tasks.filter(t => !t.deleted && t.done).length
      return `${Math.round((doneCount / totalCount) * 100)}%`
    },
    progressColor () {
      const colorLeft = `color-stop(30%, ${this.content.colors[0]})`
      const colorRight = `to(${this.content.colors[1]})`
      return `-webkit-gradient(linear, left bottom, right bottom, ${colorLeft}, ${colorRight})`
    },
    todayTasks () {
      return this.content.tasks.filter(task => {
        return task.date >= today && task.date < tomorrow
      })
    },
    tomorrowTasks () {
      return this.content.tasks.filter(task => {
        return task.date >= tomorrow
      })
    },
    outdatedTasks () {
      return this.content.tasks.filter(task => {
        return task.date < today
      })
    }
  },
}
</script>

<style lang="scss">
.todo_tips {
  opacity: 0.6;
  font-size: 13px;
  font-weight: 600;
}
.todo_title {
  margin-top: 6px;
  font-size: 32px;
}
.todo_progress {
  display: flex;
  align-items: center;
  margin-top: 30px;
}
.todo_progress_line {
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
.todo_progress_num {
  font-size: 12px;
}
.todo_tasks {
  opacity: 1;
  transform: scaleY(1);
  // opacity: 0;
  // transform: scale3d(1, 0, 1);
  // transform-origin: top;
  // will-change: transform opacity;
}
.todo_subtitle {
  margin-top: 32px;
  margin-bottom: 8px;
  color: #999;
}
</style>
