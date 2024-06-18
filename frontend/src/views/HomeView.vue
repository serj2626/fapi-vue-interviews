<script setup>

</script>

<template>
  <div class="spinner-border text-primary" role="status">
    <span class="visually-hidden">Загрузка...</span>
  </div>

  <h1 class="text-center title">Список собеседований</h1>
  <table class="table my-5">
    <thead>
      <tr>
        <th scope="col">Актуальность</th>
        <th scope="col">Вакансия</th>
        <th scope="col">Компания</th>
        <th scope="col">Контакт</th>
        <th scope="col">Статус</th>
        <th scope="col">Дата создания</th>
        <th scope="col">Дата обновления</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Открыта</td>
        <td>Python Developer</td>
        <td>AMD</td>
        <td>@nastya@mail.ru</td>
        <td>Тестовое задание</td>
        <td>2024-06-15</td>
        <td>2024-06-26</td>
      </tr>
    </tbody>
  </table>
</template>


<style scoped>

.title{
  color: blue;
}
</style>