<script setup>
defineProps({
    institute: Object
})
</script>

<template>
    <div class="max-w-sm bg-gray-900 border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700">
      <a href="#">
          <img class="rounded-t-lg" :src="institute.logo" :alt="institute.abbreviation" />
      </a>
      <div class="p-5">
          <a href="#">
              <h5 class="mb-2 text-2xl font-bold tracking-tight text-white dark:text-white">{{ institute.abbreviation }}</h5>
          </a>
          <p class="mb-3 font-normal text-gray-300 dark:text-gray-400">{{ institute.name }}</p>
          <a href="#" class="inline-flex items-center px-3 py-2 text-sm font-medium text-center text-white bg-orange-500 rounded-lg hover:bg-orange-600 focus:ring-4 focus:outline-none focus:ring-orange-300 dark:bg-orange-600 dark:hover:bg-orange-700 dark:focus:ring-orange-800">
              Перейти
              <svg class="w-3.5 h-3.5 ml-2" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 10">
                  <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M1 5h12m0 0L9 1m4 4L9 9"/>
              </svg>
          </a>
      </div>
    </div>
  </template>

<style scoped>

</style>