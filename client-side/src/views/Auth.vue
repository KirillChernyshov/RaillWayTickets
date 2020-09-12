<template lang="html">
    <div class="form">
        <b-form
            @submit="checkValid"
        >
            <b-form-group
                v-for="item in form"
                :key="item.label"
                :label="item.label"
            >
                <b-form-input
                    v-model="item.value"
                    :placeholder="item.placeholder"
                    :state="item.valid"
                    :type="item.type"
                    size="sm"
                    @focus="item.valid = null"
                >
                </b-form-input>
            </b-form-group>
            <b-button type="submit" variant="primary" size="sm">Войти</b-button>
            <span>
                или <b-link href="/reg">зарегистрироваться</b-link>
            </span>
            <b-spinner v-if="waiting"
                class="spiner"
                variant="success" small type="grow" label="Spinning"
            >
            </b-spinner>
            <div class="error">{{ error }}</div>
        </b-form>
    </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
    name: "authorization",
    data: () => ({
        form: {
            email: {
                label: "Эл. почта:",
                placeholder: "Введите адрес эл. почты",
                value: "",
                type: "email",
                valid: null,
            },
            password: {
                label: "Пароль:",
                placeholder: "Введите пароль",
                value: "",
                type: "password",
                valid: null,
            },
        },
    }),
    computed: {
        ...mapState({
            waiting: state => state.auth.waiting,
            error: state => state.auth.error,
        })
    },
    methods: {
        checkValid(e) {
            e.preventDefault();

            let data = {};

            for (let key of Object.keys(this.form)) {
                data[key] = this.form[key].value
            }

            this.$store.dispatch("auth/authorization", data)
                .then(() => {
                    window.ym(67271437,'reachGoal','login');
                    console.log("loged");
                });
        },
    }
}
</script>

<style lang="css" scoped>
    .form {
        border: 1px solid #ccc;
        border-radius: .5vh;
        box-sizing: border-box;
        margin: auto;
        max-width: 50vh;
        padding: 2vh;
        text-align: left;
    }

    .spiner {
        margin-left: 1vh;
    }

    .error {
        margin-top: 1vh;
        color: red;
        font-size: 1.4vh;
    }
</style>
