<template>
    <div id="app">
        <nav-bar />

        <div id="content">
            <router-view/>
        </div>

    </div>
</template>

<script>

import NavBar from '@/components/NavBar.vue'

export default {
    name: 'Home',
    components: {
        NavBar,
    },
    created() {
        this.$store.commit('user/initUserData');
    },
}
</script>

<style>
#app {
    background-image: url("https://trello-backgrounds.s3.amazonaws.com/SharedBackground/2133x1600/6409c6d4cb00da823bf8655f1d52c79b/photo-1564319453909-c0ab34359309.jpg");
    background-size: cover;
    color: #2c3e50;
    height: fit-content;
    min-height: 100vh;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}

#content {
    background-color: white;
    box-sizing: border-box;
    margin: auto;
    max-width: 1024px;
    padding-top: 60px;
    padding-bottom: 3vh;
    width: 120vh;
    /* height: 300vh; */
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
