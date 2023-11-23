<template>
    <div class="w-full bg-white dark:bg-gray-900 shadow-md p-4 rounded-lg overflow-hidden">
      <form @submit.prevent="submitForm">
        <div class="flex flex-col md:flex-row">
          <div class="w-full md:w-2/3 md:pr-4">
            <div class="flex flex-col justify-between p-3 leading-normal">
              <h5 class="mb-2 text-xl font-bold text-gray-900 dark:text-gray-400">
                Имя: формат "Фамилия Имя Отчество"
                <input v-model="teacher.name" class="w-full border border-gray-300 p-2 rounded-md" />
              </h5>
              <table class="table-auto mb-3 text-gray-700 dark:text-gray-400">
                <tbody>
                  <tr>
                    <td class="font-semibold text-gray-700 dark:text-gray-400 pr-2">Биография:</td>
                    <td><textarea v-model="teacher.bio" class="w-full border border-gray-300 p-2 rounded-md"></textarea></td>
                  </tr>
                  <tr>
                    <td class="font-semibold text-gray-700 dark:text-gray-400 pr-2">Альма-матер:</td>
                    <td><input v-model="teacher.alma_mater" class="w-full border border-gray-300 p-2 rounded-md" /></td>
                  </tr>
                </tbody>
              </table>
              <div class="mt-3">
                <button type="submit" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
                  Опубликовать
                </button>
              </div>
            </div>
          </div>
          <div class="w-full md:w-1/3">
            <div class="w-full h-64 md:h-auto">
              <img class="object-cover w-full h-full rounded-l-lg border border-4 border-orange-400"
                :src="teacher.first_photo ? teacher.first_photo : no_photo" :alt="teacher.name" />
            </div>
            <input v-model="teacher.first_photo" type="text" class="w-full border border-gray-300 p-2 rounded-md mt-2" />
          </div>
        </div>
      </form>
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
    methods: {
      submitForm() {
        console.log('Отправлено:', this.editedTeacher);
      },
    },
  };
  </script>