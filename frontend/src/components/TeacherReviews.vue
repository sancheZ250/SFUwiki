<template>
    <div class="bg-gray-100 dark:bg-gray-800 p-8">
        <h2 class="text-3xl font-semibold mb-6 dark:text-gray-400">Отзывы о преподавателе {{ teacherName }}</h2>
        <div class="grid grid-cols-1 gap-6">
            <div v-for="review in reviews" :key="review.id"
                class="bg-white dark:bg-gray-900 text-gray-700 dark:text-gray-500 rounded-lg shadow-md p-6">
                <router-link :to="!review.is_anonymous ? `/profile/${review.student.id}` : `#`">
                <div class="flex items-center mb-4">
                    <div class="w-24 h-24 rounded-full overflow-hidden">
                        <img v-if="!review.is_anonymous && review.student && review.student.profile && review.student.profile.avatar"
                            :src="review.student.profile.avatar" alt="../assets/anon.jpg"
                            class="w-full h-full object-cover" />
                        <img v-else src="../assets/anon.jpg" alt="../assets/anon.jpg" class="w-full h-full object-cover" />
                    </div>
                    <div class="ml-4">
                        <!-- <router-link :to="`/profile/${review.student.id}`"> -->
                            <p class="text-lg font-semibold">{{ review.is_anonymous ? 'Анонимный пользователь' :
                                review.student.username }}</p>
                        <!-- </router-link> -->
                        <p class="text-gray-600">{{ formatDate(review.created_at) }}</p>
                    </div>
                </div>
            </router-link>
                <div class="mb-4">
                    <p class="text-xl font-semibold">Знания: {{ review.knowledge_rating }}</p>
                    <p class="text-xl font-semibold">Преподавательские навыки: {{ review.teaching_skill_rating }}</p>
                    <p class="text-xl font-semibold">Халявность: {{ review.easiness_rating }}</p>
                    <p class="text-xl font-semibold">Коммуникабельность: {{ review.communication_rating }}</p>
                </div>
                <p class="text-gray-700 dark:text-gray-500">{{ review.comment }}</p>
            </div>
        </div>
    </div>
</template>
  
<script>
import { format, parseISO } from 'date-fns';

export default {
    props: {
        reviews: Array,
        teacherName: String,
    },
    methods: {
        formatDate(dateString) {
            const date = parseISO(dateString); // Преобразовать строку в объект даты
            return format(date, 'dd MMM yyyy HH:mm'); // Форматировать дату как '02 Nov 2023 13:27'
        },
    },
};
</script>