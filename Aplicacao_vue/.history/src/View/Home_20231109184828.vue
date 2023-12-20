<template>
    <div></div>
</template>

<script>
import axios from 'axios';
export default {
    name: 'Home',
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
                    this.lstApi();
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
