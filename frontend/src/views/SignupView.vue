<script setup></script>

<template>
    <div>
        <h1 class="text-center">Регистрация</h1>
        <div class="col-md-4 mx-auto mt-5">
            <form>
                <div class="form-group">
                    <label for="username">Имя пользователя</label>
                    <input type="text" id="username" name="username" class="form-control">
                </div>
                <div class="form-group my-3">
                    <label for="username">Почта</label>
                    <input type="email" id="email" name="email" class="form-control">
                </div>
                <div class="form-group">
                    <label for="password">Пароль</label>
                    <input type="password" id="password" name="password" class="form-control">
                </div>
                <button type="submit" class="btn btn-primary w-100 mt-3">Зарегестрироваться</button>
            </form>
        </div>
    </div>
</template>