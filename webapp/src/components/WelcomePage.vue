<template>
    <div class="welcome-page">
        <!-- <div class="page-wrapper">
            <p>{{ this.$store.state.vehicleModel }}</p>
        </div> -->
        <weather-widget></weather-widget>
        <gradient></gradient>
        <slider-list></slider-list>
        <slider-detail></slider-detail>
        <slider-editing></slider-editing>
        <floating-button></floating-button>
        <shortcuts-list></shortcuts-list>
    </div>
</template>

<script>
import WeatherWidget from "./WeatherWidget.vue"
import Gradient from "./Gradient.vue"
import SliderList from './SliderList.vue'
import SliderDetail from './SliderDetail.vue'
import SliderEditing from './SliderEditing.vue'
import FloatingButton from './FloatingButton.vue'
import ShortcutsList from './ShortcutsList.vue'

export default {
    components: {
        WeatherWidget,
        Gradient,
        SliderList,
        SliderDetail,
        SliderEditing,
        FloatingButton,
        ShortcutsList
    },
    data() {
        return {

        }
    },
    methods: {
    
    },
    created() {

    }
}

</script>

<style>
.welcome-page {
    /* z-index: -1; */
    width: 100vw;
    height: 100vh;
    overflow: hidden;
    /* background-color: rgb(240, 221, 215); */
}
.page-wrapper {
    width: 100%;
    height: 100%;
    /* background-image: url('../assets/img/XC60.jpg'); */
    background-size: 100% auto;
    background-repeat: no-repeat;
    background-position: left top;
}
</style>
