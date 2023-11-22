<template>
  <form @submit.prevent="updateReview" class="bg-white dark:bg-gray-900 p-4 shadow-md">
    <h3 class="text-xl font-semibold mb-4 dark:text-gray-400">Ваш отзыв на преподавателя, можете его отредактировать</h3>
    <div class="mb-4">
      <label for="knowledgeRating" class="block text-gray-700 dark:text-gray-400 font-semibold">Знания:</label>
      <input v-model="knowledgeRating" type="number" id="knowledgeRating" min="1" max="5" required
        class="border p-2 rounded-md dark:bg-gray-600 dark:text-white">
    </div>
    <div class="mb-4">
      <label for="teachingSkillRating" class="block text-gray-700 dark:text-gray-400 font-semibold">Преподавательские
        навыки:</label>
      <input v-model="teachingSkillRating" type="number" id="teachingSkillRating" min="1" max="5" required
        class="border p-2 rounded-md dark:bg-gray-600 dark:text-white">
    </div>
    <div class="mb-4">
      <label for="easinessRating" class="block text-gray-700 dark:text-gray-400 font-semibold">Халявность:</label>
      <input v-model="easinessRating" type="number" id="easinessRating" min="1" max="5" required
        class="border p-2 rounded-md dark:bg-gray-600 dark:text-white">
    </div>
    <div class="mb-4">
      <label for="communicationRating" class="block text-gray-700 dark:text-gray-400 font-semibold">Общение:</label>
      <input v-model="communicationRating" type="number" id="communicationRating" min="1" max="5" required
        class="border p-2 rounded-md dark:bg-gray-600 dark:text-white">
    </div>
    <div class="mb-4">
      <label for="comment" class="block text-gray-700 dark:text-gray-400 font-semibold">Комментарий:</label>
      <textarea v-model="comment" id="comment" required rows="4"
        class="border p-2 rounded-md dark:bg-gray-600 dark:text-white"></textarea>
    </div>
    <div class="mb-4">
      <label for="isAnonymous" class="block text-gray-700 dark:text-gray-400 font-semibold">Анонимно:</label>
      <input v-model="isAnonymous" type="checkbox" id="isAnonymous" class="mr-2">
    </div>
    <button type="submit" class="bg-blue-500 text-white p-2 rounded-md">Обновить отзыв</button>
    <button @click="deleteReview" class="bg-red-500 text-white p-2 rounded-md mt-4">Удалить отзыв</button>
  </form>
</template>
  
<script>
import axios from 'axios';

export default {
  props: {
    userReview: Object, // Существующий отзыв пользователя для редактирования
  },
  data() {
    return {
      knowledgeRating: this.userReview.knowledge_rating,
      teachingSkillRating: this.userReview.teaching_skill_rating,
      easinessRating: this.userReview.easiness_rating,
      communicationRating: this.userReview.communication_rating,
      comment: this.userReview.comment,
      isAnonymous: this.userReview.is_anonymous,
    };
  },
  methods: {
    async updateReview() {
      try {
        const response = await axios.put(`/api/v1/teachers/${this.userReview.teacher_id}/reviews/${this.userReview.id}/`, {
          knowledge_rating: this.knowledgeRating,
          teaching_skill_rating: this.teachingSkillRating,
          easiness_rating: this.easinessRating,
          communication_rating: this.communicationRating,
          comment: this.comment,
          is_anonymous: this.isAnonymous,
        });

        // Обработай успешное обновление отзыва
        console.log('Отзыв успешно обновлен:', response.data);
      } catch (error) {
        // Обработай ошибку при обновлении отзыва
        console.error('Ошибка при обновлении отзыва', error);
      }
    },
    async deleteReview() {
      try {
        await axios.delete(`/api/v1/teachers/${this.userReview.teacher_id}/reviews/${this.userReview.id}/`);
        console.log('Отзыв успешно удален');
      } catch (error) {
        console.error('Ошибка при удалении отзыва', error);
      }
    },
  },
};
</script>