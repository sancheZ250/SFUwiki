<template>
    <form @submit.prevent="submitReview" class="bg-white dark:bg-gray-800 p-6 shadow-lg rounded-lg">
      <h3 class="text-2xl font-semibold mb-6 dark:text-gray-300">Оставьте свой отзыв</h3>
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
        <div class="mb-4">
          <label for="comment" class="block text-gray-700 dark:text-gray-400 font-semibold">Комментарий:</label>
          <textarea v-model="comment" id="comment" required rows="4" class="border p-2 w-full rounded-md dark:bg-gray-600 dark:text-white shadow-inner"></textarea>
        </div>
        <div class="mb-4">
          <label for="isAnonymous" class="block text-gray-700 dark:text-gray-400 font-semibold">Анонимно:</label>
          <input v-model="isAnonymous" type="checkbox" id="isAnonymous" class="mr-2">
        </div>
      </div>
      <button type="submit" class="mt-6 w-full bg-orange-500 text-white p-3 rounded-md hover:bg-orange-600 transition-colors duration-300">
      Отправить отзыв
    </button>
    </form>
  </template>
  
  <script>
  import axios from 'axios';
  import easinessIcon from '../assets/easinessIcon.png';
  import teachingSkillIcon from '../assets/teachingSkillIcon.png';
  import communicationIcon from '../assets/communicationIcon.png';
  import knowledgeIcon from '../assets/knowledgeIcon.png';
  
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
      getButtonClass(ratingType, num) {
      return [
        'w-8 h-8 rounded-full font-medium shadow-md',
        this[`${ratingType}Rating`] === num
        ];
      },
      setRating(ratingType, num) {
        console.log(`Setting ${ratingType} to ${num}`);
        this[`${ratingType}Rating`] = num;
    },
    },
  };
  </script>