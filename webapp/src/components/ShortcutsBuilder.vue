<template>
    <div class="shortcuts-builder" v-show="showScBuilder">
        <li 
            v-for="method in selectedMethods"
            :key="method"
        >
            <func-module :methName="method"></func-module>
        </li>
    </div>
</template>

<script>
import FuncModule from './FuncModule.vue'
import { mapState } from 'vuex'

export default {
    components: {
        FuncModule
    },
    computed: {
        ...mapState(['showScBuilder', 'selectedMethods']),
    },
    methods: {

    }
}

</script>

<style>
.shortcuts-builder {
    margin-top: 20px;
    width: 100%;
    height: auto;
    background-color: #E2ECE9;
    border-radius: 20px;
    padding-top: 10px;
}

</style>
