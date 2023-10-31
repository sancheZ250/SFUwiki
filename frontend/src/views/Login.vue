<template>
    <div class="max-w-md mx-auto p-6 bg-white shadow-md rounded-lg dark:bg-gray-800">
      <h1 class="text-2xl font-semibold text-gray-900 dark:text-white">Авторизация</h1>
      <form @submit.prevent="loginUser" class="mt-4 space-y-4">
        <div class="mb-6">
          <label for="username" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Имя пользователя</label>
          <input
            type="text"
            id="username"
            v-model="userData.username"
            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
            required
          />
        </div>
        <div class="mb-6">
          <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Пароль</label>
          <input
            type="password"
            id="password"
            v-model="userData.password"
            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
            required
          />
        </div>
        <button
          type="submit"
          class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover-bg-blue-700 dark:focus-ring-blue-800"
        >
          Войти
        </button>
        <div v-if="loginError" class="text-red-600 dark:text-red-500">{{ loginError }}</div>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import router from '../routes/index.js';
  
  export default {
    data() {
      return {
        userData: {
          username: "",
          password: "",
        },
        loginError: null,
      };
    },
    methods: {
      async loginUser() {
        try {
          // Шаг 1: Вход с получением токена
          const loginResponse = await axios.post("auth/token/login/", this.userData);
          const auth_token = loginResponse.data.auth_token;
          const currentUserResponse = await axios.get("/api/v1/auth/users/me/", {
            headers: {
              Authorization: `Token ${auth_token}`
            }
          });
          // Обработка успешного входа
          console.log("Пользователь успешно вошел в систему:", loginResponse.data);
          this.$store.dispatch('login', { username: currentUserResponse.data.username, token: loginResponse.data.auth_token, userId: currentUserResponse.data.id});
          router.push({ name: "home" });
        } catch (error) {
          // Обработка ошибок входа
          this.loginError = "Ошибка при входе. Проверьте имя пользователя и пароль.";
        }
      },
    },
  };
  </script>