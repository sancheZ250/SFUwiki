<template>
  <div>
    <template v-if="$store.getters.isAuthenticated">
      <AddTeacherForm />
    </template>
    <template v-else>
      <p>
        Для того чтобы оставить отзыв, пожалуйста,
        <router-link to="/login" class="text-blue-500">войдите в систему</router-link> или
        <router-link to="/register" class="text-blue-500">зарегистрируйтесь</router-link>.
      <br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />
      </p>
    </template>
  </div>
</template>

<script>
import AddTeacherForm from "../components/AddTeacherForm.vue";
import { computed } from 'vue';
export default {
  components: {
    AddTeacherForm, // Регистрируем компонент AddTeacherForm
  },
};
</script>