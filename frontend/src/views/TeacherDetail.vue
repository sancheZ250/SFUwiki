<template>
  <div>
    <div class="teacher-info">
      <TeacherInfo :teacher="teacherData" :photo="teacherAvatar" />
      <div class="teacher-photo-carousel">
        <InstituteCarousel :photos="teacherPhotosForCarousel" />
      </div>
    </div>
    <div class="review-container">
      <template v-if="isAuthenticated">
        <div class="review-form">
          <ReviewForm :teacherId="teacherData.id" :addReview="addReview" />
        </div>
    </template>
    <template v-else>
      <p>
        Для того чтобы оставить отзыв, пожалуйста, 
        <router-link to="/login" class="text-blue-500">войдите в систему</router-link> или 
        <router-link to="/register" class="text-blue-500">зарегистрируйтесь</router-link>.
      </p>
    </template>
    <div class="review">
      <TeacherReviews :reviews="teacherReviews" :teacherName="teacherData.name" />
    </div>
      </div>
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


const addReview = (newReview) => {
  teacherReviews.value.unshift(newReview);
};

onMounted(async () => {
  const { instituteId, teacherId } = route.params;
  try {
    const response = await axios.get(`/api/v1/institutes/${instituteId}/teachers/${teacherId}/`);
    teacherData.value = response.data;
    teacherPhotos.value = response.data.photos;
    teacherAvatar.value = response.data.first_photo;
    teacherPhotosForCarousel.value = teacherPhotos.value;
    teacherReviews.value = response.data.reviews;
  } catch (error) {
    console.error('Ошибка при получении данных', error);
  }
});
</script>

<style>
.teacher-info {
  float: right;
  width: 40%;
  max-height: 200px;
  }


.review-container {
  display: flex;
  flex-direction: column; /* Это задаст вертикальное расположение */
}

.review {

}

.review-form {
  float: left;
}

.teacher-photo-carousel {
  
}

</style>