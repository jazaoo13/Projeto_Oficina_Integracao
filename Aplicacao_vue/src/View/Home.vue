<template>
    <!-- <div class="bodyClass"> -->
        <div class="container-fluid">
            <div class="row">
                <Sidebar></Sidebar>
            </div>
            <div class="content-container">
                <HeaderPage></HeaderPage>
                <EstoqueView></EstoqueView>
            </div>
        </div>
    <!-- </div> -->
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
    // min-height: calc(100vh - 20px);
    // min-width: calc(100vw - 20px);
    height: 100%;
    width: 100%;
    padding: 0.375rem;
    font-family: Poppins, sans-serif;
    display: flex;
}

.row {
    margin-right: 0px;
    margin-left: 0px;
}

.container-fluid {
    display: flex;
    flex-direction: row;
    padding-left: 5px;
    padding-top: 5px;
    padding-bottom: 5px;
    padding-right: 5px;
    width:unset;
    min-height: 98.5vh;
}

.content-container {
    font-family:sans-serif;
    font-size: large;
    height: 100%;
    width: 100%;
    display: flex;
    flex-direction: column;
    padding-left: 5px;
}</style>
