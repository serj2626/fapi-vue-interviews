<script setup></script>

<template>
    <div class="col-md-10 mx-auto">
        <h1 class="text-center title pb-5">Добавить вакансию</h1>
        <form class="row g-3">
            <div class="col-md-6">
                <label for="inputVacancy" class="form-label">Вакансия</label>
                <input type="text" class="form-control" id="inputVacancy">
            </div>
            <div class="col-md-6">
                <label for="inputCompany" class="form-label">Компания</label>
                <input type="text" class="form-control" id="inputCompany">
            </div>
            <div class="col-6">
                <label for="inputStatus" class="form-label">Статус вакансии</label>
                <select id="inputStatus" class="form-select">
                    <option selected>Выбрать...</option>
                    <option>...</option>
                </select>
            </div>
            <div class="col-6">
                <label for="inputRes" class="form-label">Статус отклика</label>
                <select id="inputRes" class="form-select">
                    <option selected>Выбрать...</option>
                    <option>...</option>
                </select>
            </div>
            <div class="col-md-6">
                <label for="inputPContact" class="form-label">Контактное лицо</label>
                <input type="email" class="form-control" id="inputContact">
            </div>
                <button type="submit" class="btn btn-add py-2">Добавить</button>
        </form>
    </div>
</template>


<style scoped>

.btn-add{
    background:linear-gradient(to right, #e7c857 0%, #ff5900 100%);
    color: white;
    border: none;

    &:hover{
        background:linear-gradient(to right, #ffc907 0%, #ff772d 100%);
        
    }
}
</style>