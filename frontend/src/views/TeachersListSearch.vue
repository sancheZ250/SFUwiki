<template>
  <div class="max-w-screen-xl mx-auto">
    <div class="mb-4">
      <input
        v-model="searchQuery"
        @input="searchTeachers"
        placeholder="Поиск по имени преподавателя"
        class="w-full px-4 py-2 rounded-lg border focus:ring-2 focus:ring-orange-600 dark:focus:ring-blue-800 dark:focus:border-blue-600"
      />
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
      <TeacherCard v-for="teacher in teacherList" :key="teacher.id" :teacher="teacher" :isModeration="false" />
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
const searchQuery = ref(''); // Добавляем реактивное свойство для поискового запроса

const loadTeachers = async (page) => {
  try {
    const response = await axios.get(`/api/v1/all_teachers/?page=${page}`, {
      params: {
        search: searchQuery.value, // Добавляем параметр поиска
      },
    });
    teacherList.value = response.data.results;
    currentPage.value = page;
    totalPages.value = Math.ceil(response.data.count / 9);
  } catch (error) {
    console.error('Ошибка при получении данных:', error);
  }
};

const searchTeachers = () => {
  loadTeachers(1); // Загрузка снова с первой страницы при поиске
};
onMounted(() => {
  loadTeachers(1);
});
</script>