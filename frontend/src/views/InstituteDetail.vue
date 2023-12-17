<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import axios from 'axios';

import InstituteInfo from '../components/InstituteInfo.vue';
import DepartmentCard from '../components/DepartmentCard.vue';
import InstituteCarousel from '../components/Carousel.vue';
const institute = ref({});

const fetchInstitute = async () => {
  const route = useRoute();
  const id = route.params.id;

  try {
    const response = await axios.get(`/api/v1/institutes/${id}/`);
    institute.value = response.data;
  } catch (error) {
    console.error('Error fetching institute data', error);
  }
};

onMounted(() => {
  fetchInstitute();
});
</script>

<template>
  <div>
    <div class="bg-gray-100 dark:bg-gray-800 py-8">
      <div class="container mx-auto p-6 bg-white dark:bg-gray-700 shadow-lg rounded-lg">
        <InstituteInfo :institute="institute" />
        <InstituteCarousel :photos="institute.photos" />
        <h3 class="text-2xl text-gray-900 dark:text-white mt-8">Кафедры института:</h3>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mt-4">
          <DepartmentCard v-for="department in institute.departments" :key="department.id" :department="department" />
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped></style>