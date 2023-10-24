import { createRouter, createWebHistory} from 'vue-router';

// import Home from '../views/Home.vue';
// import About from '../views/About.vue';
// import Institutes from '../views/Institutes.vue';

const Home = () => import('../views/Home.vue');
const About = () => import('../views/About.vue');
const Institutes = () => import('../views/Institutes.vue');
const routes = [
    { path : '/', component:Home},
    { path : '/about', component:About},
    { path : '/institutes', component:Institutes},
];

const router = createRouter({
    history: createWebHistory(),
    routes: routes
});

export default router;