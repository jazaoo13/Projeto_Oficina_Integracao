const store = new Vuex.Store({
    default:{
        state: {
            count: 0
        },
        mutations: {
            increment(state) {
                state.count++
            }
        }
    }
})