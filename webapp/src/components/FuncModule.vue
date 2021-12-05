<template>
    <div class="func-module" @click="openScBuilder(); collectMethods(); toggleScList()">
        <div class="func-item">
            <div class="item-content">
                {{ methName }}
            </div>
        </div>
    </div>
</template>

<script>
import { mapMutations } from 'vuex'

export default {
    props: {
        methName: {
            type: String,
            required: true
        }
    },
    methods: {
        ...mapMutations(['openScBuilder', 'toggleScList', 'buildShortcuts']),

        collectMethods() {
            this.buildShortcuts(this.methName)
        }
    }
}

</script>

<style>
.func-module {
    width: 100%;
    height: 60px;
}
.func-item {
    margin: 0 auto;
    width: 90%;
    height: 50px;
    background-color: #ffffff;
    border-radius: 15px;
    text-align: center;
}
.item-content {
    font-size: 25px;
    padding-top: 12px;
    color: rgb(80, 80, 80);
}
</style>