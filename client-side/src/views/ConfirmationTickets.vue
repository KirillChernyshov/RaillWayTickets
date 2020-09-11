<template lang="html">
    <div class="tickets">
        <b-form class="search" inline>
            <b-form-group
                label="Станция отбытия"
            >
                <b-form-input
                    v-model="identificator"
                    class="mb-2 mr-sm-2 mb-sm-0"
                ></b-form-input>
            </b-form-group>

            <b-button class="btn" @click="search()">Поиск</b-button>
        </b-form>

        <b-table v-if="tickets.length" sticky-header class="align-left" striped hover :items="tickets" :fields="fields">
            <template v-slot:cell(actions)="row">
                <b-button v-if="row.item.is_booked" size="sm" variant="info" @click="confirmReservation(row.item.ticket_id)" class="mr-2">
                &#10004;
                </b-button>
                <b-button size="sm" @click="cancelReservation(row.item.ticket_id)" class="mr-2">
                &#10008;
                </b-button>
            </template>
        </b-table>
    </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
    name: 'confirmation',
    data: () => ({
        identificator: '',
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
            // {
            //     key: "is_booked",
            //     label: "Статус"
            // },
            {
                key: "actions",
                label: "Действия",
            }
        ],
    }),
    computed: {
        ...mapState({
            tickets: state => state.confirmationTickets.tickets
        })
    },
    methods: {
        search() {
            if (!this.identificator) return;

            let data = {};

            if (this.identificator.indexOf('@') == -1)
                data.ticket_id = parseInt(this.identificator);
            else
                data.usr_email = this.identificator;

            this.$store.dispatch('confirmationTickets/searchTickets', data);
        },
        cancelReservation(id) {
            this.$store.dispatch('confirmationTickets/cancelReservation', id)
                .then(() => {
                    this.search();
                });
        },
        confirmReservation(id) {
            this.$store.dispatch('confirmationTickets/confirmReservation', id)
                .then(() => {
                    this.search();
                });
        }
    }
}
</script>

<style lang="css" scoped>
    .tickets {
        text-align: left;
    }

    .tickets .search {
        margin: 10px 30px;
    }

    .tickets .search .btn {
        margin: auto auto 0 0;
    }

    .tickets .routes {
        max-height: 70vh;
    }
</style>
