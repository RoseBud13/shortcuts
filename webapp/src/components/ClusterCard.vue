<template>
    <div class="cluster-card" :style="getCardStyle" @click="doExecution">
        <div class="card-name">
            <p>{{ temp_name }}</p>
        </div>
    </div>
</template>

<script>
import { executeTemplate } from "../api"

export default {
    props: {
        cardStyle: {
            type: Object,
            required: true
        },
        temp_name: {
            type: String,
            required: true
        }
    },
    data() {
        return {
            temp: this.temp_name
        }
    },
    computed: {
        getCardStyle() {
            return {
                '--bg-color': this.cardStyle.cardBgColor,
                '--bg-opacity': this.cardStyle.cardBgOpacity,
                '--card-height': this.cardStyle.cardHeight
            }
        }
    },
    methods: {
        doExecution() {
            executeTemplate(this.temp).then(response => {
                console.log(response)
            })
        }
    }
}

</script>

<style lang="scss">
.cluster-card {
    width: 170px;
    height: var(--card-height);
    margin: 10px 7px;
    background-color: var(--bg-color);
    opacity: var(--bg-opacity);
    border-radius: 20px;
}
.card-name {
    width: 100%;
    height: 30px;
    position: relative;
    top: 50px;
    left: 20px;
    color: black;
}
.card-name p {
    font-size: 23px;
}
</style>
