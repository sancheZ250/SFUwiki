<template>
  <div v-if="teacher" class="w-full bg-white dark:bg-gray-900 shadow-md p-4 rounded-lg overflow-hidden">
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
                  <select v-model="selectedInstitute" class="w-full border border-gray-300 p-2 rounded-md" required>
                    <option v-for="institute in institutesDepartments" :key="institute.id" :value="institute.id">{{
                      institute.name }}</option>
                  </select>
                </tr>
                <tr>
                  <select v-model="selectedDepartment" class="w-full border border-gray-300 p-2 rounded-md" required>
                    <option v-for="department in getDepartmentsByInstitute(selectedInstitute)" :key="department.id"
                      :value="department.id">{{ department.name }}</option>
                  </select>
                </tr>
                <tr>
                  <td class="font-semibold text-gray-700 dark:text-gray-400 pr-2">Биография:</td>
                  <td><textarea v-model="teacher.bio" class="w-full border border-gray-300 p-2 rounded-md"></textarea>
                  </td>
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
              <button type="button" @click="deleteTeacher"
                class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded mt-4">
                Удалить
              </button>
            </div>
          </div>
        </div>
        <div class="w-full md:w-1/3">
          <div class="w-full h-64 md:h-auto">
            <div v-if="!isPhotoChanged"><img
                class="object-cover w-full h-full rounded-l-lg border border-4 border-orange-400"
                :src="teacher.first_photo ? teacher.first_photo : no_photo" :alt="teacher.name" /></div>
            <div v-else><img class="object-cover w-full h-full rounded-l-lg border border-4 border-orange-400"
                :src="teacher.first_photo ? teacherPhotoUrl : no_photo" :alt="teacher.name" /></div>
          </div>
          <label for="file">Вы можете изменить фото:</label>
          <input id="file" type="file" @change="onFileChange" class="w-full border border-gray-300 p-2 rounded-md mt-2"
            accept="image/*" />
        </div>
      </div>
    </form>
  </div>
</template>
  
<script setup>
import no_photo from '../assets/no_photo.jpg';
import axios from 'axios';
import { ref, onMounted, watch } from 'vue';
import router from '../routes/index.js';

const props = defineProps({
  teacher: Object,
});
const institutesDepartments = ref([]); // Переменная для данных с API
const selectedInstitute = ref(null); // Хранение выбранного института
const selectedDepartment = ref(null); // Хранение выбранной кафедры
let teacherPhotoUrl = '';
let isPhotoChanged = false;

onMounted(async () => {
  try {
    const response = await axios.get('/api/v1/institute_departments_list/');
    // Используем данные из эндпоинта и заполняем институты
    institutesDepartments.value = response.data;
  } catch (error) {
    console.error('Ошибка при загрузке данных:', error);
  }
});

const getDepartmentsByInstitute = (instituteId) => {
  const foundInstitute = institutesDepartments.value.find(institute => institute.id === instituteId);
  return foundInstitute ? foundInstitute.departments : [];
};

if (props.teacher && props.teacher.first_photo) {
  teacherPhotoUrl = props.teacher.first_photo;
}

const onFileChange = (event) => {
  const file = event.target.files[0];
  if (file) {
    props.teacher.first_photo = file;
    isPhotoChanged = true;
    teacherPhotoUrl = URL.createObjectURL(file);
  }
};

const submitForm = () => {
  const teacherId = props.teacher.id;
  const updatedTeacher = {
    id: props.teacher.id,
    name: props.teacher.name,
    department: selectedDepartment.value,
    alma_mater: props.teacher.alma_mater,
    institute: selectedInstitute.value,
    bio: props.teacher.bio,
    date_published: props.teacher.date_published,
    created_by: props.teacher.created_by,
    is_published: true,
    ...(isPhotoChanged ? { first_photo: props.teacher.first_photo } : {}),
  };

  axios
    .put(`/api/v1/moderate-teachers/${teacherId}/`, updatedTeacher, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    })
    .then((response) => {
      console.log('Отправлено:', response.data);
      isPhotoChanged = false;
      router.push('/moderation')
    })
    .catch((error) => {
      console.error('Ошибка при отправке данных:', error);
    });
};

const deleteTeacher = () => {
  const teacherId = props.teacher.id;
  axios
    .delete(`/api/v1/moderate-teachers/${teacherId}/`)
    .then((response) => {
      console.log('Преподаватель удален:', response.data);
    })
    .catch((error) => {
      console.error('Ошибка при удалении преподавателя:', error);
    });
};
watch(() => props.teacher, (newValue) => {
  selectedInstitute.value = newValue.institute;
  selectedDepartment.value = newValue.department;
});
</script>