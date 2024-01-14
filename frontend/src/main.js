import { createApp } from 'vue';
import App from './App.vue';
import router from './routes';
import './style.css';
import axios from 'axios';
import store from './store';
import 'flowbite';

const app = createApp(App);
app.config.globalProperties.$axios = axios;
axios.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers['Authorization'] = `Token ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);
axios.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response.status === 401) {
      localStorage.removeItem('token');
      // Дополнительные действия, которые вы можете предпринять при истечении токена
    }
    return Promise.reject(error);
  }
);
app.use(router);
app.use(store);
app.mount('#app');