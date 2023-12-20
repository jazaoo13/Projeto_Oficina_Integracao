<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <HomeTeste/>
  </div>
</template>

<script>
import HomeTeste from './src/View/HomeTeste.vue'

export default {
  name: 'App',
  components: {
    HomeTeste
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
