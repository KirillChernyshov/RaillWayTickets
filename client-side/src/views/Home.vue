<template>
    <div class="home">
        <div class="head">Добро пожаловать на платформу RaillWayTickets!</div>
        <div class="body">
            Данная платформа позволяет просматривать расписание маршрутов поездов.
            <br />
            Для бронирования мест необходимо <b-link>авторизоваться</b-link> или <b-link>зарегистрироваться</b-link>.
        </div>
    </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'home',
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
