<template>
    <div>
        <h1>People</h1>
    </div>
</template>

<script lang="ts">
import Vue from 'vue'
import Component from 'vue-class-component'
import Axios from 'axios';

@Component({
    beforeRouteEnter(to: any, from: any, next: Function) {
        console.log("loading...");
        Axios.get('/people').then(() => {
            console.log("loaded!");
            next();
        }, () => {
            console.log("loading failed");
        });
    },
    beforeRouteUpdate(to: any, from: any, next: Function) {
        console.log("loading...");
        setTimeout(() => {
            console.log("loaded!");
            next();
        }, 2000);
    }
})
export default class People extends Vue {
}

</script>