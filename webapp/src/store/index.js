import {createStore} from 'vuex'

export default createStore({
    state: {
        vehicleModel: ''
    },
    mutations: {
        setVehicleModel(state, model) {
            state.vehicleModel = model;
        }
    },
    actions: {},
    modules: {}
})
