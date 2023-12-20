<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<style lang="scss">
#app {
  min-height: 100vh;
  min-width: 100vw;
  width:fit-content;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background: radial-gradient(circle at 50% 50%, #192233 20%, #000);
}
*, *::before, *::after {
    box-sizing: unset;
}

nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
