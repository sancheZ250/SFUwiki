<template>
  <div>
    <form @submit.prevent="updateReview" class="bg-white dark:bg-gray-800 p-6 shadow-lg rounded-lg">
      <h3 class="text-2xl font-semibold mb-6 dark:text-gray-300">Редактирование отзыва</h3>
      <div class="space-y-4">
        <!-- Блоки оценок -->
        <div v-for="ratingType in ratingTypes" :key="ratingType.name" class="flex items-center space-x-2">
          <label :for="ratingType.name" class="block text-gray-700 dark:text-gray-400 font-semibold capitalize">
            {{ ratingType.label }}:
          </label>
          <div class="flex space-x-1">
            <button v-for="num in [1, 2, 3, 4, 5]" :key="num" type="button" :class="getButtonClass(ratingType.name, num)"
                @click="setRating(ratingType.name, num)">
              <img v-if="num <= this[`${ratingType.name}Rating`]" :src="ratingType.icon" class="w-8 h-8"/>
              <img v-else :src="ratingType.icon" class="w-8 h-8" style="opacity: 0.3;"/>
            </button>
          </div>
        </div>
        <!-- Комментарий и анонимность -->
        <div class="mb-4">
          <label for="comment" class="block text-gray-700 dark:text-gray-400 font-semibold">Комментарий:</label>
          <textarea v-model="comment" id="comment" required rows="4" class="border p-2 w-full rounded-md dark:bg-gray-600 dark:text-white shadow-inner"></textarea>
        </div>
        <div class="mb-4">
          <label for="isAnonymous" class="block text-gray-700 dark:text-gray-400 font-semibold">Анонимно:</label>
          <input v-model="isAnonymous" type="checkbox" id="isAnonymous" class="mr-2">
        </div>
      </div>
      <!-- Кнопки обновления и удаления отзыва -->
      <div class="flex space-x-2 mt-6">
        <button 
          type="submit" 
          class="flex-1 bg-blue-500 text-white p-3 rounded-lg hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-700 focus:ring-opacity-50 transition ease-in-out duration-300 shadow-lg"
        >
          Обновить отзыв
        </button>
        <button 
          type="button" 
          @click="deleteReview" 
          class="flex-1 bg-red-500 text-white p-3 rounded-lg hover:bg-red-600 focus:outline-none focus:ring-2 focus:ring-red-700 focus:ring-opacity-50 transition ease-in-out duration-300 shadow-lg"
        >
          Удалить отзыв
        </button>
      </div>

    </form>
  </div>
</template>

<script>
import axios from 'axios';
import easinessIcon from '../assets/easinessIcon.png';
import teachingSkillIcon from '../assets/teachingSkillIcon.png';
import communicationIcon from '../assets/communicationIcon.png';
import knowledgeIcon from '../assets/knowledgeIcon.png';

export default {
  props: {
    userReview: Object,
    editReview: Function,
  },
  data() {
    return {
      knowledgeRating: this.userReview.knowledge_rating,
      teachingSkillRating: this.userReview.teaching_skill_rating,
      easinessRating: this.userReview.easiness_rating,
      communicationRating: this.userReview.communication_rating,
      comment: this.userReview.comment,
      isAnonymous: this.userReview.is_anonymous,

      ratingTypes: [
        {
          name: 'knowledge',
          label: 'Знания',
          icon: knowledgeIcon
        },
        {
          name: 'communication',
          label: 'Коммуникабельность',
          icon: communicationIcon
        },
        {
          name: 'easiness',
          label: 'Халявность',
          icon: easinessIcon
        },
        {
          name: 'teachingSkill',
          label: 'Преподавательские навыки',
          icon: teachingSkillIcon
        }
      ]
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

        console.log('Отзыв успешно обновлен:', response.data);
        this.editReview();
      } catch (error) {
        console.error('Ошибка при обновлении отзыва', error);
      }
    },
    async deleteReview() {
      try {
        await axios.delete(`/api/v1/teachers/${this.userReview.teacher_id}/reviews/${this.userReview.id}/`);
        console.log('Отзыв успешно удален');
        this.editReview();
      } catch (error) {
        console.error('Ошибка при удалении отзыва', error);
      }
    },
    setRating(ratingType, num) {
      this[`${ratingType}Rating`] = num;
    },
    getButtonClass(ratingType, num) {
      return [
        'w-8 h-8 rounded-full font-medium shadow-md',
        this[`${ratingType}Rating`] === num
      ];
    },
  },
};
</script>