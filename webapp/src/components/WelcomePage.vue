<template>
    <div class="welcome-page">
        <div class="page-wrapper">
            <p>{{ this.$store.state.vehicleModel }}</p>
        </div>
        <weather-widget></weather-widget>
    </div>
</template>

<script>
import WeatherWidget from "./WeatherWidget.vue"

export default {
    components: {
        WeatherWidget
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
    z-index: -1;
    width: 100vw;
    height: 100vh;
    overflow: hidden;
}
.page-wrapper {
    width: 100%;
    height: 100%;
    background-image: url('../assets/img/XC60.jpg');
    background-size: 100% auto;
    background-color: white;
    background-repeat: no-repeat;
    background-position: left top;
}
</style>
