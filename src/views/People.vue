<template>
    <div>
        <h1>People</h1>
    </div>
</template>

<script>
import Axios from 'axios';

export default {
    beforeRouteEnter(to, from, next) {// eslint-disable-next-line
        console.log("loading...");
        Axios.get('/people').then(() => {// eslint-disable-next-line
            console.log("loaded!");
            next();
        }, () => {// eslint-disable-next-line
            console.log("loading failed");
        });
    },
    beforeRouteUpdate(to, from, next) {// eslint-disable-next-line
        console.log("loading...");
        setTimeout(() => {// eslint-disable-next-line
            console.log("loaded!");
            next();
        }, 2000);
    }
}
</script>