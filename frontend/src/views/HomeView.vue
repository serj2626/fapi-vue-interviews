<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import InterviewForm from "@/components/InterviewForm.vue";
const msg = ref("");
const show = ref(false);

const getMessage = async () => {
  try {
    let res = await axios.get("/");
    console.log(res.data);
  } catch (err) {
    console.log(err);
  }
};

onMounted(getMessage);
</script>

<template>
  <div class="col-md-10 mx-auto">
    <div class="d-flex justify-content-center py-3 px-2 mb-5">
      <button
        @click="show = true"
        class="btn-select"
      >
        Вакансии
      </button>
      <button
        @click="show = false"
        class="btn-select"
      >
        Добавить
      </button>
    </div>
    <InterviewForm v-if="!show"/>
    <div v-else>
      <h1 class="text-center title">Список вакансий</h1>

      <table class="table my-5 shadow-lg">
        <thead>
          <tr>
            <th scope="col">Статус</th>
            <th scope="col">Вакансия</th>
            <th scope="col">Компания</th>
            <th scope="col">Контакт</th>
            <th scope="col">Отклики</th>
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
              <div class="btn-group">
                <button class="btn btn-warning btn-sm" type="button">
                  Без отклика
                </button>
                <button
                  type="button"
                  class="btn btn-sm btn-secondary dropdown-toggle dropdown-toggle-split"
                  data-bs-toggle="dropdown"
                  aria-expanded="false"
                >
                  <span class="visually-hidden">Toggle Dropdown</span>
                </button>
                <ul class="dropdown-menu">
                  <li>
                    <a class="dropdown-item bg-white" href="#">Без отклика</a>
                  </li>
                  <li><a class="dropdown-item bg-white" href="#">Звонок</a></li>
                  <li>
                    <a class="dropdown-item bg-white" href="#"
                      >Тестовое задание</a
                    >
                  </li>
                  <li><a class="dropdown-item bg-white" href="#">Отказ</a></li>
                  <li><a class="dropdown-item bg-white" href="#">Оффер</a></li>
                </ul>
              </div>
            </td>
            <td>2024-06-15</td>
            <td>2024-06-26</td>
            <td>
              <div class="btn-group dropend">
                <div class="btn-group">
                  <button class="btn btn-info btn-sm" type="button">
                    Выбрать
                  </button>
                  <button
                    type="button"
                    class="btn btn-sm btn-secondary dropdown-toggle dropdown-toggle-split"
                    data-bs-toggle="dropdown"
                    aria-expanded="false"
                  >
                    <span class="visually-hidden">Выбрать</span>
                  </button>
                  <ul class="dropdown-menu">
                    <li>
                      <a class="dropdown-item bg-white" href="#">Удалить</a>
                    </li>
                    <li>
                      <a class="dropdown-item bg-white" href="#"
                        >Редактировать</a
                      >
                    </li>
                    <li>
                      <a class="dropdown-item bg-white" href="#">Действие</a>
                    </li>
                  </ul>
                </div>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<style scoped>
.title {
  color: blue;
}

.btn-select{
  background: linear-gradient(to right, #453f2d 0%, #8026ee 100%);
  margin: 0 10px;
  padding: 10px 15px;
  color: yellow;
  border-radius: 12px;
  border: none;
  }
</style>
