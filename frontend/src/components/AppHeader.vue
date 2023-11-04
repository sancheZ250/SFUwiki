<template>
  <nav class="bg-gradient-to-r from-orange-400 via-orange-500 to-orange-600 border-gray-200 dark:bg-gray-900">
    <div class="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4">
      <router-link to="/" class="flex items-center">
        <img src="../assets/logo.png" class="h-24 mr-3"/>
        <span class="self-center text-2xl font-semibold whitespace-nowrap dark:text-grey-100">SFUwiki</span>
      </router-link>
      <button data-collapse-toggle="navbar-default" type="button" class="inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600" aria-controls="navbar-default" aria-expanded="false">
        <span class="sr-only">Open main menu</span>
        <svg class="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 17 14">
          <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M1 1h15M1 7h15M1 13h15"/>
        </svg>
      </button>
      <div class="hidden w-full md:block md:w-auto" id="navbar-default">
        <ul class="font-medium flex flex-col p-4 md:p-0 mt-4 border border-orange rounded-lg bg-orange md:flex-row md:space-x-8 md:mt-0 md:border-0 md:bg-orange dark:bg-orange md:dark:bg-orange dark:border-orange">
            <li>
            <router-link to="/institutes" class="block py-2 pl-3 pr-4 text-gray-900 bg-orange rounded hover:bg-orange-600 md:hover-bg-transparent md:border-0 md:hover:text-grey-100 dark:bg-orange md:p-0 dark:text-grey-100 md:dark:hover-text-grey-100 dark:hover-bg-orange-600 dark:hover-text-white md:dark:hover-bg-transparent">Институты</router-link>
          </li>
          <li>
            <router-link to="/teachers" class="block py-2 pl-3 pr-4 text-gray-900 bg-orange rounded hover:bg-orange-600 md:hover-bg-transparent md:border-0 md:hover:text-grey-100 dark:bg-orange md:p-0 dark:text-grey-100 md:dark:hover-text-grey-100 dark:hover-bg-orange-600 dark:hover-text-white md:dark:hover-bg-transparent">Преподаватели</router-link>
          </li>
          <li>
            <button @click="toggleDarkMode" class="block py-2 pl-3 pr-4 text-gray-900 bg-orange rounded hover:bg-orange-600 md:hover-bg-transparent md:border-0 md:hover:text-grey-100 dark:bg-orange md:p-0 dark:text-grey-100 md:dark:hover-text-grey-100 dark:hover-bg-orange-600 dark:hover-text-white md:dark:hover-bg-transparent">
            Переключить тему
          </button>
          </li>
          <li v-if="!$store.getters.isAuthenticated">
            <router-link to="/register" class="block py-2 pl-3 pr-4 text-gray-900 bg-orange rounded hover:bg-orange-600 md:hover-bg-transparent md:border-0 md:hover:text-grey-100 dark:bg-orange md:p-0 dark:text-grey-100 md:dark:hover-text-grey-100 dark:hover-bg-orange-600 dark:hover-text-white md:dark:hover-bg-transparent">Регистрация</router-link>
          </li>
          <li v-if="!$store.getters.isAuthenticated">
            <router-link to="/login" class="block py-2 pl-3 pr-4 text-gray-900 bg-orange rounded hover:bg-orange-600 md:hover-bg-transparent md:border-0 md:hover:text-grey-100 dark:bg-orange md:p-0 dark:text-grey-100 md:dark:hover-text-grey-100 dark:hover-bg-orange-600 dark:hover-text-white md:dark:hover-bg-transparent">Войти</router-link>
          </li>
          <li v-if="$store.getters.isAuthenticated">
            <div class="flex items-center">
              <span class="mr-2 text-gray-900 dark:text-grey-100">{{ this.$store.getters.getUsername }}</span>
              <button @click="logout" class="text-red-300 bg-orange hover:underline text-sm font-medium">Выйти</button>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  mounted() {
    const savedTheme = localStorage.getItem('color-theme');
    if (savedTheme === 'dark') {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  },
  methods: {
    toggleDarkMode() {
      const isDarkMode = document.documentElement.classList.contains('dark');
      if (isDarkMode) {
        document.documentElement.classList.remove('dark');
        localStorage.setItem('color-theme', 'light');
      } else {
        document.documentElement.classList.add('dark');
        localStorage.setItem('color-theme', 'dark');
      }
    },
    async logout() {
      try {
        // Отправьте запрос на выход с токеном в заголовке
        await this.$axios.post('auth/token/logout/', null);
        // Вызовите действие 'logout' из вашего хранилища, чтобы очистить данные о пользователе и токене
        this.$store.dispatch('logout');
      } catch (error) {
        // Обработайте ошибку, если выход не удался
        console.error('Ошибка при выходе:', error);
      }
    },
  },
};
</script>