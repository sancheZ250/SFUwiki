<template>
    <div class="w-full flex flex-col-reverse md:flex-row">
      <div class="w-full md:w-2/3">
        <div class="flex flex-col justify-between p-4 leading-normal">
          <h5 class="mb-2 text-2xl font-bold text-gray-900 dark:text-white">
            {{ department.name }}
          </h5>
          <p class="mb-3 font-normal text-gray-700 dark:text-gray-400">
            {{ department.description }}
          </p>
        </div>
      </div>
      <div class="w-full md:w-1/3">
        <img
          class="object-cover w-full h-96 md:h-auto md:w-full md:rounded-l-lg"
          :src="department.logo"
          :alt="department.name"
        />
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      department: Object,
    },
  };
  </script>