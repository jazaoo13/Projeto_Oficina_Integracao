<template>
    <div >
        <Sidebar class="bodyClass">
        </Sidebar>
        <EstoquePage></EstoquePage>
    </div>
</template>

<script>
import axios from 'axios';
import Sidebar from './Sidebar.vue';
import EstoquePage from './Estoque.vue'
export default {
    name: 'HomePage',
    components:{
        Sidebar,
        EstoquePage
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
                    this.lstApi=resposta
                })
                .catch((erro) => console.log(erro));
        },
    },
    mounted(){
        this.chamar_api()
    },
};
</script>

<style lang="sass" scoped>
.bodyClass {
    height: 100vh;
    background: radial-gradient(circle at 50% 50%, #192233 20%, #000);
    padding: 0.375rem;
    font-family: Poppins, sans-serif;
    position: relative;
}
</style>
