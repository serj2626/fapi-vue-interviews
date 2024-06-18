<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>


<template>
<div class="container">
    <ul class="nav nav-pills mt-5 d-flex justify-content-center">
      <li class="nav-item">
        <RouterLink :to="{ name: 'home' }" class="nav-link active">Home</RouterLink>
      </li>
      <li class="nav-item">
        <RouterLink :to="{ name: 'login' }" class="nav-link">Login</RouterLink>
      </li>
      <li class="nav-item">
        <RouterLink :to="{ name: 'signup' }" class="nav-link">Signup</RouterLink>
      </li>
      <li class="nav-item">
        <a class="nav-link disabled" aria-disabled="true">Logout</a>
      </li>
    </ul>
  </div>
</template>