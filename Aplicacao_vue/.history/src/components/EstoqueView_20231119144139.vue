<template>
    <div class="backPage" :class="{ 'isActive': this.$store.state.isActive }">

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
    width: calc(100% - 85px);
    margin-left: auto;
    border-radius: 20px;
    margin-top: auto;
    height: calc(100% - 10px);
    transition: width 500ms ease ;
    &.isActive{
        width:calc(100% - 245px);
        transition: width 500ms ease ;
    }
}
</style>