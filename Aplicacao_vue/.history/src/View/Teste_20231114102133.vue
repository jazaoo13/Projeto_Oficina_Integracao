<template>
    <aside :class="`&{isActive && 'isActive'}`">
        <div class="logo">
            <img src="../assets/html5.svg" alt="HTML5">
        </div>
       <div class="manu-toggle-wrap">
            <button class="menu-toggle" @click="toggle()">
                <span class="material-icons">keyboard_double_arrow_right</span>
            </button>

       </div>

    </aside>
</template>

<script>
    export default {
        name:'teste_component',
        data(){
            return{
                is_expanded:false
            }
        },
        methods:{
            toggle(){
                this.is_expanded = !this.is_expanded;
            }
        },
    }
</script>

<style lang="scss" scoped>
aside{
    display:Flex;
    flex-direction: column;
    width: 4rem;
    min-height: 100vh;
    overflow: hidden;
    padding:1rem;

    background-color: darkcyan;
    color: white;
    
    transition: 0.2s ease-out;

    .logo{
        margin-bottom: 1rem;

        img{
            width: 2rem;
        }
    }
    @media(max-width: 768px){
        position:fixed;
        z-index: 99;
    }
    &.isActive{

    }
}
</style>