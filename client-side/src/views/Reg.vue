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
            <b-button type="submit" variant="primary" size="sm">Регистрация</b-button>
            <span>
                или <b-link href="/auth">авторизоваться</b-link>
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
    name: "registration",
    data: () => ({
        form: {
            firstname: {
                label: "Имя:",
                placeholder: "Введите имя",
                value: "",
                type: "text",
                valid: null,
            },
            lastname: {
                label: "Фамилия:",
                placeholder: "Введите фамилию",
                value: "",
                type: "text",
                valid: null,
            },
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
            checkpass: {
                label: "Повт. пароль:",
                placeholder: "Повторите пароль",
                value: "",
                type: "password",
                valid: null,
            },
        },
    }),
    computed: {
        ...mapState({
            waiting: state => state.reg.waiting,
            error: state => state.reg.error,
        })
    },
    methods: {
        validation() {
            let count = 0;

            for (let key of Object.keys(this.form)) {

                let item = this.form[key];

                if (item.value < 3) {
                    item.valid = false;
                    count++;
                }
                else {
                    //item.valid = null;
                }

                if (key == "checkpass") continue;
                if (key == "password") {
                    if (item.value != this.form["checkpass"].value) {
                        item.valid = false;
                        this.form["checkpass"].valid = false;
                        count++;
                    } else {
                        item.valid = null;
                        this.form["checkpass"].valid = null;
                    }
                }

            }

            return count;
        },
        checkValid(e) {
            e.preventDefault();

            if (this.validation() || this.waiting) return;

            let data = {};

            for (let key of Object.keys(this.form)) {
                data[key] = this.form[key].value
            }

            this.$store.dispatch("reg/registration", data);
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
