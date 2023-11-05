<template>
    <form @submit.prevent="submitReview" class="bg-white dark:bg-gray-900 p-4 shadow-md">
      <h3 class="text-xl font-semibold mb-4 dark:text-gray-400">Оставьте свой отзыв</h3>
      <div class="mb-4">
        <label for="knowledgeRating" class="block text-gray-700 dark:text-gray-400 font-semibold">Знания:</label>
        <input v-model="knowledgeRating" type="number" id="knowledgeRating" min="1" max="5" required class="border p-2 rounded-md dark:bg-gray-600 dark:text-white">
      </div>
      <div class="mb-4">
        <label for="teachingSkillRating" class="block text-gray-700 dark:text-gray-400 font-semibold">Преподавательские навыки:</label>
        <input v-model="teachingSkillRating" type="number" id="teachingSkillRating" min="1" max="5" required class="border p-2 rounded-md dark:bg-gray-600 dark:text-white">
      </div>
      <div class="mb-4">
        <label for="easinessRating" class="block text-gray-700 dark:text-gray-400 font-semibold">Халявность:</label>
        <input v-model="easinessRating" type="number" id="easinessRating" min="1" max="5" required class="border p-2 rounded-md dark:bg-gray-600 dark:text-white">
      </div>
      <div class="mb-4">
        <label for="communicationRating" class="block text-gray-700 dark:text-gray-400 font-semibold">Общение:</label>
        <input v-model="communicationRating" type="number" id="communicationRating" min="1" max="5" required class="border p-2 rounded-md dark:bg-gray-600 dark:text-white">
      </div>
      <div class="mb-4">
        <label for="comment" class="block text-gray-700 dark:text-gray-400 font-semibold">Комментарий:</label>
        <textarea v-model="comment" id="comment" required rows="4" class="border p-2 rounded-md dark:bg-gray-600 dark:text-white"></textarea>
      </div>
      <div class="mb-4">
        <label for="isAnonymous" class="block text-gray-700 dark:text-gray-400 font-semibold">Анонимно:</label>
        <input v-model="isAnonymous" type="checkbox" id="isAnonymous" class="mr-2">
      </div>
      <button type="submit" class="bg-blue-500 text-white p-2 rounded-md">Отправить отзыв</button>
    </form>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    props: {
      teacherId: Number,
      addReview: Function,
    },
    data() {
      return {
        knowledgeRating: 5,
        teachingSkillRating: 5,
        easinessRating: 5,
        communicationRating: 5,
        comment: '',
        isAnonymous: false,
      };
    },
    methods: {
      async submitReview() {
        try {
          const response = await axios.post(`/api/v1/teachers/${this.teacherId}/reviews/`, {
            knowledge_rating: this.knowledgeRating,
            teaching_skill_rating: this.teachingSkillRating,
            easiness_rating: this.easinessRating,
            communication_rating: this.communicationRating,
            comment: this.comment,
            is_anonymous: this.isAnonymous,
          });
  
          // Обработайте успешное добавление отзыва
          const newReview = response.data;
          console.log('Отзыв успешно добавлен:', response.data);
          this.addReview(newReview);
          // Опционально: очистите поля формы после отправки
          this.knowledgeRating = 5;
          this.teachingSkillRating = 5;
          this.easinessRating = 5;
          this.communicationRating = 5;
          this.comment = '';
          this.isAnonymous = false;
        } catch (error) {
          // Обработайте ошибку при добавлении отзыва
          console.error('Ошибка при добавлении отзыва', error);
        }
      },
    },
  };
  </script>