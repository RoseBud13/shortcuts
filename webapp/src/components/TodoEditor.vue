<template>
    <div class="todo-editor">
        <app-bar title="New Tasks" left="times" @left="toggleEditing" />
        <div class="todo-editing_head">
            <p>What tasks are you planning to perform?</p>
        </div>
        <div class="todo-editing_body">
            <textarea rows="3" v-model="editing.text"></textarea>
            <p class="todo-editing_meta">
                <i :class="['fa', `fa-${selected.slider.icon}`]"></i>
                {{ selected.slider.name }}
            </p>
            <p class="todo-editing_meta">
                <i class="fa fa-calendar"></i>
                Today
            </p>
        </div>
    </div>
</template>

<script>
import AppBar from './AppBar.vue'
import { mapState, mapMutations } from 'vuex'

export default {
    components: {
        AppBar
    },
    computed: {
        ...mapState(['selected', 'editing'])
    },
    methods: {
        ...mapMutations(['toggleEditing'])
    }
}

</script>

<style lang="scss">
.todo-editor textarea {
  margin: 6px 0;
  border: none;
  outline: none;
  width: 100%;
  resize: none;
  // background: #eee;
  color: #666;
  font-size: 32px;
  line-height: 1.2em;
}
.todo-editing_head {
  padding: 40px 40px 0;
  color: #999;
}
.todo-editing_body {
  padding: 0 40px;
}
.todo-editing_meta {
  display: flex;
  height: 44px;
  align-items: center;
  border-bottom: 1px solid #eee;
  color: #999;

  i {
    padding-right: 10px;
  }
}
</style>
