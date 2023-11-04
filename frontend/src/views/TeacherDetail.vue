<template>
  <div>
    <TeacherInfo :teacher="teacherData" :photo="teacherAvatar" />
    <InstituteCarousel :photos="teacherPhotosForCarousel" />
    <TeacherReviews :reviews="teacherReviews" :teacherName="teacherData.name" />
    <template v-if="isAuthenticated">
      <template v-if="hasUserReviewed">
        <p>Вы уже оставили отзыв на этой странице преподавателя.</p>
      </template>
      <template v-else>
        <ReviewForm :teacherId="teacherData.id" :addReview="addReview" />
      </template>
    </template>
    <template v-else>
      <p>
        Для того чтобы оставить отзыв, пожалуйста, 
        <router-link to="/login" class="text-blue-500">войдите в систему</router-link> или 
        <router-link to="/register" class="text-blue-500">зарегистрируйтесь</router-link>.
      </p>
    </template>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import TeacherInfo from '../components/TeacherInfo.vue';
import InstituteCarousel from '../components/InstituteCarousel.vue';
import TeacherReviews from '../components/TeacherReviews.vue';
import ReviewForm from '../components/ReviewForm.vue';
import { useRoute } from 'vue-router';
import { useStore } from 'vuex';

const store = useStore();
const isAuthenticated = store.getters.isAuthenticated;
const userId = store.getters.getUserId;
const teacherData = ref({});
const teacherPhotos = ref([]);
const teacherReviews = ref([]);
const teacherAvatar = ref({});
const teacherPhotosForCarousel = ref([]);
const route = useRoute();

// Проверка на наличие отзыва пользователя
const hasUserReviewed = ref(false);

const addReview = (newReview) => {
  teacherReviews.value.push(newReview);
};

onMounted(async () => {
  const { instituteId, teacherId } = route.params;
  try {
    const response = await axios.get(`/api/v1/institutes/${instituteId}/teachers/${teacherId}/`);
    teacherData.value = response.data;
    teacherPhotos.value = response.data.photos;
    teacherAvatar.value = teacherPhotos.value[0];
    teacherPhotosForCarousel.value = teacherPhotos.value.slice(1);
    teacherReviews.value = response.data.reviews;

    // Проверка на наличие отзыва пользователя на этой странице преподавателя
    hasUserReviewed.value = teacherReviews.value.some(review => review.user_id === userId);
  } catch (error) {
    console.error('Ошибка при получении данных', error);
  }
});
</script>