<template>
    <div>
        <div class="teste" :class="{ 'isActive': this.$store.state.isActive }">TESTE</div>
    </div>
</template>

<script>
import store from '../store';
import { mapState } from 'vuex'
export default {
    name: "HeaderPage",
    store,
    data() {
        return {
            //isActive: false,
        }
    },
    computed: {
        ...mapState(['isActive'])

    },
}
</script>

<style lang="scss" scoped>
.teste {
    width: calc(100vw - 90px);
    background-color: #f4f4f6;
    border-radius: 0.75rem;
    height: 100px;
    &.isActive{
        width:calc(100vw - 250px);
    }
}

// .header{

// }
</style>