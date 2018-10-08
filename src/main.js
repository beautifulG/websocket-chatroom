// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import routes from './router'
import VueRouter from 'vue-router'
import Vuex from 'vuex'
import vuescroll from 'vuescroll'
import 'vuescroll/dist/vuescroll.css';

Vue.config.productionTip = false

Vue.use(vuescroll)
Vue.use(Vuex)
Vue.use(VueRouter)
const router = new VueRouter({
	routes
});
const store = new Vuex.Store({
    state:{
        nickname:"",
        id:0
    },
    mutations:{
        creatUser(state,data){
            state.nickname = data.nickname;
            state.id = data.id;
        }
    }
});
const socket = io('http://127.0.0.1:5000');
Vue.prototype.$socket = socket;

new Vue({
	router,
    store
}).$mount('#app')
