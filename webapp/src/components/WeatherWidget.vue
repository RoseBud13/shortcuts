<template>
    <div class="weather-widget">
        <p>{{ city }}</p>
        <p>{{ weather }}</p>
        <span><i class="fas fa-cloud"></i></span>
    </div>
</template>

<script>
import { getWeatherInfo } from "../api";

export default {
    data() {
        return {
            city: '',
            weather: ''
        }
    },
    methods: {
        getWeather() {
            getWeatherInfo().then(response => {
                this.city = response.location;
                this.weather = response.weather_status;
            }).catch(error => {
                console.log(error);
            });
        }
    },
    created() {
        this.getWeather();
    }
}

</script>

<style>
.weather-widget {
    z-index: 1;
    width: 250px;
    height: 70px;
    background-color: rgba(221, 166, 157, 0.3);
    border-radius: 10px;
    position: fixed;
    top: 50px;
    right: 30px;
}
</style>
