<template>
    <div class="max-w-screen-xl mx-auto">
      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
        <TeacherCard v-for="teacher in teacherList" :key="teacher.id" :teacher="teacher" />
      </div>
      <Pagination :currentPage="currentPage" :totalPages="totalPages" @page-change="loadTeachers" />
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import TeacherCard from '../components/TeacherCard.vue';
  import Pagination from '../components/Pagination.vue';
  import axios from 'axios';
  
  const teacherList = ref([]);
  const currentPage = ref(1);
  const totalPages = ref(1);
  
  const loadTeachers = async (page) => {
    try {
      const response = await axios.get(`/api/v1/all_teachers/?page=${page}`);
      teacherList.value = response.data.results;
      currentPage.value = page;
      totalPages.value = Math.ceil(response.data.count / 2); //2 - количество преподавателей на 1 странице, ПОМЕНЯТЬ БЛЯДЬ ПОТОМ НА 9!
    } catch (error) {
      console.error('Ошибка при получении данных:', error);
    }
  };
  
  onMounted(() => {
    loadTeachers(currentPage.value);
  });
  </script>