<template>
    <div class="home">
        <div v-if="valid" class="head">Здравствуйте, {{ name }}!</div>
        <div class="head">Добро пожаловать на платформу RaillWayTickets!</div>
        <div class="body">
            Данная платформа позволяет просматривать расписание маршрутов поездов.
            <br />
            Для бронирования мест
            <span v-if="!valid">
                необходимо
                <b-link href="/auth">авторизоваться</b-link>
                или
                <b-link href="/reg">зарегистрироваться</b-link>.
            </span>
            <span v-else>
                перейдите на вкладку с
                <b-link href="/reg">расписанием</b-link>.
            </span>
        </div>
    </div>
</template>

<script>
// @ is an alias to /src
import { mapGetters } from 'vuex'

export default {
    name: 'home',
    computed: {
        ...mapGetters('user', [
            'valid',
            'name'
        ]),
    },
    components: {

    }
}
</script>

<style scoped>
    .home {
        margin-top: 20vh;
        padding-bottom: 20vh;
    }

    .home .head {
        font-size: 4vh;
        font-weight: 500;
    }

    .home .body {
        font-size: 2vh;
        padding: 4vh;
    }

</style>
