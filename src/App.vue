<template>
    <div id="app">
        <input id='sidebar-checkbox' type='checkbox' v-model="isSidebarOpen">
        <label for="sidebar-checkbox" id='sidebar-toggle'>
            <i class="fa fa-2x fa-bars"></i>
        </label>
        <div id="sidebar">
            <ul>
                <li class="divider"></li>
                <li>
                    <router-link to="/new">
                        <i class="fa fa-2x fa-plus-circle"></i> <span>Create New</span>
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
export default {
    data() {
        return {
            isSidebarOpen: false,
        };
    },
    watch: {
        '$route' () {
            this.$data.isSidebarOpen = false;
        }
    }
}
</script>