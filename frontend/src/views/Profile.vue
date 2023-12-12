<template>
  <div class="container mx-auto p-8">
    <div class="flex flex-col md:flex-row">
      <!-- Блок с фотографией пользователя -->
      <div class="photo w-full md:w-1/2">
        <img v-if="user.profile && user.profile.avatar" :src="user.profile.avatar" alt="User avatar" class="w-full h-auto rounded-lg shadow-md"/>
      </div>

      <!-- Блок с информацией о пользователе -->
      <div class="info w-full md:w-1/2 mt-4 md:mt-0 md:ml-4">
        <div v-if="user" class="user-info">
          <!-- Информационный блок с именем пользователя -->
          <div class="info-block bg-blue-300 p-4 rounded-lg shadow-sm mb-4">
            <h1 class="username text-xl font-bold">{{ user.username }}</h1>
          </div>

          <!-- Информационный блок с полным именем пользователя -->
          <div class="info-block bg-green-300 p-4 rounded-lg shadow-sm mb-4">
            <p class="name">{{ user.first_name }} {{ user.last_name }}</p>
          </div>

          <!-- Информационный блок с репутацией пользователя -->
          <div class="info-block bg-red-300 p-4 rounded-lg shadow-sm mb-4">
            <p class="reputation">Репутация: {{ user.profile.reputation }}</p>
          </div>

          <!-- Информационный блок с датой присоединения пользователя -->
          <div class="info-block bg-yellow-300 p-4 rounded-lg shadow-sm">
            <p class="join-date">С нами с: {{ formatDate(user.date_joined) }}</p>
          </div>
        </div>
        <div v-else class="loading">
          <p>Loading...</p>
        </div>
      </div>
    </div>
  </div>
</template>


  
  <script>
  import axios from 'axios';
  import { useRoute } from 'vue-router';

  
  export default {
    data() {
      return {
        user: null,
      };
    },
    async created() {
      const route = useRoute();
      const userId = route.params.id;
      const response = await axios.get(`/api/v1/profile/${userId}/`); // Replace with the correct URL
      this.user = response.data;
    },
    methods: {
    formatDate(dateStr) {
      const months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря'];
      const date = new Date(dateStr);
      const day = date.getDate();
      const month = months[date.getMonth()];
      const year = date.getFullYear();
      return `${day < 10 ? '0' + day : day} ${month} ${year} года`;
    }
  },
  };
  </script>
  
  <style scoped>
  .avatar {
    /* Стили для аватара пользователя */
    border: 3px solid white;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }

  .name, .reputation, .join-date {
    /* Стили для дополнительной информации о пользователе */
    margin-top: 2px;
    font-size: 1rem;
  }
</style>
