<template>
    <div>
        <div class="header" :class="{ 'isActive': isActive }">TESTE</div>
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
    height: 20vh;
}
</style>