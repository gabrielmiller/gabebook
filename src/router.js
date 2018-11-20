import Vue from 'vue';
import Router from 'vue-router';

import Edit from './views/Edit.vue';
import Home from './views/Home.vue';
import New from './views/New.vue';
import People from './views/People.vue';
import Person from './views/Person.vue';

Vue.use(Router);

function beforeMarkdownEditorLeave(to, from, next) {
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
            beforeLeave: beforeMarkdownEditorLeave,
            component: Edit,
            name: 'Edit Entry',
            path: '/edit/:entryId',
        },
        {
            //beforeLeave: beforeMarkdownEditorLeave,
            component: Person,
            name: 'Edit Person',
            path: '/person/:personId/edit',
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
            //beforeLeave: beforeMarkdownEditorLeave,
            component: Person,
            name: 'New Person',
            path: '/person/new',
        },
        {
            component: People,
            name: 'People',
            path: '/people',
        },
        {
            component: Person,
            name: 'Person',
            path: '/person/:personId',
        },
    ],
});
