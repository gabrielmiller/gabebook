<template>
    <div id="app">
        <input id='sidebar-checkbox' type='checkbox' v-model="isSidebarOpen">
        <label for="sidebar-checkbox" id='sidebar-toggle'>
            <icon-menu></icon-menu>
        </label>
        <div id="sidebar">
            <ul>
                <li class="divider"></li>
                <li>
                    <router-link to="/new">
                        <icon-plus></icon-plus> <span>Create New</span>
                    </router-link>
                </li>
                <li class="divider"></li>
                <li>
                    <router-link to="/">
                        <icon-home></icon-home> <span>Home</span>
                    </router-link>
                </li>
                <li>
                    <router-link to="/people">
                        <icon-people></icon-people> <span>People</span>
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
export default {
    data() {
        return {
            isSidebarOpen: false,
        };
    },
    watch: {
        '$route' (to, from) {
            this.$data.isSidebarOpen = false;
        }
    }
}
</script>