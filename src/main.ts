import Vue from 'vue';
import App from './App.vue';

import router from './router';
import store from './store';
import './markdownEditor';
import './components';
import './registerServiceWorker';

Vue.config.productionTip = false;

new Vue({
    router,
    store,
    render: (h: any) => h(App),
}).$mount('#app');