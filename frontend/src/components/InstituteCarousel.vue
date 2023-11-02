<template>
    <Carousel>
        <Slide v-for="photo in photos" :key="photo">
            <img class="carousel__item" :src="photo.photo" alt="photo">
        </Slide>
  
        <template #addons>
            <Navigation />
            <Pagination />
        </template>
    </Carousel>
 </template>
 
 <script>
 import { defineComponent } from 'vue'
 import { Carousel, Navigation, Pagination, Slide } from 'vue3-carousel'
 
 import 'vue3-carousel/dist/carousel.css'
 
 export default defineComponent({
    name: 'Basic',
    components: {
        Carousel,
        Slide,
        Pagination,
        Navigation,
    },
    props: {
        photos: Array,
    },
 })
 </script>
 
 <style scoped>
 .carousel__item {
   min-height: 200px;
   width: 100%;
   max-height: 600px; /* Установите максимальную высоту */
   max-width: 100%; /* Установите максимальную ширину */
   object-fit: contain; /* Сохраняет соотношение сторон и уменьшает изображение */
   border-radius: 8px;
   display: flex;
   justify-content: center;
   align-items: center;
 }
 
 .carousel__slide {
   padding: 10px;
 }
 
 .carousel-navigation,
 .carousel-pagination {
   display: flex;
   justify-content: center;
   align-items: center;
 }
 
 .carousel-navigation button,
 .carousel-pagination button {
   background-color: var(--vc-clr-primary);
   color: var(--vc-clr-white);
   border: none;
   border-radius: 100%; /* Создает круглую кнопку */
   width: 100px;
   height: 100px;
   font-size: 20px;
   margin: 0 5px;
   cursor: pointer;
 }
 
 .carousel-navigation button:hover,
 .carousel-pagination button:hover {
   background-color: var(--vc-clr-secondary); /* Изменяет цвет при наведении */
 }
 
 .carousel__prev {
   margin-right: 10px;
 }
 
 .carousel__next {
   margin-left: 10px;
 }
 </style>