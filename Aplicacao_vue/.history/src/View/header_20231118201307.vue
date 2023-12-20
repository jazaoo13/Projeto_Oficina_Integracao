<template>
    <div>
        <div class="teste" :class="{ 'isActive': isActive }">TESTE</div>
    </div>
</template>

<script>
    export default {
        name: "EstoquePage"
    }
</script>

<style lang="scss" scoped>
.teste{
    background-color: #f4f4f6;
    border-radius: 0.75rem;
    height: 100px;
}
// .header{
    
// }
</style>