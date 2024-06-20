<script setup>
import { RouterLink } from "vue-router";
</script>

<template>
  <div class="container d-flex justify-content-center pt-5">
    <img src="/icon.png" height="100" width="100" alt="">
  </div>

  <div class="container">
    <ul class="nav nav-pills mt-5 d-flex justify-content-center">
      <li class="nav-item">
        <RouterLink :to="{ name: 'home' }" class="nav-link ">Главная</RouterLink>
      </li>
      <li class="nav-item">
        <RouterLink :to="{ name: 'login' }" class="nav-link">Войти</RouterLink>
      </li>
      <li class="nav-item">
        <RouterLink :to="{ name: 'signup' }" class="nav-link">Регистрация</RouterLink>
      </li>
      <li class="nav-item">
        <a class="nav-link disabled" aria-disabled="true">Выйти</a>
      </li>
    </ul>
  </div>
</template>

<style scoped>
.nav-link {
  text-decoration: none;
  font-size: 18px;
  color: black;
}

.router-link-exact-active {
  padding: 10px 10px;
  border-radius: 15px;
  background-color: orange;
  color: white;
}
</style>
