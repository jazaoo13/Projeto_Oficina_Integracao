<template>
    <div class="bodyClass">
        <div class="container-fluid">
            <div class="row">
                <Sidebar></Sidebar>
                <HeaderPage></HeaderPage>
            </div>
            <div class="row">
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
import mapState from 'vuex'
export default {
    name: 'HomePage',
    components: {
        Sidebar,
        HeaderPage,
        EstoqueView
    },
    computed:{
        ...mapState({
            count
        })
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
    height: 100vh;
    background: radial-gradient(circle at 50% 50%, #192233 20%, #000);
    padding: 0.375rem;
    font-family: Poppins, sans-serif;
    position: relative;
}
</style>
