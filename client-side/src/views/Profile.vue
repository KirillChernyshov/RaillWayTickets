<template lang="html">
    <div class="profile">
        <div>
            <b-avatar variant="primary" :text="avatar" size="100px"></b-avatar>
            <div class="info">
                <div class="name">{{ firstname}} {{ lastname }}</div>
                <div>{{ dRole }}</div>
            </div>
        </div>
        <b-table v-if="tickets.length" sticky-header class="align-left" striped hover :items="tickets" :fields="fields">
            <template v-slot:cell(actions)="row">
                <b-button size="sm" @click="cancelReservation(row.item.ticket_id)" class="mr-2">
                  Отменить бронирование
                </b-button>
            </template>
        </b-table>
        <div v-else>Здесь будет отображаться список Ваших билетов</div>
    </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
    name: "profile",
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
                key: "actions",
                label: "Действия"
            }
        ],
    }),
    computed: {
        ...mapState({
            firstname: state => state.user.local.firstname,
            lastname: state => state.user.local.lastname,
            role: state => state.user.local.role,
            tickets: state => state.user.tickets,
        }),
        avatar() {
            return this.firstname[0] + this.lastname[0];
        },
        dRole() {
            let roles = {
                client: "пользователь"
            }

            return roles[this.role];
        }
    },
    methods: {
        cancelReservation(id) {
            this.$store.dispatch('user/cancelTicketReservation', id);
        }
    },
    created() {

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
    }
</style>
