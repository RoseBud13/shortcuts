<template>
    <div class="cluster-card" :style="getCardStyle">
        <div class="cluster-card-item1" :style="getCardStyle"></div>
        <div class="cluster-card-item2" :style="getCardStyle"></div>
    </div>
</template>

<script>
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
        }
    }
}

</script>

<style lang="scss">
.cluster-card {
    width: 350px;
    height: var(--card-height);
    border: none;
    margin: 30px auto;
    display: flex;
}
.cluster-card-item1 {
    width: 160px;
    height: var(--card-height);
    margin-right: 15px;
    background-color: var(--bg-color);
    opacity: var(--bg-opacity);
    border-radius: 20px;
}
.cluster-card-item2 {
    width: 160px;
    height: var(--card-height);
    margin-left: 15px;
    background-color: var(--bg-color);
    opacity: var(--bg-opacity);
    border-radius: 20px;
}
</style>
