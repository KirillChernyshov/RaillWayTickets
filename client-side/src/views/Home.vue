<template>
    <div class="home">
        <div v-if="valid" class="head">Здравствуйте, {{ name }}!</div>
        <div class="head">Добро пожаловать на платформу RaillWayTickets!</div>
        <div class="body">
            Данная платформа позволяет просматривать расписание маршрутов поездов.
            <br />
            <span v-if="!valid && role != 'manager'">Для бронирования мест</span>
            <span v-if="valid && role == 'manager'">Для оформления билетов</span>
            <span v-if="!valid">
                необходимо
                <b-link href="/auth">авторизоваться</b-link>
                или
                <b-link href="/reg">зарегистрироваться</b-link>.
            </span>
            <span v-else>
                перейдите на вкладку с
                <b-link href="/timetable">расписанием</b-link>.
            </span>
            <br />
            <span v-if="role == 'manager'">
                Для подтверждения билетов перейдите на вкладку
                <b-link href="/confirmation">подтверждения билетов</b-link>.
            </span>
        </div>
    </div>
</template>

<script>
// @ is an alias to /src
import { mapState, mapGetters } from 'vuex'

export default {
    name: 'home',
    computed: {
        ...mapState({
            role: state => state.user.local.role,
        }),
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
