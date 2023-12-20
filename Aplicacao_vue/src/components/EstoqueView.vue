<template>
    <div class="fundo" :class="{ 'isActive': this.$store.state.isActive }">
        <div class="teste">
            <ul class="listaItens">
                <li class="items" v-for="produto in produtos" :key="produto.indice">
                    <div class="text-container">
                        <v class="nome">{{produto.nome}}</v>
                    </div>
                    <div class="item-wrapper">
                        <v class="image"><img class="imagens" :src="getImageUrl(produto.image)" alt="Product Image" /></v>
                    </div>
                    <div class="text-container">
                        <v class="litragem">{{ produto.litragem.toFixed(2) }}ml</v>
                    </div>
                </li>
            </ul>
            <!-- <button @click="updateDatabase()">Update Database</button> -->
        </div>
    </div>
</template>

<script>
import io from 'socket.io-client'
import axios from 'axios';
import { mapState } from 'vuex'
export default {
    name: "EstoqueView",
    data() {
        return {
            produtos: [],
        }
    },
    methods: {
        computed: {
            ...mapState(['isActive'])
        },
        getImageUrl(base64String) {
            return base64String ? `data:image/png;base64,${base64String}` : null;
        },
        async getProdutos() {
            try {
                const response = await axios.get('http://192.168.43.67:5000/get_produtos');
                console.log('Data from server:', response.data);
                response.data.sort((a, b) => a.indice - b.indice);
                this.produtos = response.data;
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        },
        async updateDatabase() {
            try {
                const randomPeso = Math.floor(Math.random() * 1000);
                // Example data for the POST request
                const postData = {
                    cod_barra: 78969954434,
                    peso: randomPeso.toString()
                };

                // Make a POST request to update the database
                await axios.post('http://192.168.43.67:5000/update_database', postData);

                // Fetch updated data after the database is updated
                //await this.getProdutos();
            } catch (error) {
                console.error('Error updating database:', error);
            }
        },
    },
    mounted() {
        this.getProdutos();
        const socket = io('http://192.168.43.67:5000');
        socket.on('database_updated', (data) => {
            console.log('database_updated:', data);
            this.getProdutos();
        })
    }
}
</script>

<style lang="scss" scoped>
.fundo {
    background-color: #ffffff;
    width: 100%;
    height: 100%;
    margin-left: auto;
    border-radius: 20px;
    margin-top: 5px;
    margin-right: 0px;
    height: auto;
    transition: width 500ms ease;

    &.isActive {
        //width: calc(100% - 245px);
        transition: width 500ms ease;
    }
}

.items {
    background-color: lightslategray;
    flex-grow: 0;
    margin: 20px 10px 0px;
    border-radius: 20px;
    list-style-type: none;
}

.listaItens {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: space-evenly;
    padding-left: 10px;
    padding-right: 10px;
}

.imagens {
    object-fit: contain;
    height: 250px;
    margin-left: 15px;
    margin-right: 15px;
}
.item-wrapper { 
  display: flex;
  width: 150px; 
  flex-direction: column;
}

.text-container {
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-top: 10px;
  padding-bottom: 10px;
  color: #172031;
}
.litragem{
    text-align: center;
}
.nome{
    text-align: center;
}
</style>