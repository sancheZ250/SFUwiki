<script setup>
import { ref, onMounted } from 'vue';
import InstituteCard from '../components/InstituteCard.vue';
import axios from 'axios'; 

const instituteList = ref([]);

onMounted(async () => {
    try {
        const response = await axios.get('/api/v1/institutes/');
        instituteList.value = response.data;
    } catch (error) {
        console.error('Ошибка при получении данных:', error);
    }
})
</script>

<template>
    <div class="max-w-screen-xl mx-auto grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
      <InstituteCard v-for="institute in instituteList" :key="institute.id" :institute="institute" />
    </div>
  </template>


<style scoped>
  .institute-card {
    transition: transform 0.2s, box-shadow 0.2s;
  }

  .institute-card:hover {
    transform: scale(1.05);
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }
</style>

