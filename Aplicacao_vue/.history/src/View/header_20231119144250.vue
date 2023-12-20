<template>
    <div>
        <div class="header" :class="{ 'isActive': this.$store.state.isActive }">
        <h1>Estoque</h1>
        </div>
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
.header {
    width: calc(100% - 85px);
    background-color: #f4f4f6;
    border-radius: 0.75rem;
    height: 100px;
    margin-left:auto;
    transition: width 500ms ease ;
    &.isActive{
        width:calc(100% - 245px);
        transition: width 500ms ease ;
    }
}

// .header{

// }
</style>