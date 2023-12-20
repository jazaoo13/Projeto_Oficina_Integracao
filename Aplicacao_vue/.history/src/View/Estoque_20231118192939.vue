<template>
    <div class="header">
        <div class="teste" :class="{ 'isActive': isActive }">TESTE</div>
    </div>
</template>

<script>
    export default {
        name: "EstoquePage"
    }
</script>

<style lang="scss" scoped>
.header{
    background-color: aqua;
    width: calc(100vw - 5rem);
    height: 50px;
    position:fixed;
    left: calc(5rem + 10px);
    border-radius: 0.75rem;
}
.teste{
    background-color: #f4f4f6;
    position: absolute;
    width: 94.5vw;
    left: calc(5rem + 5px);
    right: 5px;
    border-radius: 0.75rem;
    height: 100px;
    top:0;
    transition: fade-in 100ms ease !important;
    &.isActive{
        left:calc(15rem + 5px);
        width: calc(94.5vw - 160px); 
        
    }
}
</style>