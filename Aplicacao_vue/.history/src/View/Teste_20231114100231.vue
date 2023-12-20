<template>
    <aside>

    </aside>
</template>

<script>
    export default {
        
    }
</script>

<style lang="scss" scoped>
aside{
    display:Flex;
    flex-direction: column;
    width: calc(2rem + 32px);
    min-height: 100vh;
    overflow: hidden;
    padding:1rem;

    background-color: darkcyan;
    color: white;
    
    transition: 0.2s ease-out;

    @media(max-width: 768px){
        position:fixed;
        z-index: 99;
    }
    &.isActive{

    }
}
</style>