<template>
    <div>
        <h2>{{ formTitle }}</h2>
        <form @submit.prevent="submitForm">
            <div class="form-group">
                <label for="name">Имя:</label>
                <input type="text" id="name" v-model="teacher.name" required />
            </div>
            <div class="form-group">
                <label for="institute">Институт:</label>
                <select id="institute" v-model="teacher.institute" @change="updateDepartments" required>
                    <option value="">Выберите институт</option>
                    <option v-for="institute in institutes" :key="institute.id" :value="institute.id">
                        {{ institute.name }}
                    </option>
                </select>
            </div>
            <div class="form-group">
                <label for="department">Кафедра:</label>
                <select id="department" v-model="teacher.department" required>
                    <option value="">Выберите кафедру</option>
                    <option v-for="department in selectedInstitute?.departments" :key="department.id"
                        :value="department.id">
                        {{ department.name }}
                    </option>
                </select>
            </div>
            <div class="form-group">
                <label for="almaMater">Альма Матер:</label>
                <input type="text" id="almaMater" v-model="teacher.alma_mater" required />
            </div>
            <div class="form-group">
                <label for="bio">Биография:</label>
                <textarea id="bio" v-model="teacher.bio" required></textarea>
            </div>
            <div class="form-group">
                <label for="photos">Фотографии:</label>
                <input type="file" id="photos" ref="photoInput" multiple @change="handlePhotoUpload" />
            </div>
            <button type="submit">Отправить на модерацию</button>
            <div v-if="showSuccessModal" class="modal">
                <div class="modal-content">
                    <p class="success-message">{{ successMessage }}</p>
                    <button @click="closeSuccessModal">Закрыть</button>
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
                department: null,
                alma_mater: "",
                bio: "",
                institute: null,
            },
            departments: [],
            institutes: [],
            selectedInstitute: null,
            photos: [],
            showSuccessModal: false, // Добавляем состояние для управления видимостью модального окна
            successMessage: "", // Добавляем состояние для сообщения об успешной отправке
        };
    },
    methods: {
        handlePhotoUpload(event) {
            this.photos = event.target.files;
        },
        closeSuccessModal() {
            this.showSuccessModal = false;
        },
        async submitForm() {
            try {
                // Отправка данных о преподавателе на сервер
                const teacherResponse = await axios.post(`/api/v1/institutes/${this.teacher.institute}/teachers/`, this.teacher);
                const newTeacherId = teacherResponse.data.id;
                for (let i = 0; i < this.photos.length; i++) {
                    await this.uploadTeacherPhoto(newTeacherId, this.photos[i]);
                }
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
            this.teacher.department = null;
            this.teacher.alma_mater = "";
            this.teacher.bio = "";
            this.teacher.institute = null;
            this.departments = [];
            this.selectedInstitute = null;
            this.photos = [];
            this.$refs.photoInput.value = "";
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
            const selectedInstituteId = this.teacher.institute;
            if (selectedInstituteId) {
                const selectedInstitute = this.institutes.find((institute) => institute.id === selectedInstituteId);
                this.selectedInstitute = selectedInstitute;
            } else {
                this.selectedInstitute = null;
            }
            this.teacher.department = null;
        },
        async uploadTeacherPhoto(teacherId, photo) {
            try {
                const formData = new FormData();
                formData.append('photo', photo);
                formData.append('teacher', teacherId);

                await axios.post(`/api/v1/teacher-photos/`, formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data',
                    },
                });

                // Обработка успешной загрузки фотографии
            } catch (error) {
                // Обработка ошибки при загрузке фотографии
                console.error('Ошибка при загрузке фотографии:', error);
            }
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
    color: green;
    font-weight: bold;
}
</style>
