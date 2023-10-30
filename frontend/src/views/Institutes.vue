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

