<template>
    <div class="shortcuts">
        <li v-for="shortcut in content.shortcutsInfo" :key="shortcut.id">
            <cluster-card :cardStyle="shortcut.cardStyle" :temp_name="shortcut.name"></cluster-card>
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
.shortcuts {
    width: 100%;
    border: none;
    margin: 30px auto;
    display: flex;
    flex-wrap: wrap;
    justify-content: flex-start;
}

</style>
