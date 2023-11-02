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
 
 <style>
 .carousel__item {
    min-height: 200px;
    width: 100%;
    height: 600px; /* Добавьте эту строку */
   object-fit: cover; /* Добавьте эту строку */
    border-radius: 8px;
    display: flex;
    justify-content: center;
    align-items: center;
 }
 
 .carousel__slide {
    padding: 10px;
 }
 
 .carousel__prev,
 .carousel__next {
    box-sizing: content-box;
    border: 5px solid white;
 }
 </style>