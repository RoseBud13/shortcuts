<template>
    <div class="home">
        <card-list :cards="cards"></card-list>
    </div>
</template>

<script>
import CardList from "../components/CardList.vue"

export default {
    components: {
        CardList
    },
    data() {
        return {
            cards: [
                {
                    id: 1,
                    cardType: 'main',
                    cardStyle: {
                        cardBgColor: 'yellow',
                        cardBgOpacity: 0.5,
                        cardHeight: '200px'
                    }
                },
                {
                    id: 2,
                    cardType: 'main',
                    cardStyle: {
                        cardBgColor: 'blue',
                        cardBgOpacity: 0.5,
                        cardHeight: '150px'
                    }
                },
                {
                    id: 3,
                    cardType: 'cluster',
                    cardStyle: {
                        cardBgColor: 'pink',
                        cardBgOpacity: 0.5,
                        cardHeight: '160px'
                    }
                },
                {
                    id: 4,
                    cardType: 'main',
                    cardStyle: {
                        cardBgColor: 'black',
                        cardBgOpacity: 0.5,
                        cardHeight: '170px'
                    }
                },
                {
                    id: 5,
                    cardType: 'main',
                    cardStyle: {
                        cardBgColor: 'green',
                        cardBgOpacity: 0.5,
                        cardHeight: '300px'
                    }
                }
            ],
        }
    }
}

</script>

<style>
.home {
    overflow: hidden;
}
</style>
