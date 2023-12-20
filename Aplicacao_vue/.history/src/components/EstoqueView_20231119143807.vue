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
    width: calc(100% - 245px);
    margin-left: auto;
    border-radius: 20px;
    margin-top: auto;
    height: calc(100% - 10px);
}
</style>