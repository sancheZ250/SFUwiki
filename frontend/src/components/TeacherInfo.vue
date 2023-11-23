<template>
  <div class="w-full bg-white dark:bg-gray-900 shadow-md p-4 rounded-lg overflow-hidden">
    <div class="flex flex-col md:flex-row">
      <div class="w-full md:w-2/3 md:pr-4">
        <div class="flex flex-col justify-between p-3 leading-normal">
          <h5 class="mb-2 text-xl font-bold text-gray-900 dark:text-white">
            {{ teacher.name }}
          </h5>
          <table class="table-auto mb-3 text-gray-700 dark:text-gray-400">
            <tbody>
              <tr>
                <td class="font-semibold text-gray-700 dark:text-gray-400 pr-2">Биография:</td>
                <td>{{ teacher.bio }}</td>
              </tr>
              <tr>
                <td class="font-semibold text-gray-700 dark:text-gray-400 pr-2">Альма-матер:</td>
                <td>{{ teacher.alma_mater }}</td>
              </tr>
              <tr>
                <td class="font-semibold text-gray-700 dark:text-gray-400 pr-2">Дисциплины:</td>
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
          <div class="mt-3">
            <div class="text-sm mb-1 font-semibold text-gray-700 dark:text-gray-400">Рейтинги:</div>
            <div class="flex flex-wrap gap-2">
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
              <div class="text-gray-700 dark:text-gray-400">
                Общий рейтинг: {{ teacher.avg_rating }}
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="w-full md:w-full">
        <img class="object-cover w-full h-64 md:h-auto md:w-full rounded-l-lg border border-4 border-orange-400"
          :src="teacher.first_photo ? teacher.first_photo : no_photo" :alt="teacher.name" />
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