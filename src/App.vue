<template>
    <div id="app">
        <input
            class="invisible-toggle"
            id='sidebar-checkbox'
            type='checkbox'
            v-model="isSidebarOpen">
        <label for="sidebar-checkbox" id='sidebar-toggle'>
            <i class="fa fa-2x fa-bars"></i>
        </label>
        <div class="ease-slide sidebar toggle-content" id="sidebar">
            <div class="title">
                <span>{{ title }}</span>
            </div>
            <ul>
                <li class="divider"></li>
                <li>
                    <router-link to="/new">
                        <i class="fa fa-2x fa-plus-circle"></i> <span>New Entry</span>
                    </router-link>
                </li>
                <li class="divider"></li>
                <li>
                    <router-link to="/">
                        <i class="fa fa-2x fa-home"></i> <span>Home</span>
                    </router-link>
                </li>
                <li>
                    <router-link to="/people">
                        <i class="fa fa-2x fa-users"></i> <span>People</span>
                    </router-link>
                </li>
            </ul>
        </div>
        <div id="content">
            <router-view/>
        </div>
    </div>
</template>

<script>
import mockData from './mockData';

export default {
    beforeRouteEnter() {
        return mockData.fetchAllPeople().then((result) => {
            for (let person of result) {
                this.people.push(person);
            }
        });
    },
    data() {
        return {
            isSidebarOpen: false,
            people: []
        };
    },
    computed: {
        title: function() {
            return this.$route.name;
        }
    },
    watch: {
        '$route' () {
            this.$data.isSidebarOpen = false;
        }
    }
}
</script>