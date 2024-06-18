<script setup>
import { RouterView } from 'vue-router'
import Header from './components/Header.vue'
</script>

<template>
  <Header />

  <div class="container-fluid my-5">
    <div class="row">
      <RouterView />
    </div>
  </div>

</template>

<style scoped></style>
