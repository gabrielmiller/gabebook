import Vue from 'vue';
import Router from 'vue-router';

import Edit from './views/Edit.vue';
import Home from './views/Home.vue';
import New from './views/New.vue';
import People from './views/People.vue';

//import Axios from 'axios';
import mockData from './mockData';

Vue.use(Router);

// eslint-disable-next-line
function beforeMarkdownEditorLeave(to, from, next) {
    let leave = true;

    if (this.$data.isDirty) {
        leave = confirm("Are you sure you want to leave?");
    }

    if (leave) {
        next();
    }
}

function loadPeople(to, from, next) {
    return mockData.getAllPeople().then((result) => {// eslint-disable-next-line
        console.log("get all people called", result);
        next(vm => {// eslint-disable-next-line
            console.log("vm is ", vm);
            //vm.$data.people = result;
        });
        //this.$data.people = result;
    });
    /*
    console.log("loading...");
    Axios.get('/people').then(() => {// eslint-disable-next-line
        console.log("loaded!");
        next();
    }, () => {// eslint-disable-next-line
        console.log("loading failed");
    });
    */
}

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            beforeLeave: beforeMarkdownEditorLeave,
            component: Edit,
            name: 'Edit Entry',
            path: '/edit/:id',
        },
        {
            component: Home,
            name: 'Home',
            path: '/',
        },
        {
            beforeLeave: beforeMarkdownEditorLeave,
            component: New,
            name: 'New Entry',
            path: '/new',
        },
        {
            beforeEnter: loadPeople,
            beforeUpdate: loadPeople,
            component: People,
            name: 'People',
            path: '/people',
        },
    ],
});
