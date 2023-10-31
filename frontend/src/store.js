// store.js
import { createStore } from 'vuex';

const store = createStore({
  state: {
    token: localStorage.getItem('token') || null, 
    userId: localStorage.getItem('userId') || null,
    username: localStorage.getItem('username') || null, 
  },
  mutations: {
    setUserId(state, userId) {
      state.userId = userId;
      localStorage.setItem('userId', userId);
    },
    setUsername(state, username) {
      state.username = username;
      localStorage.setItem('username', username);
    },
    setToken(state, token) {
      state.token = token;
      localStorage.setItem('token', token); // Сохранение токена в localStorage
    },
    clearUserId(state) {
      state.userId = null;
      localStorage.removeItem('userId');
    },
    clearUsername(state) {
      state.username = null;
      localStorage.removeItem('username');
    },
    clearToken(state) {
      state.token = null;
      localStorage.removeItem('token'); // Удаление токена из localStorage
    },
  },
  actions: {
    login({ commit }, { userId, username, token }) {
      commit('setUserId', userId);
      commit('setUsername', username);
      commit('setToken', token);
    },
    logout({ commit }) {
      commit('clearUserId');
      commit('clearUsername');
      commit('clearToken');
    },
  },
  getters: {
    getUserId: (state) => state.userId,
    getUsername: (state) => state.username,
    isAuthenticated: (state) => !!state.token, // Проверка наличия токена для определения авторизации
    getToken: (state) => state.token,
  },
});

export default store;
