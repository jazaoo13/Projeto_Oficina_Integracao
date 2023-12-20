<template>
    <div class="fundo">
        <div class="row" :class="{ 'isActive': this.$store.state.isActive }">
            <ul class="teste">
                <li class="items">TESTE</li>
                <li class="items">TESTE</li>
                <li class="items">TESTE</li>
                <li class="items">TESTE</li>
                <li class="items">TESTE</li>
                <li class="items">TESTE</li>
                <li class="items">TESTE</li>
                <li class="items">TESTE</li>
                <li class="items">TESTE</li>
                <li class="items">TESTE</li>
                <li class="items">TESTE</li>
                <li class="items">TESTE</li>
                <li class="items">TESTE</li>
                <li class="items">TESTE</li>
                <li class="items">TESTE</li>
                <!-- <li class="items">TESTE</li>
                <li class="items">TESTE</li>
                <li class="items">TESTE</li> -->
            </ul>
        </div>
    </div>
</template>

<script>

import { mapState } from 'vuex'
export default {
    name: "EstoqueView",
    methods: {
        computed: {
            ...mapState(['isActive'])
        }
    },
}
</script>

<style lang="scss" scoped>
.row {
    width: calc(100% - 85px);
    margin-left: auto;
    border-radius: 20px;
    margin-top: 5px;
    margin-right: 0px;
    height: calc(100% - 10px);
    transition: width 500ms ease;

    &.isActive {
        width: calc(100% - 245px);
        transition: width 500ms ease;
    }
}
.fundo{
    background-color: #f4f4f6;
    height: 100%;
    width: calc(100% - 85px);
}

.items {
    background-color: black;
    padding: 80px 100px;
    margin: 20px 10px 0px;
    border-radius: 20px;
    list-style-type: none;
}

.teste {
    display: flex;
    flex-direction: row;
    justify-content: space-evenly;
    flex-wrap: wrap;
    flex-grow: 2;
    align-items: flex-start;
}</style>