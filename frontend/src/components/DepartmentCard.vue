<template>
  <router-link :to="'/institutes/' + department.institute_id + '/department/' + department.id">
  <div class="max-w-sm bg-white border border-gray-200 rounded-lg shadow hover:bg-gray-100 dark:border-gray-700 dark:bg-gray-800 dark:hover:bg-gray-700">
    <div class="h-48 bg-cover bg-center rounded-t-lg" :style="`background-image: url(${department.logo})`"></div>
    <div class="p-4">
      <h5 class="text-2xl font-bold text-gray-900 dark:text-white">{{ department.name }}</h5>
      <p class="mt-2 text-gray-700 dark:text-gray-400">{{ department.description }}</p>
    </div>
  </div>
</router-link>
</template>
  
<script setup>
import { ref } from 'vue';

const props = defineProps({
  department: Object,
});
</script>