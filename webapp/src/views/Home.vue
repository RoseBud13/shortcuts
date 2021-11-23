<template>
    <div class="home">
        <div class="hidden-tools">
            <button @click="getCardStyle">Get Cards</button>
        </div>
        <card-list v-if="showCards" :cards="cards"></card-list>
    </div>
</template>

<script>
import CardList from "../components/CardList.vue"
import { fetchCardStyle } from "../api"

export default {
    components: {
        CardList
    },
    data() {
        return {
            showCards: false,
            cards: [
                // {
                //     id: 1,
                //     cardType: 'main',
                //     cardStyle: {
                //         cardBgColor: 'yellow',
                //         cardBgOpacity: 0.5,
                //         cardHeight: '200px'
                //     }
                // },
                // {
                //     id: 2,
                //     cardType: 'main',
                //     cardStyle: {
                //         cardBgColor: 'blue',
                //         cardBgOpacity: 0.5,
                //         cardHeight: '150px'
                //     }
                // },
                // {
                //     id: 3,
                //     cardType: 'cluster',
                //     cardStyle: {
                //         cardBgColor: 'pink',
                //         cardBgOpacity: 0.5,
                //         cardHeight: '160px'
                //     }
                // },
                // {
                //     id: 4,
                //     cardType: 'main',
                //     cardStyle: {
                //         cardBgColor: 'black',
                //         cardBgOpacity: 0.5,
                //         cardHeight: '170px'
                //     }
                // },
                // {
                //     id: 5,
                //     cardType: 'main',
                //     cardStyle: {
                //         cardBgColor: 'green',
                //         cardBgOpacity: 0.5,
                //         cardHeight: '300px'
                //     }
                // }
            ],
        }
    },
    methods: {
        getCardStyle() {
            fetchCardStyle().then(response => {
                this.cards = response.cards;
                this.showCards = true;
            })
        }
    }
}

</script>

<style>
.home {
    overflow: hidden;
}
.hidden-tools {
    z-index: -1;
}
</style>
