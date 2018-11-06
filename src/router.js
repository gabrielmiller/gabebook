import Vue from 'vue';
import Router from 'vue-router';

import Edit from './views/Edit.vue';
import Home from './views/Home.vue';
import New from './views/New.vue';
import People from './views/People.vue';

Vue.use(Router);

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/edit/:id',
            name: 'edit',
            component: Edit,
        },
        {
            path: '/',
            name: 'home',
            component: Home,
        },
        {
            path: '/new',
            name: 'new',
            component: New,
        },
        {
            path: '/people',
            name: 'people',
            component: People,
        },
    ],
});