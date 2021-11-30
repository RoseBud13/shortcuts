<template>
    <div class="main-card" :style="getCardStyle">
        <p>{{ cardContent.content }}</p>
    </div>
</template>

<script>
import { mapState } from 'vuex'
export default {
    props: {
        cardStyle: {
            type: Object,
            required: true
        }
    },
    computed: {
        getCardStyle() {
            return {
                '--bg-color': this.cardStyle.cardBgColor,
                '--bg-opacity': this.cardStyle.cardBgOpacity,
                '--card-height': this.cardStyle.cardHeight
            }
        },
        ...mapState(['cardContent'])
    }
}

</script>

<style lang="scss">
.main-card {
    background-color: var(--bg-color);
    opacity: var(--bg-opacity);
    height: var(--card-height);
    width: 350px;
    border-radius: 20px;
    margin: 30px auto;
    text-align: center;
}
.main-card p {
    font-size: 30px;
}
</style>
