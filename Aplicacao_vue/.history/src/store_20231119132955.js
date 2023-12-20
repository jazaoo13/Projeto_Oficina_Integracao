import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
    state: {
        count: 0,
        isActive: false
    },
    mutations: {
        increment(state) {
            state.count++
        },
        setIsActive(state,isActive){
            state.isActive = !state.isActive
        }
    },
    
})
export default store