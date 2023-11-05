<template>
    <nav aria-label="Page navigation">
      <ul class="flex items-center -space-x-px h-8 text-sm">
        <li>
          <button
            @click="goToPage(prevPage)"
            :disabled="prevPage === null"
            class="flex items-center justify-center px-3 h-8 leading-tight text-orange-500 bg-white border border-orange-300 hover:bg-orange-100 hover-text-orange-700 dark-bg-orange-800 dark-border-orange-700 dark-text-orange-400 dark-hover-bg-orange-700 dark-hover-text-white"
          >
            <span class="sr-only">Previous</span>
            <svg class="w-2.5 h-2.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 6 10">
              <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 1 1 5l4 4"/>
            </svg>
          </button>
        </li>
        <li v-for="page in pages" :key="page">
          <button
            @click="goToPage(page)"
            :class="[buttonClass, { 'text-blue-600': page === currentPage, 'active-button': page === currentPage }]"
            class="flex items-center justify-center px-3 h-8 leading-tight text-orange-500 bg-white border border-orange-300 hover:bg-orange-100 hover-text-orange-700 dark-bg-orange-800 dark-border-orange-700 dark-text-orange-400 dark-hover-bg-orange-700 dark-hover-text-white"
          >
            {{ page }}
          </button>
        </li>
        <li>
          <button
            @click="goToPage(nextPage)"
            :disabled="nextPage === null"
            class="flex items-center justify-center px-3 h-8 leading-tight text-orange-500 bg-white border border-orange-300 hover:bg-orange-100 hover-text-orange-700 dark-bg-orange-800 dark-border-orange-700 dark-text-orange-400 dark-hover-bg-orange-700 dark-hover-text-white"
          >
            <span class="sr-only">Next</span>
            <svg class="w-2.5 h-2.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 6 10">
              <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 9 4-4-4-4"/>
            </svg>
          </button>
        </li>
      </ul>
    </nav>
  </template>
  
  <script>
  export default {
    props: {
      currentPage: Number,
      totalPages: Number,
    },
    computed: {
      prevPage() {
        return this.currentPage > 1 ? this.currentPage - 1 : null;
      },
      nextPage() {
        return this.currentPage < this.totalPages ? this.currentPage + 1 : null;
      },
      pages() {
        const pages = [];
        for (let i = 1; i <= this.totalPages; i++) {
          pages.push(i);
        }
        return pages;
      },
    },
    methods: {
      goToPage(page) {
        if (page !== null) {
          this.$emit("page-change", page);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .active-button {
    background-color: orange; /* Цвет для активной кнопки */
    color: white; /* Цвет текста для активной кнопки */
  }
  </style>