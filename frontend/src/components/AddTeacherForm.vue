<template>
  <div>
    <h2 class="text-xl font-semibold mb-4">{{ formTitle }}</h2>
    <form @submit.prevent="submitForm" class="max-w-md">
      <div class="mb-6">
        <label for="name" class="block text-sm font-medium text-gray-700 mb-2">Имя:</label>
        <input type="text" id="name" v-model="teacher.name" required
          class="w-full border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:border-blue-500" />
      </div>
      <div class="mb-6">
        <label for="institute_id" class="block text-sm font-medium text-gray-700 mb-2">Институт:</label>
        <select id="institute_id" v-model="teacher.institute_id" @change="updateDepartments" required
          class="w-full border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:border-blue-500">
          <option value="">Выберите институт</option>
          <option v-for="institute in institutes" :key="institute.id" :value="institute.id">
            {{ institute.name }}
          </option>
        </select>
      </div>
      <div class="mb-6">
        <label for="department_id" class="block text-sm font-medium text-gray-700 mb-2">Кафедра:</label>
        <select id="department_id" v-model="teacher.department_id" required
          class="w-full border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:border-blue-500">
          <option value="">Выберите кафедру</option>
          <option v-for="department in selectedInstitute?.departments" :key="department.id" :value="department.id">
            {{ department.name }}
          </option>
        </select>
      </div>
      <div class="mb-6">
        <label for="almaMater" class="block text-sm font-medium text-gray-700 mb-2">Альма Матер:</label>
        <input type="text" id="almaMater" v-model="teacher.alma_mater" required
          class="w-full border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:border-blue-500" />
      </div>
      <div class="mb-6">
        <label for="bio" class="block text-sm font-medium text-gray-700 mb-2">Биография:</label>
        <textarea id="bio" v-model="teacher.bio" required
          class="w-full border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:border-blue-500"></textarea>
      </div>
      <div class="mb-6">
        <label for="photo" class="block text-sm font-medium text-gray-700 mb-2">Фото:</label>
        <div class="flex items-center justify-between">
          <label for="photo"
            class="w-48 flex items-center px-4 py-2 bg-white text-blue-500 rounded border border-blue-500 hover:bg-blue-500 hover:text-white cursor-pointer">
            <span>Выбрать файл</span>
            <input type="file" id="photo" @change="handlePhotoUpload" accept="image/*" class="hidden" />
          </label>
          <span v-if="teacher.first_photo" class="text-gray-700">{{ teacher.first_photo.name }}</span>
        </div>
      </div>
      <button type="submit"
        class="w-full bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">Отправить
        на модерацию</button>
      <div class="mb-6">
        <label for="photo" class="block text-sm font-medium text-gray-700 mb-2">Фото:</label>
        <div class="flex items-center justify-between">
          <span v-if="showPreview">
            <img :src="imagePreview" alt="Preview" class="w-48 h-48 object-cover rounded">
          </span>
          <span v-else-if="teacher.first_photo" class="text-gray-700">{{ teacher.first_photo.name }}</span>
        </div>
      </div>
      <div v-if="showSuccessModal" class="modal">
        <div class="modal-content">
          <p class="success-message">{{ successMessage }}</p>
          <button @click="closeSuccessModal"
            class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">Закрыть</button>
        </div>
      </div>
    </form>

  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      formTitle: "Добавить преподавателя",
      teacher: {
        name: "",
        department_id: null,
        alma_mater: "",
        bio: "",
        institute_id: null,
        first_photo: null
      },
      departments: [],
      institutes: [],
      selectedInstitute: null,
      showSuccessModal: false, // состояние для управления видимостью модального окна
      successMessage: "", // состояние для сообщения об успешной отправке
      file: '',
      showPreview: false,
      imagePreview: ''
    };
  },
  methods: {
    handlePhotoUpload(event) {
      this.teacher.first_photo = event.target.files[0];
      this.showPreview = true;
      this.imagePreview = URL.createObjectURL(event.target.files[0]);
    },
    closeSuccessModal() {
      this.showSuccessModal = false;
    },
    async submitForm() {
      try {
        // Отправка данных о преподавателе на сервер
        const teacherResponse = await axios.post(`/api/v1/institutes/${this.teacher.institute_id}/teachers/`, this.teacher, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        })
        // Обработка успешного ответа и перенаправление или вывод сообщения об успехе
        this.successMessage = "Преподаватель отправлен на модерацию, спасибо за ваш вклад в развитие проекта";
        this.showSuccessModal = true;
        this.clearForm();
      } catch (error) {
        // Обработка ошибки при отправке данных на сервер
        console.error('Ошибка при отправке данных на сервер:', error);
      }
    },
    clearForm() {
      this.teacher.name = "";
      this.teacher.department_id = null;
      this.teacher.alma_mater = "";
      this.teacher.bio = "";
      this.teacher.institute_id = null;
      this.departments = [];
      this.selectedInstitute = null;
      this.teacher.first_photo = null;
    },
    async fetchInstitutesAndDepartments() {
      try {
        const response = await axios.get('/api/v1/institute_departments_list/');
        this.institutes = response.data;
      } catch (error) {
        console.error('Ошибка при получении данных об институтах и кафедрах:', error);
      }
    },
    updateDepartments() {
      const selectedInstituteId = this.teacher.institute_id;
      if (selectedInstituteId) {
        const selectedInstitute = this.institutes.find((institute) => institute.id === selectedInstituteId);
        this.selectedInstitute = selectedInstitute;
      } else {
        this.selectedInstitute = null;
      }
      this.teacher.department_id = null;
    },
  },
  created() {
    this.fetchInstitutesAndDepartments();
  },
};
</script>

<style scoped>
.form-group {
  margin-bottom: 1rem;
}

.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 100;
}

.modal-content {
  background: white;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
  text-align: center;
}

.success-message {
  color: rgb(0, 200, 40);
  font-weight: bold;
}</style>