<template>
    <div class="profile">
      <h1>User Profile</h1>
      <div v-if="user">
        <p><strong>Ник:</strong> {{ user.username }}</p>
        <img :src="user.profile.avatar" alt="User avatar" /> 
        <p><strong>Имя:</strong> {{ user.first_name }}</p>
        <p><strong>Фамилия:</strong> {{ user.last_name }}</p>
        <p><strong>РеП:</strong> {{ user.profile.reputation }}</p>
        <p><strong>С нами с:</strong> {{ user.date_joined }}</p>
      </div>
      <div v-else>
        <p>Loading...</p>
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
  };
  </script>
  
  <style scoped>
  /* Add your styles here */
  </style>