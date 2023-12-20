<template>
    <div class="fundo" :class="{ 'isActive': this.$store.state.isActive }">
        <div class="teste" >
            <ul class="listaItens">
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

.fundo{
    background-color: #ffffff;
    //width: calc(100% - 85px);
    margin-left: auto;
    border-radius: 20px;
    margin-top: 10px;
    margin-right: 0px;
    height: auto;
    transition: width 500ms ease;
    &.isActive {
        //width: calc(100% - 245px);
        transition: width 500ms ease;
    }
}

.items {
    background-color: black;
    //padding: 80px 100px;
    width: 150px;
    height: 300px;
    margin: 20px 10px 0px;
    border-radius: 20px;
    list-style-type: none;
    padding-top: 50px;
}

.listaItens {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: space-evenly;
    padding-left: 10px;
    padding-right: 10px;
}</style>