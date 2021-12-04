<template>
    <div class="shortcuts">
        <li v-for="shortcut in content.shortcutsInfo" :key="shortcut.id">
            <cluster-card :cardStyle="shortcut.cardStyle"></cluster-card>
        </li>
    </div>
</template>

<script>
import ClusterCard from "./ClusterCard.vue";

export default {
    components: {
        ClusterCard
    },
    props: {
        content: {
            type: Object,
            required: true
        }
    }
}

</script>

<style>

</style>
