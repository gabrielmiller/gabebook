<template>
    <div id="app">
        <input type='checkbox' id='sidebar-checkbox'>
        <label id='sidebar-toggle' for="sidebar-checkbox">
            <icon-menu></icon-menu>
        </label>
        <div id="sidebar">
            <ul>
                <li><router-link to="/new"><icon-plus></icon-plus> Create New</router-link></li>
                <li><router-link to="/">Home</router-link></li>
                <li><router-link to="/people"><icon-people></icon-people>People</router-link></li>
            </ul>
        </div>
        <div id="content">
            <router-view/>
        </div>
    </div>
</template>