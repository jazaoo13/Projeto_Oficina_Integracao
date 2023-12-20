<template>
    <div class="bodyClass">
        <div class="container-fluid">
            <div class="row">
                <Sidebar></Sidebar>
            </div>
            <div class="content-container">
                <HeaderPage></HeaderPage>
                <EstoqueView></EstoqueView>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import Sidebar from './Sidebar.vue';
import HeaderPage from './Header.vue'
import EstoqueView from '../components/EstoqueView.vue'
export default {
    name: 'HomePage',
    components: {
        Sidebar,
        HeaderPage,
        EstoqueView
    },
    data() {
        return {
            lstApi: '',
        };
    },
    methods: {
        chamar_api() {
            let url = 'https://catfact.ninja/fact';
            axios
                .get(url, {

                })
                .then((resposta) => {
                    this.lstApi = resposta
                })
                .catch((erro) => console.log(erro));
        },
    },
    mounted() {
        this.chamar_api()
    },
};
</script>

<style lang="scss" scoped>
.bodyClass {
    background: radial-gradient(circle at 50% 50%, #192233 20%, #000);
    padding: 0.375rem;
    font-family: Poppins, sans-serif;
    display: flex;
}
.container-fluid {
  display: flex;
  flex-direction: row;
  margin-left: 5px;
  margin-right: 5px;
  margin-top: 5px;
  margin-bottom: 5px;
}
.content-container {
  display: flex;
  flex-direction: column;
}
</style>
