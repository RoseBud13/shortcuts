<template>
  <transition name="edit">
    <div class="slider-editing" v-if="!!editing">
      <todo-editor v-show="editorType === 'todo'"></todo-editor>
      <shortcuts-editor v-show="editorType === 'shortcuts'"></shortcuts-editor>
    </div>
  </transition>
</template>

<script>
import { mapState } from 'vuex'
import TodoEditor from "./TodoEditor.vue"
import ShortcutsEditor from './ShortcutsEditor.vue'

export default {
  components: {
    TodoEditor,
    ShortcutsEditor
  },
  computed: {
    ...mapState(['editing', 'editorType'])
  },
}
</script>

<style lang="scss">
.slider-editing {
  position: fixed;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  border-radius: 0;
  background-color: white;
  color: #666;
  will-change: transform;
  z-index: 2;
}
.edit-leave-to,
.edit-enter {
  transform: translateY(100%);
}
.edit-enter-to,
.edit-leave {
  transform: translateY(0);
}
.edit-enter-active {
  transition: all 0.5s ease;
}
.edit-leave-active {
  transition: all 0.5s ease;
}
</style>
