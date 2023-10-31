<template>
    <div class="max-w-md mx-auto p-6 bg-white shadow-md rounded-lg dark:bg-gray-800">
      <h1 class="text-2xl font-semibold text-gray-900 dark:text-white">Регистрация</h1>
      <form @submit.prevent="registerAndLoginUser" class="mt-4 space-y-4">
  <div class="mb-6">
    <label for="username" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Имя пользователя</label>
    <input
      type="text"
      id="username"
      v-model="userData.username"
      autocomplete="username"
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
      autocomplete="current-password" 
      class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
      required
    />
    <div v-if="passwordTooShort" class="text-red-600 dark:text-red-500">Пароль слишком короткий (минимум 8 символов)</div>
  </div>
  <div class="mb-6">
    <label for="password_confirmation" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Повторите пароль</label>
    <input
      type="password"
      id="password_confirmation"
      v-model="userData.password_confirmation"
      autocomplete="current-password" 
      class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
      required
    />
    <div v-if="passwordsDoNotMatch" class="text-red-600 dark:text-red-500">Пароли не совпадают</div>
  </div>
  <button
    type="submit"
    class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover-bg-blue-700 dark:focus-ring-blue-800"
  >
    Зарегистрироваться
  </button>
  <div v-if="registrationError" class="text-red-600 dark:text-red-500">{{ registrationError }}</div>
</form>
    </div>
  </template>
  
  <script>
  import router from '../routes/index.js';
  
  export default {
    data() {
      return {
        userData: {
          username: "",
          password: "",
          password_confirmation: "",
        },
        registrationError: null,
      };
    },
    computed: {
      passwordsDoNotMatch() {
        return this.userData.password !== this.userData.password_confirmation;
      },
      passwordTooShort() {
        return this.userData.password.length < 8;
      },
    },
    methods: {
      async registerAndLoginUser() {
        if (this.passwordTooShort || this.passwordsDoNotMatch) {
          return;
        }
  
        try {
          // Шаг 1: Регистрация пользователя
          const registrationResponse = await this.$axios.post("api/v1/auth/users/", this.userData);
  
          // Шаг 2: Вход с получением токена
          const loginResponse = await this.$axios.post("auth/token/login/", {
            username: this.userData.username,
            password: this.userData.password,
          });
  
          // Обработка успешной регистрации и входа
          console.log("Пользователь успешно зарегистрирован и вошел в систему:", loginResponse.data);
  
          // Сохраните токен в хранилище Vuex с помощью действия 'login'
          this.$store.dispatch('login', { username: registrationResponse.data.username, userId: registrationResponse.data.id, token: loginResponse.data.auth_token });
          router.push({ name: "home" });
        } catch (error) {
          // Обработка ошибок регистрации или входа
          this.registrationError = "Ошибка при регистрации";
        }
      },
    },
  };
  </script>