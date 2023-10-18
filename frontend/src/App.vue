<template>
 <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
 <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
  <div id="app">
    <InstituteList /> <!-- Добавьте это, чтобы использовать компонент -->
  </div>
</template>

<script>
import InstituteList from './components/InstituteList.vue';
export default {
  name: 'App',
  components: {
    InstituteList
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
