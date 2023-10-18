<template>
  <div>
    <h1>List of Institutes</h1>
    <div class="card-container">
      <div v-for="institute in institutes" :key="institute.id" class="card">
        <img :src="institute.logo" class="card-image" />
        <div class="card-info">
          <h2>{{ institute.name }}</h2>
          <p>{{ institute.abbreviation }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      institutes: []
    };
  },
  mounted() {
    axios.get('http://localhost:8000/api/v1/institutes/')
      .then(response => {
        this.institutes = response.data;
      })
      .catch(error => {
        console.error('Failed to fetch institutes:', error);
      });
  }
};
</script>

<style>
.card-container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.card {
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 10px;
  width: 300px;
  background-color: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.card-image {
  max-width: 100%;
  height: auto;
}

.card-info {
  text-align: center;
}

h2 {
  font-size: 20px;
  margin: 10px 0;
}

p {
  font-size: 14px;
}
</style>