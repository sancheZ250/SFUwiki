<template>
    <div class="teacher-info">
      <TeacherInfo :teacher="teacherData" />
      <template v-if="teacherPhotos && teacherPhotos.length">
        <div class="teacher-photo-carousel">
          <InstituteCarousel :photos="teacherPhotos" />
        </div>
      </template>
    </div>
    <div class="review-container">
      <template v-if="isAuthenticated">
        <template v-if="!hasReview">
          <div class="review-form">
            <ReviewForm :teacherId="teacherData.id" :addReview="addReview" />
          </div>
        </template>
        <template v-else>
          <ReviewEditForm :userReview="currentUserReview" :editReview="editReview"/>
        </template>
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
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import TeacherInfo from '../components/TeacherInfo.vue';
import InstituteCarousel from '../components/InstituteCarousel.vue';
import TeacherReviews from '../components/TeacherReviews.vue';
import ReviewForm from '../components/ReviewForm.vue';
import ReviewEditForm from '../components/ReviewEditForm.vue';
import { useRoute } from 'vue-router';
import { useStore } from 'vuex';

const store = useStore();
const route = useRoute();

const isAuthenticated = store.getters.isAuthenticated;
const userId = store.getters.getUserId;

const teacherData = ref({});
const teacherPhotos = ref([]);
const teacherReviews = ref([]);
const currentUserReview = ref({});

const addReview = (newReview) => {
  teacherReviews.value.unshift(newReview);
};
const editReview = () =>{
  refreshData();
};
const { instituteId, teacherId } = route.params;
const hasReview = ref(false);

const refreshData = async () => {
  try {
    const response = await axios.get(`/api/v1/institutes/${instituteId}/teachers/${teacherId}/`);
    teacherData.value = response.data;
    teacherPhotos.value = response.data.photos;
    teacherReviews.value = response.data.reviews;
    const reviewResponse = await axios.get(`/api/v1/check-review-unique/${teacherId}/`);
    hasReview.value = reviewResponse.data.has_review;
    currentUserReview.value = teacherReviews.value.find(review => review.student.id === parseInt(userId));
  } catch (error) {
    console.error('Ошибка при получении данных', error);
  }
};

onMounted(refreshData);

</script>

<style>
.teacher-info {
  float: right;
  width: 40%;
  max-height: 200px;
}


.review-container {
  display: flex;
  flex-direction: column;
}



.review-form {
  float: left;
}
</style>