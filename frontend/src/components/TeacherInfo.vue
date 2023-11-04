<template>
  <div class="w-full flex flex-col-reverse md:flex-row bg-white dark:bg-gray-900 rounded-lg shadow-md p-4">
    <div class="w-full md:w-2/3">
      <div class="flex flex-col justify-between p-3 leading-normal">
        <h5 class="mb-2 text-xl font-bold text-gray-900 dark:text-white">
          {{ teacher.name }}
        </h5>
        <p class="mb-3 font-normal text-gray-700 dark:text-gray-400">
          {{ teacher.bio }}
        </p>
        <div class="mt-3">
          <div class="text-sm mb-1">Рейтинги:</div>
          <div class="flex space-x-2">
            <div>
              Знания: {{ teacher.knowledge_rating }}
            </div>
            <div>
              Навыки преподавания: {{ teacher.teaching_skill_rating }}
            </div>
            <div>
              Халявность: {{ teacher.easiness_rating }}
            </div>
            <div>
              Коммуникабельность: {{ teacher.communication_rating }}
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="w-full md:w-1/3">
      <img
        class="object-cover w-full h-64 md:h-auto md:w-full rounded-l-lg"
        :src="photo ? photo.photo : 'https://via.placeholder.com/150'"
        :alt="teacher.name"
      />
    </div>
  </div>
</template>

<script>
export default {
  props: {
    teacher: Object,
    photo: Object,
  },
};
</script>