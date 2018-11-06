import Vue from 'vue';
import Router from 'vue-router';

import Edit from './views/Edit.vue';
import Home from './views/Home.vue';
import New from './views/New.vue';
import People from './views/People.vue';

Vue.use(Router);

function beforeLeave(to, from, next) {
    let leave = true;

    if (this.$data.isDirty) {
        leave = confirm("Are you sure you want to leave?");
    }

    if (leave) {
        next();
    }
}

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            beforeLeave: beforeLeave,
            component: Edit,
            name: 'edit',
            path: '/edit/:id',
        },
        {
            component: Home,
            name: 'home',
            path: '/',
        },
        {
            beforeLeave: beforeLeave,
            component: New,
            name: 'new',
            path: '/new',
        },
        {
            component: People,
            name: 'people',
            path: '/people',
        },
    ],
});
