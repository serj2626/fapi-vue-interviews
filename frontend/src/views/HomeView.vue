<script setup>

</script>

<template>
  <div class="col-md-10 mx-auto">
    <h1 class="text-center title">Список собеседований</h1>
    <table class="table my-5 shadow-lg">
      <thead>
        <tr>
          <th scope="col">Актуальность</th>
          <th scope="col">Вакансия</th>
          <th scope="col">Компания</th>
          <th scope="col">Контакт</th>
          <th scope="col">Статус</th>
          <th scope="col">Дата создания</th>
          <th scope="col">Дата обновления</th>
          <th scope="col">Действие</th>
        </tr>
      </thead>
      <tbody>
        <tr class="shadow-lg">
          <td>Открыта</td>
          <td>Python Developer</td>
          <td>AMD</td>
          <td>@nastya@mail.ru</td>
          <td>
            <div class="btn-group dropend">
              <button type="button" class="btn btn-success btn-sm dropdown-toggle" data-bs-toggle="dropdown"
                aria-expanded="false">
                Тестовое задание
              </button>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item bg-white" href="#">Без отклика</a></li>
                <li><a class="dropdown-item bg-white" href="#">Звонок</a></li>
                <li><a class="dropdown-item bg-white" href="#">Тестовое задание</a></li>
                <li><a class="dropdown-item bg-white" href="#">Отказ</a></li>
                <li><a class="dropdown-item bg-white" href="#">Оффер</a></li>
              </ul>
            </div>
          </td>
          <td>2024-06-15</td>
          <td>2024-06-26</td>
          <td>
            <div class="btn-group dropend">
              <button type="button" class="btn btn-sm btn-secondary dropdown-toggle" data-bs-toggle="dropdown"
                aria-expanded="false">
                Выбрать
              </button>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item bg-white" href="#">Удалить</a></li>
                <li><a class="dropdown-item bg-white" href="#">Редактировать</a></li>
                <li><a class="dropdown-item bg-white" href="#">Действие</a></li>
              </ul>
            </div>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</template>


<style scoped>
.title {
  color: blue;
}
</style>