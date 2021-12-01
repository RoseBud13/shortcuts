import {createStore} from 'vuex'

export default createStore({
    state: {
        vehicleModel: '',
        landed: null,
        departured: null,
        show: true,
        cardContent: {
            content: 'data here'
        }
    },
    mutations: {
        setVehicleModel(state, model) {
            state.vehicleModel = model;
        },
        landedCon (state, landed) {
            state.departured = null
            state.landed = landed
            state.show = false
        },
        departuredCon (state) {
            state.departured = state.landed
            state.landed = null
            state.show = true
        },
    },
    actions: {},
    modules: {}
})
