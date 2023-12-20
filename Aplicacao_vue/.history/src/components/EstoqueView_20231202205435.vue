<template>
    <div class="fundo" :class="{ 'isActive': this.$store.state.isActive }">
        <div class="teste" >
            <ul class="listaItens">
                <!-- <li class="items">TESTE</li>
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
                <li class="items">TESTE</li> -->
                <!-- <li class="items">TESTE</li>
                <li class="items">TESTE</li>
                <li class="items">TESTE</li> -->
            </ul>
        </div>
    </div>
</template>

<script>
import io from 'socket.io-client'
import { mapState } from 'vuex'
export default {
    name: "EstoqueView",
    data(){
        return{
            updateData: '',
        }
    },
    methods: {
        computed: {
            ...mapState(['isActive'])
        }
    },
    mounted(){
        const socket = io.connect('http:localhost:5000');

        socket.on('uopdate_response',(data) =>{
            console.log('Received update:', data);
            this.updateData = data.data;
        })
    }
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