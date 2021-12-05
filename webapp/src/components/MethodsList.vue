<template>
    <transition name="edit">
        <div class="methods-list" v-show="showScList">
            <div class="header-bar" @click="toggleScList">
                <div class="bar"></div>
            </div>
            <div class="function-items">
                <li 
                    v-for="method in methods"
                    :key="method"
                >
                    <func-module :methName="method"></func-module>
                </li>
            </div>
        </div>
    </transition>
</template>

<script>
import { mapState, mapMutations } from 'vuex'
import { fetchAllMethods } from '../api'
import FuncModule from './FuncModule.vue'

export default {
    components: {
        FuncModule
    },
    data() {
        return {
            methods: []
        }
    },
    computed: {
        ...mapState(['showScList'])
    },
    methods: {
        ...mapMutations(['toggleScList']),

        getMethods() {
            fetchAllMethods().then(response => {
                this.methods = response.methods;
            }).catch(error => {
                console.log(error);
            });
        }
    },
    created() {
        this.getMethods()
    }
}

</script>

<style>
.methods-list {
    width: 100vw;
    height: 100%;
    position: fixed;
    top: 300px;
    background-color: #eceded;
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
    background-color: #f6fefb;
    border-radius: 7px;
}
.function-items {
    overflow : scroll;
    height: 530px;
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
  transition: all 0.9s ease;
}
.edit-leave-active {
  transition: all 0.9s ease;
}
</style>
