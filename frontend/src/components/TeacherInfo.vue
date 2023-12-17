<template>
  <div class="bg-white dark:bg-gray-900 shadow-md p-4 rounded-lg overflow-hidden">
    <div class="flex flex-col lg:flex-row items-center lg:items-start">
      <div class="flex-1">
        <div class="p-3 leading-normal">
          <h5 class="mb-2 text-xl font-bold text-gray-900 dark:text-white">
            {{ teacher.name }}
          </h5>
          <table class="table-auto mb-3 text-gray-700 dark:text-gray-400">
            <tbody>
              <tr>
                <td class="font-semibold pr-2">Биография:</td>
                <td>{{ teacher.bio }}</td>
              </tr>
              <tr>
                <td class="font-semibold pr-2">Альма-матер:</td>
                <td>{{ teacher.alma_mater }}</td>
              </tr>
              <tr>
                <td class="font-semibold pr-2">Дисциплины:</td>
                <td>
                  <ul class="list-disc list-inside">
                    <li v-for="discipline in teacher.disciplines" :key="discipline.id">
                      {{ discipline.name }}
                    </li>
                  </ul>
                </td>
              </tr>
            </tbody>
          </table>
          <div>
            <div class="text-sm mb-1 font-semibold dark:text-gray-400">Рейтинги:</div>
            <div class="flex flex-wrap gap-2 dark:text-gray-400">
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
              <div>
                Общий рейтинг: {{ teacher.avg_rating }}
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="lg:w-2/3">
        <!-- Изображение преподавателя -->
        <img 
          class="w-96 h-auto lg:w-full lg:h-auto object-cover rounded-lg border border-4 border-orange-400" 
          :src="teacher.first_photo ? teacher.first_photo : no_photo" 
          :alt="teacher.name" 
        />
      </div>
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
};
</script>

<style>
@media (min-width: 1024px) {
  .teacher-info {
    display: flex;
    justify-content: space-between;
  }
  .teacher-info > div {
    /* Adjust the width as necessary */
    width: calc(50% - 1rem); /* Subtracting the gap you want */
  }
  .teacher-info-image {
    /* Adjust the size as necessary */
    max-width: 250px; /* This controls the size of the image */
    max-height: 250px;
  }
}
</style>
