<template>
    <div class="fundo" :class="{ 'isActive': this.$store.state.isActive }">
        <div class="teste" >
            <ul class="listaItens">
                <li class="items" v-for="produto in produtos" :key="produto.indice">
                    {{ produto.litragem }}
                </li>
            </ul>
            <button @click="updateDatabase()">Update Database</button>
        </div>
    </div>
</template>

<script>
import io from 'socket.io-client'
import axios from 'axios';
import { mapState } from 'vuex'
export default {
    name: "EstoqueView",
    data(){
        return{
            produtos: [],
        }
    },
    methods: {
        computed: {
            ...mapState(['isActive'])
        },
        async getProdutos() {
            try {
                const response = await axios.get('http://localhost:5000/get_produtos');
                console.log('Data from server:', response.data);        
                this.produtos = response.data;
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        },
        async updateDatabase() {
            try {
                // Example data for the POST request
                const postData = {
                    cod_barra: '76548976445',
                    peso: '666'
                };

                // Make a POST request to update the database
                await axios.post('http://localhost:5000/update_database', postData);

                // Fetch updated data after the database is updated
                //await this.getProdutos();
            } catch (error) {
                console.error('Error updating database:', error);
            }
        },
    },
    mounted(){
        this.getProdutos();
        const socket = io('http://localhost:5000');
        socket.on('Database updated',(data) =>{
            console.log('database_updated:', data);
            this.produtos = data.data;
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