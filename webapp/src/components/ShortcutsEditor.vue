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
            <textarea rows="1" v-model="tempName" placeholder="add name"></textarea>
            <shortcuts-builder></shortcuts-builder>
            <div class="add-button" @click="toggleScList(); setName()" >
              <p>select methods</p>
            </div>
        </div>
    </div>
</template>

<script>
import AppBar from './AppBar.vue'
import ShortcutsBuilder from './ShortcutsBuilder.vue'

import { mapState, mapMutations } from 'vuex'

export default {
    components: {
        AppBar,
        ShortcutsBuilder
    },
    data() {
      return {
        tempName: ''
      }
    },
    computed: {
        ...mapState(['selected', 'showScList'])
    },
    methods: {
        ...mapMutations(['toggleEditing', 'toggleScList', 'setBuilderName']),

        setName() {
          this.setBuilderName(this.tempName)
        }
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
.add-button {
  margin-top: 10px;
  width: 100%;
  height: 30px;
  background-color: rgb(215, 215, 215);
  border-radius: 5px;
  color: black;
  text-align: center;
}
.add-button p {
  padding-top: 2px;
  font-size: 20px;
}
</style>