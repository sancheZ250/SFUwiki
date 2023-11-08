<template>
    <router-link :to="getTeacherLink(teacher)">
      <div class="max-w-md mx-auto bg-white dark:bg-gray-900 rounded-xl shadow-md overflow-hidden md:max-w-2xl m-4">
        <div class="md:flex">
          <div class="md:flex-shrink-0">
            <img class="h-48 w-full object-cover md:w-48" :src="teacher.first_photo" alt="">
          </div>
          <div class="p-8">
            <a href="#" class="block mt-1 text-lg leading-tight font-medium text-black dark:text-gray-300 hover:underline">{{ teacher.name }}</a>
            <div class="mt-4">
              <div class="flex items-center">
                <div class="flex items-center">
                  <div class="text-sm">
                    <div class="flex items-center mt-1">
                      <svg class="fill-current text-yellow-500 dark:text-yellow-300 w-4" viewBox="0 0 24 24">
                        <path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.62L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/>
                      </svg>
                      <span class="ml-2 dark:text-gray-400">{{ teacher.avg_rating }}</span>
                    </div>
                  </div>
                </div>
              </div>
              <div class="flex mt-4 items-center">
                <div class="text-sm">
                  <div class="flex items-center mt-1">
                    <svg class="fill-current text-gray-500 dark:text-gray-300 w-4" viewBox="0 0 24 24">
                      <path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.62L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/>
                    </svg>
                    <span class="ml-2 dark:text-gray-400">{{ teacher.review_count }}</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </router-link>
  </template>
  
  <script>
  export default {
    props: {
      teacher: Object,
      isModeration: Boolean,
    },
    methods: {
    getTeacherLink(teacher) {
      if (this.isModeration) {
        // Ссылка для модераторов
        return '/moderation/' + teacher.id;
      } else {
        // Ссылка для обычных пользователей
        return '/institutes/' + teacher.institute_id + '/teachers/' + teacher.id;
      }
    },
  },
  };
  </script>