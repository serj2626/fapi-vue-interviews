<script setup></script>

<template>
    <div>
        <h1 class="text-center">Авторизация</h1>
        <div class="col-md-4 mx-auto mt-5">
            <form>
                <div class="form-group mb-3">
                    <label for="username">Username</label>
                    <input type="text" id="username" name="username" class="form-control">
                </div>
                <div class="form-group">
                    <label for="password">Password</label>
                    <input type="password" id="password" name="password" class="form-control">
                </div>
                <button type="submit" class="btn btn-primary w-100 mt-3">Войти</button>
            </form>
        </div>
    </div>
</template>