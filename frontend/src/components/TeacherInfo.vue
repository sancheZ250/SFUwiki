<template>
  <div class="w-full flex flex-col-reverse md:flex-row bg-white dark:bg-gray-900 shadow-md p-4">
    <div class="w-full md:w-3/3">
      <div class="flex flex-col justify-between p-3 leading-normal">
        <h5 class="mb-2 text-xl font-bold text-gray-900 dark:text-white">
          {{ teacher.name }}
        </h5>
        <p class="mb-3 font-normal text-gray-700 dark:text-gray-400">
          Биография:
          {{ teacher.bio }}
        </p>
        <p class="mb-3 font-normal text-gray-700 dark:text-gray-400">
          Альма-матер:
          {{ teacher.alma_mater }}
        </p>
        <div class="mt-3">
          <div class="mb-3 font-normal text-gray-700 dark:text-gray-400">Дисциплины:</div>
          <ul class="mb-3 font-normal text-gray-700 dark:text-gray-400">
            <li v-for="discipline in teacher.disciplines" :key="discipline.id">
              {{ discipline.name }}
            </li>
          </ul>
        </div>
        <div class="mt-3">
          <div class="text-sm mb-1 text-gray-700 dark:text-gray-400">Рейтинги:</div>
          <div class="flex space-x-2">
            <div class="text-gray-700 dark:text-gray-400">
              Знания: {{ teacher.knowledge_rating }}
            </div>
            <div class="text-gray-700 dark:text-gray-400">
              Навыки преподавания: {{ teacher.teaching_skill_rating }}
            </div>
            <div class="text-gray-700 dark:text-gray-400">
              Халявность: {{ teacher.easiness_rating }}
            </div>
            <div class="text-gray-700 dark:text-gray-400">
              Коммуникабельность: {{ teacher.communication_rating }}
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="w-full md:w-full">
      <img
        class="object-cover w-full h-64 md:h-auto md:w-full rounded-l-lg border border-4 border-orange-400"
        :src="teacher.first_photo ? teacher.first_photo : no_photo"
        :alt="teacher.name"
      />
    </div>
  </div>
</template>

<script>
import no_photo from '../assets/no_photo.jpg';
export default {
  props: {
    teacher: Object,
  },
  data() {
    return {
      no_photo,
    };
  },
  computed: {
    photoSource() {
      return this.teacher.first_photo ? this.teacher.first_photo : require('@/assets/anon.jpg');
    },
  },
};
</script>