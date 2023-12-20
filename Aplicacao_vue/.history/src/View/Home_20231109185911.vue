<template>
    <div></div>
</template>

<script>
import axios from 'axios';
export default {
    name: 'HomePage',
    data() {
        return {
            lstApi: '',
        };
    },
    methods: {
        chamar_api() {
            let url = 'http.../api';
            axios
                .post(url, {
                    indice: '',
                    peso: '',
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

<style lang="sass" scoped></style>
