import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
    data(){
        return{
            isActive: false
        }
    },
    state: {
        count: 0,
        isActive: false
    },
    mutations: {
        increment(state) {
            state.count++
        },
        setIsActive(state){
            state.isActive = !state.isActive
        }
    },
    
})
export default store