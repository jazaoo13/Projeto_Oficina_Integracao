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
                .catch(console.log.error());
        },
    },
};
</script>

<style lang="sass" scoped></style>
