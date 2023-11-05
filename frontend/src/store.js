// store.js
import { createStore } from 'vuex';

const store = createStore({
  state: {
    token: localStorage.getItem('token') || null, 
    userId: localStorage.getItem('userId') || null,
    username: localStorage.getItem('username') || null, 
    isModerator: localStorage.getItem('isModerator') === 'true' || false, // Добавляем поле isModerator
    isAdmin: localStorage.getItem('isAdmin') === 'true' || false,
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
    setModeratorAndAdminStatus(state, { isModerator, isAdmin }) {
      state.isModerator = isModerator;
      state.isAdmin = isAdmin;
      localStorage.setItem('isModerator', isModerator ? 'true' : 'false');
      localStorage.setItem('isAdmin', isAdmin ? 'true' : 'false');
    },
    clearModeratorAndAdminStatus(state){
      state.isAdmin = null;
      state.isModerator = null;
      localStorage.removeItem('isAdmin');
      localStorage.removeItem('isModerator');
    }
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
      commit('clearModeratorAndAdminStatus');
    },
    setModeratorAndAdminStatus({ commit }, { isModerator, isAdmin }) {
      commit('setModeratorAndAdminStatus', { isModerator, isAdmin });
    },
  },
  getters: {
    getUserId: (state) => state.userId,
    getUsername: (state) => state.username,
    isAuthenticated: (state) => !!state.token, // Проверка наличия токена для определения авторизации
    getToken: (state) => state.token,
    isModerator: (state) => state.isModerator,
    isAdmin: (state) => state.isAdmin,
  },
});

export default store;
