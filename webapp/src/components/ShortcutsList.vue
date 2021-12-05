<template>
    <div class="shortcuts-list" v-show="showScList">
        <div class="header-bar">
            <div class="bar"></div>
        </div>
        <div class="function-items">
            <func-module></func-module>
            <func-module></func-module>
            <func-module></func-module>
            <func-module></func-module>
            <func-module></func-module>
            <func-module></func-module>
            <func-module></func-module>
            <func-module></func-module>
            <func-module></func-module>
            <func-module></func-module>
            <func-module></func-module>
            <func-module></func-module>
        </div>
    </div>
</template>

<script>
import { mapState } from 'vuex'
import FuncModule from './FuncModule.vue'

export default {
    components: {
        FuncModule
    },
    computed: {
        ...mapState(['showScList'])
    }
}

</script>

<style>
.shortcuts-list {
    width: 100vw;
    height: 100%;
    position: fixed;
    top: 300px;
    background-color: #e8e7e7;
    border-radius: 30px 30px 0 0;
    z-index: 3;
}
.header-bar {
    height: 50px;
    width: 100%;
}
.header-bar .bar {
    width: 70%;
    height: 7px;
    margin: auto;
    transform: translateY(20px);
    background-color: rgb(253, 254, 255);
    border-radius: 7px;
}
.function-items {
    overflow : scroll;
    height: 530px;
}
</style>
