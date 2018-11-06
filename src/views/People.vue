<template>
    <div>
        <h1>People</h1>
    </div>
</template>

<script>
// import Axios from 'axios';

export default {
    beforeRouteEnter(to, from, next) {
        console.log("loading...");
        Axios.get('/people').then(() => {
            console.log("loaded!");
            next();
        }, () => {
            console.log("loading failed");
        });
    },
    beforeRouteUpdate(to, from, next) {
        console.log("loading...");
        setTimeout(() => {
            console.log("loaded!");
            next();
        }, 2000);
    }
}
</script>