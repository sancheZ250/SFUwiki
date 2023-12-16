<template>
  <div class="container mx-auto px-4">
    <div class="flex flex-wrap -mx-4">
      <!-- Колонка для информации о преподавателе -->
      <div class="w-full lg:order-2 lg:w-1/2 px-4 mb-4 lg:mb-0">
        <TeacherInfo :teacher="teacherData" />
      </div>

      <!-- Колонка для формы редактирования или добавления отзыва -->
      <div class="w-full lg:order-1 lg:w-1/2 px-4">
        <template v-if="isAuthenticated">
          <template v-if="!hasReview">
            <ReviewForm :teacherId="teacherData.id" :addReview="addReview" />
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
      </div>
    </div>
    <!-- Колонка для отзывов -->
    <div class="w-full lg:order-3 px-4 mt-8">
      <TeacherReviews :reviews="teacherReviews" :teacherName="teacherData.name" />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import TeacherInfo from '../components/TeacherInfo.vue';
import TeacherCarousel from '../components/Carousel.vue';
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
  refreshData();
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
@media (min-width: 1024px) { /* lg: соответствует ширине экрана 1024px и выше */
  .teacher-info {
    float: right;
    width: 40%;
    max-height: 200px;
  }

  .review-container {
    display: flex;
    flex-direction: column;
    width: 60%;
    margin-right: auto;
  }
  
  .review-form {
    float: left;
    width: 100%;
  }

  .container {
    max-width: 1920px;
  }
}

.teacher-detail-container {
  display: flex;
  flex-direction: column;
}

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