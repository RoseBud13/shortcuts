<template>
    <div class="card-list">
        <li
            v-for="card in cards"
            :key="card.id"
        >
            <main-card v-show="card.cardType === 'main'" :cardStyle="card.cardStyle"></main-card>
            <cluster-card v-show="card.cardType === 'cluster'" :cardStyle="card.cardStyle"></cluster-card>
        </li>
    </div>
</template>

<script>
import MainCard from "./MainCard.vue";
import ClusterCard from "./ClusterCard.vue";

export default {
    components: {
        MainCard,
        ClusterCard
    },
    props: {
        cards: {
            type: Array,
            required: true
        }
    }
}

</script>

<style>
.card-list {
    align-items: center;
}
.card-list, li, ol {
    list-style: none;
}
</style>
