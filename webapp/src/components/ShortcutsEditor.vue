<template>
    <div class="shortcuts-editor">
        <app-bar title="New Shortcuts" left="times" @left="toggleEditing" />
        <div class="shortcuts-editing_head">
            <p>What shortcuts are you planning to build?</p>
        </div>
        <div class="shortcuts-editing_body">
            <!-- <textarea rows="3" v-model="editing.text"></textarea> -->
            <p class="shortcuts-editing_meta">
                <i :class="['fa', `fa-${selected.slider.icon}`]"></i>
                {{ selected.slider.name }}
            </p>
            <p class="shortcuts-editing_meta">
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
.shortcuts-editor textarea {
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
.shortcuts-editing_head {
  padding: 40px 40px 0;
  color: #999;
}
.shortcuts-editing_body {
  padding: 0 40px;
}
.shortcuts-editing_meta {
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