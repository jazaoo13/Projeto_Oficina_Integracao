<template>
    <div class="backPage">

    </div>
</template>

<script>
import store from '../store';
import { mapState } from 'vuex'
    export default {
        name:"EstoqueView",
        store,
        methods: {
        computed: {
            ...mapState(['isActive'])
            
        }
    },
    }
</script>

<style lang="scss" scoped>
.backPage{
    background-color: aqua;
    width: 100%;
    height: 100%;
}
</style>