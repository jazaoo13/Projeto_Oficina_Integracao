<template>
    <div class="backPage" :class="{ 'isActive': this.$store.state.isActive }">
        <div class="container-fluid">
        <div class="items"></div>
        <div class="items"></div>
        <div class="items"></div>
        <div class="items"></div>
        <div class="items"></div>
        <div class="items"></div>
        <div class="items"></div>
        <div class="items"></div>
        <div class="items"></div>
        <div class="items"></div>
        <div class="items"></div>
        <div class="items"></div>
        <div class="items"></div>
        <div class="items"></div>
        <div class="items"></div>
        <div class="items"></div>
        <div class="items"></div>
        <div class="items"></div>
        <div class="items"></div>
        <div class="items"></div>
        </div>
       
    </div>
</template>

<script>

import { mapState } from 'vuex'
    export default {
        name:"EstoqueView",
        methods: {
        computed: {
            ...mapState(['isActive'])
        }
    },
    }
</script>

<style lang="scss" scoped>
.backPage{
    background-color: #f4f4f6;
    width: calc(100% - 85px);
    margin-left: auto;
    border-radius: 20px;
    margin-top: 5px;
    height: calc(100% - 10px);
    transition: width 500ms ease ;
    &.isActive{
        width:calc(100% - 245px);
        transition: width 500ms ease ;
    }
}
.items{

    background-color: black;
    width: 30px;
    height: 30px;
}
</style>