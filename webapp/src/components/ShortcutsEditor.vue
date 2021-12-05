<template>
    <div class="shortcuts-editor">
        <app-bar title="New Shortcuts" left="times" @left="toggleEditing" />
        <div class="shortcuts-editing_head">
            <p>What shortcuts are you planning to build?</p>
        </div>
        <div class="shortcuts-editing_body">
            <p class="shortcuts-editing_meta">
                <i :class="['fa', `fa-${selected.slider.icon}`]"></i>
                {{ selected.slider.name }}
            </p>
            <div class="add-button" @click="toggleScList" >
              add
            </div>
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
    data() {
      return {

      }
    },
    computed: {
        ...mapState(['selected', 'editing', 'showScList'])
    },
    methods: {
        ...mapMutations(['toggleEditing', 'toggleScList'])
    }
}

</script>

<style lang="scss">
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
.add-buttton {
  width: 300px;
  height: 40px;
  background-color: #fff;
  color: black;
}
</style>