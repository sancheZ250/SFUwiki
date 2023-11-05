<template>
    <div>
      <DepartmentInfo :department="departmentData" />
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mt-4">
        <TeacherCard v-for="teacher in teacherList" :key="teacher.id" :teacher="teacher" />
      </div>
    </div>
  </template>
  
<script>
import { ref, onMounted } from 'vue';
import DepartmentInfo from '../components/DepartmentInfo.vue';
import TeacherCard from '../components/TeacherCard.vue';
import axios from 'axios';
import { useRoute } from 'vue-router';

export default {
  components: {
    DepartmentInfo,
    TeacherCard,
  },
  setup() {
    const departmentData = ref({});
    const teacherList = ref([]);

    const fetchData = async () => {
      const route = useRoute();
      try {
        const { instituteId, departmentId } = route.params;
        const response = await axios.get(`/api/v1/institutes/${instituteId}/departments/${departmentId}/`);
        departmentData.value = response.data;
        teacherList.value = response.data.teachers;
      } catch (error) {
        console.error('Ошибка при получении данных', error);
      }
    };

    onMounted(() => {
      fetchData();
    });

    return {
      departmentData,
      teacherList,
    };
  },
};
</script>
