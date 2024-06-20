<script setup>
import axios from "axios";
import { reactive } from "vue";
import { useToast } from "vue-toast-notification";

const toast = useToast();


const form = reactive({
  
  username: "",
  email: "",
  password: "",
});

const submitForm = async () => {
  try {
    const res = await axios.post("/api/users/register", { ...form });
    toast.success("Аккаунт успешно создан");
    let UserForm = new FormData();
    console.log(UserForm);
    form.email = "";
    form.username = "";
    form.password = "";
    console.log(res);
    toast.success("Аккаунт успешно создан");
  } catch {
    toast.error("Ошибка при создании аккаунта");
  }
};
</script>

<template>
  <div>
    <h1 class="text-center">Регистрация</h1>
    <div class="col-md-4 mx-auto mt-5">
      <form @submit.prevent="submitForm" method="post">
        <div class="form-group">
          <label for="username">Имя пользователя</label>
          <input
            v-model="form.username"
            type="text"
            id="username"
            name="username"
            class="form-control"
            placeholder="Ваше имя"
          />
        </div>
        <div class="form-group my-3">
          <label for="username">Почта</label>
          <input
            v-model="form.email"
            type="email"
            id="email"
            name="email"
            class="form-control"
            placeholder="Ваша почта"
          />
        </div>
        <div class="form-group">
          <label for="password">Пароль</label>
          <input
            v-model="form.password"
            type="password"
            id="password"
            name="password"
            class="form-control"
            placeholder="Придумайте пароль"
          />
        </div>
        <button type="submit" class="btn btn-primary w-100 mt-4">
          Зарегестрироваться
        </button>
      </form>
    </div>
  </div>
</template>
