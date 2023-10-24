<script setup>
import { ref, onMounted } from 'vue';
import InstituteCard from '../components/InstituteCard.vue';
const instituteList = ref([]);

onMounted(() => {
    fetch('http://127.0.0.1:8000/api/v1/institutes/')
    .then((response)=>response.json())
    .then(apiInstitutes => {
        instituteList.value = apiInstitutes
    })
})
</script>


<template>
    <h1>Список институтов</h1>
    <InstituteCard v-for="institute in instituteList" :key="institute.id" :institute="institute"/>
  </template>

