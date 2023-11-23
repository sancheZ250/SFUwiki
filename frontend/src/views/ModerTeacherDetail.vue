<template>
    <div>
      <ModerTeacherInfo :teacher="teacherData" />
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted} from 'vue';
  import axios from 'axios';
  import ModerTeacherInfo from '../components/ModerTeacherInfo.vue';

  import { useRoute } from 'vue-router';
  import { useStore } from 'vuex';
  
  const store = useStore();
  const route = useRoute();
  
  const isAuthenticated = store.getters.isAuthenticated;
  const userId = store.getters.getUserId;
  const teacherId = route.params.teacherId;
  const teacherData = ref({});

  const getData = async () => {
  try {
    const response = await axios.get(`/api/v1/moderate-teachers/${teacherId}/`);
    teacherData.value = response.data;
  } catch (error) {
    console.error('Ошибка при получении данных', error);
  }
};

onMounted(getData);
  

  
  </script>