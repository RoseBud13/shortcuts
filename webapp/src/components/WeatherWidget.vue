<template>
    <div class="weather-widget">
        <div class="status-item">
            <div class="status-item-content">{{ weather }}</div>
        </div>
        <div class="content-box">
            <div class="temp-item">
                <div class="temp-item-content">
                    {{ temp }}˚
                    <div class="seperator">|</div>
                </div>
            </div>
            <div class="locaton-item">
                <div class="location-item-content">
                    <div class="location-item-date">
                        {{dateTime }}
                    </div>
                    <div class="location-item-address">
                        <i class="fas fa-map-marker-alt"></i>
                        {{ city }}
                    </div>
                </div>
            </div>
            <div class="icon-item">
                <div class="icon-item-content">
                    <i :class="['fas', `fa-${weather_icon}`]"></i>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { getWeatherInfo, getDateInfo } from "../api";

export default {
    data() {
        return {
            dateTime: '',
            city: '',
            weather: '',
            temp: '',
            weather_icon: ''
        }
    },
    methods: {
        getDateTime() {
            getDateInfo().then(response => {
                this.dateTime = response.dateInfo;
            }).catch(error => {
                console.log(error);
            });
        },
        getWeather() {
            getWeatherInfo().then(response => {
                this.city = response.location;
                this.weather = response.weather_status;
                this.temp = response.weather_info.temp;
                this.setWeatherIcon(this.weather);
            }).catch(error => {
                console.log(error);
            });
        },
        setWeatherIcon(wt) {
            if ( wt === 'Clear' ) {
                this.weather_icon = 'sun';
            } else if ( wt === 'Clouds' ) {
                this.weather_icon = 'cloud';
            } else {
                console.log(wt);
            }
        }
    },
    created() {
        this.getDateTime();
        this.getWeather();
    }
}

</script>

<style>
.weather-widget {
    z-index: 0;
    width: 280px;
    height: 70px;
    background-color: rgba(200, 201, 199, 0.7);
    border-radius: 10px;
    position: fixed;
    top: 50px;
    right: 30px;
    box-shadow: 0 10px 10px rgba(0, 0, 0, 0.2);
}
.status-item {
    width: 100%;
    height: 20px;
}
.status-item-content {
    padding-left: 17px;
    padding-top: 5px;
    font-size: 15px;
}
.content-box {
    width: 100%;
    height: 50px;
    display: flex;
}
.temp-item {
    width: 100px;
    height: 50px;
    position: relative;
}
.temp-item-content {
    display: flex;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%,-50%);
    font-size: 22px;
}
.temp-item-content .seperator {
    margin-left: 5px;
}
.location-item {
    height: 50px;
    position: relative;
}
.location-item-content {
    padding-top: 10px;
}
.location-item-date {
    font-size: 10px;
}
.location-item-address {
    display: flex;
    font-size: 10px;
}
.location-item-address i {
    margin-right: 4px;
    padding-top: 2px;
}
.icon-item {
    height: 50px;
    position: relative;
}
.icon-item-content {
    font-size: 30px;
    color: yellow;
    position: relative;
    left: 40px;
}
</style>
