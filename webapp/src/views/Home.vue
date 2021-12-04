<template>
    <div class="home">
        <welcome-page></welcome-page>
        <base-card></base-card>
        <card-list-detail></card-list-detail>
        <!-- <card-list v-if="showCards" :cards="cardsData"></card-list> -->
    </div>
</template>

<script>
import WelcomePage from '../components/WelcomePage.vue'
import BaseCard from '../components/BaseCard.vue'
import CardListDetail from '../components/CardListDetail.vue'

export default {
    components: {
        WelcomePage,
        BaseCard,
        CardListDetail
    },
    data() {
        return {
            // showCards: false,
            // cardsData: []
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
        // ...mapMutations(['setVehicleModel']),

        // getCardStyle() {
        //     fetchCardStyle().then(response => {
        //         this.cardsData = response.cardsInfo;
        //     }).catch(error => {
        //         console.log(error);
        //     });
        // },

        // getCar() {
        //     fetchCar().then(response => {
        //         var carModel = response.carModel;
        //         this.setVehicleModel(carModel);
        //     }).catch(error => {
        //         console.log(error);
        //     });
        // }
    },
    created() {
        // this.getCardStyle();
        // this.getCar();
    }
}

</script>

<style>
.home {
    overflow: hidden;
}
.home body {
    overflow: hidden;
}
</style>
