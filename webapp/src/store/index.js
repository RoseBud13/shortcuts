import {createStore} from 'vuex'

export default createStore({
    state: {
        vehicleModel: '',
        landed: null,
        departured: null,
        show: true,
        cardContent: {
            content: 'data here'
        },

        currentIndex: 0,
        sliders: [
            {
                type: '',
                icon: 'tachometer-alt',
                name: 'Home',
                content: {
                    tasks: [],
                    shortcutsInfo: [],
                    colors: ['#ccd5ae', '#e9edc9']
                },
                colors: ['#ccd5ae', '#e9edc9']
            },
            {
                type: 'shortcuts',
                icon: 'rocket',
                name: 'Shortcuts',
                content: {
                    tasks: [],
                    shortcutsInfo: [],
                    colors: ['#BEE1E6', '#E2ECE9']
                },
                colors: ['#BEE1E6', '#E2ECE9']
            },
            {
                type: '',
                icon: 'map-marked',
                name: 'Interets',
                content: {
                    tasks: [],
                    shortcutsInfo: [],
                    colors: ['#FAD2E1', '#FDE2E4']
                },
                colors: ['#FAD2E1', '#FDE2E4']
            },
            {
                type: 'todo',
                icon: 'clipboard-check',
                name: 'Todo',
                content: {
                    tasks: [
                        {
                            id: 3,
                            title: 'Design Sprint',
                            date: new Date(),
                            done: true,
                            deleted: false
                        },
                        {
                            id: 4,
                            title: 'Icon Set Design for Mobile App',
                            date: new Date(),
                            done: false,
                            deleted: false
                        },
                        {
                            id: 5,
                            title: 'HTML/CSS Study',
                            date: new Date(),
                            done: false,
                            deleted: false
                        },
                        {
                            id: 6,
                            title: 'Weekly Report',
                            date: new Date(),
                            done: false,
                            deleted: false
                        },
                        {
                            id: 7,
                            title: 'Design Meeting',
                            date: new Date(),
                            done: false,
                            deleted: false
                        },
                        {
                            id: 9,
                            title: 'Quick Prototyping',
                            date: new Date('2019-09-16'),
                            done: false,
                            deleted: false
                        },
                        {
                            id: 8,
                            title: 'UX Conference',
                            date: new Date('2019-09-16'),
                            done: false,
                            deleted: false
                        }
                    ],
                    shortcutsInfo: [],
                    colors: ['#CDDAFD', '#DFE7FD']
                },
                colors: ['#CDDAFD', '#DFE7FD']
            },
        ],

        selected: null,
        unselect: null,
        editing: null,
        editorType: null,
        showScList: false,
        showScBuilder: false,

        selectedMethods: [],
        methodsBuilderName: ''
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

        selectSlider (state, selected) {
            state.unselect = null
            state.selected = selected
        },
        unselectSlider (state) {
            state.unselect = state.selected
            state.selected = null
        },
        nextSlider (state) {
            if (state.currentIndex < state.sliders.length - 1) {
                state.currentIndex++
            }
        },
        prevSlider (state) {
            if (state.currentIndex > 0) {
                state.currentIndex--
            }
        },
        deleteTask (_, { task }) {
            task.deleted = true
        },
        toggleEditing (state) {
            if (state.editorType === 'todo') {
                if (state.editing && state.editing.text) {
                        state.selected.slider.content.tasks.unshift({
                        title: state.editing.text,
                        date: new Date(),
                        done: false,
                        deleted: false
                    })
                }
                state.editing = state.editing ? null : { text: '' }
                state.showScList = false
            } else if (state.editorType === 'shortcuts') {
                state.editing = state.editing ? null : { text: '' }
                state.showScList = false
                state.showScBuilder = false
                state.selectedMethods = []
            }
        },
        setShortcutsData(state, data) {
            state.sliders[1].content.shortcutsInfo = data
        },
        updateShortcutsData(state, data) {
            state.sliders[1].content.shortcutsInfo.push(data)
        },
        toggleScList(state) {
            state.showScList = !state.showScList
        },
        openScBuilder(state) {
            state.showScBuilder = true
        },
        closeScBuilder(state) {
            state.showScBuilder = false
            state.selectedMethods = []
        },
        buildShortcuts(state, data) {
            state.selectedMethods.push(data)
        },
        setBuilderName(state, data) {
            state.methodsBuilderName = data
        },
    },
    getters: {
        currentSlider (state) {
            return state.sliders[state.currentIndex]
        },
        todayTasks (state) {
            const tasks = []
            state.sliders.forEach(slider => {
                slider.content.tasks.forEach(task => {
                if (task.date <= tomorrow && !task.done && !task.deleted) {
                    tasks.push(task)
                }
                })
            })
            return tasks
        }
    },
    actions: {},
    modules: {}
})
