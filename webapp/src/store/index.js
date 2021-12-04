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
        currentIndex: 1,
        sliders: [
        {
            icon: 'user',
            name: 'Kaijie',
            tasks: [
            {
                id: 1,
                title: 'Dating',
                date: new Date(),
                done: false,
                deleted: false
            }
            ],
            colors: ['#7089AC', '#CED9E5']
        },
        {
            icon: 'suitcase',
            name: 'Work',
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
            colors: ['#D9B48B', '#F0DFC6']
        },
        {
            icon: 'home',
            name: 'Home',
            tasks: [
            {
                id: 2,
                title: 'House Keeping',
                date: new Date(),
                done: true,
                deleted: false
            }
            ],
            colors: ['#A3B2A4', '#E0E7D9']
        }
        ],

        selected: null,
        unselect: null,
        editing: null
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
            if (state.editing && state.editing.text) {
                state.selected.slider.tasks.unshift({
                title: state.editing.text,
                date: new Date(),
                done: false,
                deleted: false
                })
            }
            state.editing = state.editing ? null : { text: '' }
        }
    },
    getters: {
        currentSlider (state) {
            return state.sliders[state.currentIndex]
        },
        todayTasks (state) {
            const tasks = []
            state.sliders.forEach(slider => {
                slider.tasks.forEach(task => {
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
