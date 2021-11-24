<template>
    <div class="home">
        <card-list v-if="showCards" :cards="cardsData"></card-list>
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
            showCards: true,
            cardsData: []
                // {
                //     id: 1,
                //     cardType: 'main',
                //     cardStyle: {
                //         cardBgColor: 'yellow',
                //         cardBgOpacity: 0.5,
                //         cardHeight: '100px'
                //     }
                // },
                // {
                //     id: 2,
                //     cardType: 'main',
                //     cardStyle: {
                //         cardBgColor: 'red',
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
        }
    },
    methods: {
        getCardStyle() {
            fetchCardStyle().then(response => {
                this.cardsData = response.cardsInfo;
            }).catch(error => {
                console.log(error);
            });
        }
    },
    created() {
        this.getCardStyle();
    }
}

</script>

<style>
.home {
    overflow: hidden;
}
</style>
