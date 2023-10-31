<script setup>
import AppHeader from './components/AppHeader.vue';
import AppFooter from './components/AppFooter.vue';
</script>

<template>
    <div class="max-w-full mx-auto">
<AppHeader />
<RouterView />
<AppFooter/>
</div>
</template>