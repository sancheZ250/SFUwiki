<script setup>
defineProps({
    institute: Object
})
</script>

<template>
    <div class="max-w-sm bg-white dark:bg-gray-900 border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700">
      <a href="#">
        <div class="image-container">
          <img class="rounded-t-lg" :src="institute.logo" :alt="institute.abbreviation" />
        </div>
      </a>
      <div class="p-5">
        <router-link :to="'/institutes/' + institute.id">
        <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">{{ institute.abbreviation }}</h5>
        <p class="mb-3 font-normal text-gray-700 dark:text-gray-400">{{ institute.name }}</p>
        <a class="inline-flex items-center px-3 py-2 text-sm font-medium text-center text-white bg-orange-500 rounded-lg hover:bg-orange-600 focus:ring-4 focus:outline-none focus:ring-orange-300 dark:bg-orange-600 dark:hover:bg-orange-700 dark:focus:ring-orange-800">
          Перейти
          <svg class="w-3.5 h-3.5 ml-2" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 10">
            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M1 5h12m0 0L9 1m4 4L9 9"/>
          </svg>
        </a>
      </router-link>
      </div>
    </div>
  </template>

<style scoped>
.image-container {
  width: 100%; /* Фиксированная ширина */
  height: 350px; /* Фиксированная высота */
  overflow: hidden; /* Обрезаем содержимое, которое не помещается */
}

.image-container img {
  width: 100%; /* Заполнение 100% ширины контейнера */
  height: 100%; /* Заполнение 100% высоты контейнера */
  object-fit: cover; /* Заполнение контейнера с сохранением соотношения сторон и обрезкой */
}
</style>