<template lang="html">
    <div class="profile">
        <div>
            <b-avatar variant="primary" :text="avatar" size="100px"></b-avatar>
            <div class="info">
                <div class="name">{{ firstname}} {{ lastname }}</div>
                <div>{{ email }}</div>
                <div>{{ dRole }}</div>
            </div>
        </div>
        <b-table v-if="tickets.length" sticky-header class="align-left" striped hover :items="tickets" :fields="fields">
            <template v-slot:cell(actions)="row">
                <b-button v-if="row.item.is_booked" size="sm" @click="cancelReservation(row.item.ticket_id)" class="mr-2">
                &#10008;
                </b-button>
            </template>
        </b-table>
        <div v-if="role != 'manager' && !tickets.length">Здесь будет отображаться список Ваших билетов</div>
    </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
    name: "user-profile",
    data: () => ({
        fields: [
            {
                key: "ticket_id",
                label: "id",
            },
            {
                key: "dep_station_name",
                label: "Станция отбытия",
            },
            {
                key: "departure_time",
                label: "Время отбытия"
            },
            {
                key: "arr_station_name",
                label: "Станция прибытия"
            },
            {
                key: "arrival_time",
                label: "Время прибытия"
            },
            {
                key: "wagon_id",
                label: "Вагон"
            },
            {
                key: "place",
                label: "Место"
            },
            {
                key: "cost",
                label: "Цена"
            },
            {
                key: "is_booked",
                label: "Статус"
            },
            {
                key: "actions",
                label: "Отмена"
            }
        ],
    }),
    computed: {
        ...mapState({
            firstname: state => state.user.local.firstname,
            lastname: state => state.user.local.lastname,
            role: state => state.user.local.role,
            tickets: state => state.user.tickets,
            email: state => state.user.email,
        }),
        avatar() {
            return this.firstname[0] + this.lastname[0];
        },
        dRole() {
            let roles = {
                client: "пользователь",
                manager: "менеджер"
            }

            return roles[this.role];
        }
    },
    methods: {
        cancelReservation(id) {
            this.$store.dispatch('confirmationTickets/cancelReservation', id)
                .then(() => {
                    this.$store.dispatch('user/getUserTickets');
                })
            //this.$store.commit('user/setTickets', []);
        }
    },
    created() {
        this.$store.dispatch('user/getProfile');
        this.$store.dispatch('user/getUserTickets');
    }
}
</script>

<style lang="css" scoped>
    .profile>div {
        margin: 30px 50px;
        display: flex;
        text-align: left;
    }

    .profile .info>div {
        margin-left: 30px;
    }

    .profile .info .name {
        font-weight: 900;
        margin-top: 20px;
    }

    .align-left {
        text-align: left;
        max-height: 60vh;
        margin-left: 5px!important;
        margin-right: 5px!important;
    }
</style>
