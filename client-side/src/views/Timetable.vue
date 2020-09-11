<template lang="html">
    <div class="timetable">
        <b-form class="search" inline>
            <b-form-group
                label="Станция отбытия"
            >
                <b-form-select
                    v-model="dep_station_name"
                    :options="cities"
                    class="mb-2 mr-sm-2 mb-sm-0"
                ></b-form-select>
            </b-form-group>

            <b-form-group
                label="Станция прибытия"
            >
                <b-form-select
                    v-model="arr_station_name"
                    :options="cities"
                    class="mb-2 mr-sm-2 mb-sm-0"
                ></b-form-select>
            </b-form-group>
            <b-form-group
                label="Дата прибытия"
            >
                <b-form-datepicker
                    v-model="date"
                    class="mb-2 mr-sm-2 mb-sm-0"
                ></b-form-datepicker>
            </b-form-group>
            <b-form-group
                label="Время прибытия"
            >
                <b-form-timepicker
                    v-model="time"
                    class="mb-2 mr-sm-2 mb-sm-0"
                ></b-form-timepicker>
            </b-form-group>
            <b-button class="btn" @click="search()">Поиск</b-button>
        </b-form>

        <b-table :busy="load" sticky-header class="align-left routes" striped hover :items="routes" :fields="fields">
            <template v-show="false" v-slot:cell(actions)="row">
                <b-button
                    v-if="role == 'client'"
                    size="sm"
                    variant="info"
                    @click="showBookTicket(row.item)"
                    class="mr-2"
                >
                  Бронировать билет
                </b-button>
                <b-button
                    v-if="role == 'manager'"
                    size="sm"
                    variant="info"
                    @click="showIssueTicket(row.item)"
                    class="mr-2"
                >
                 Оформить билет
                </b-button>
            </template>
            <template v-slot:table-busy>
                <div class="text-center text-info my-2">
                    <b-spinner class="align-middle"></b-spinner>
                    <strong> Загрузка...</strong>
                </div>
            </template>
        </b-table>

        <BookTicket v-bind="bookTicket" @search="search"/>
        <IssueTicket v-bind="bookTicket" @search="search"/>
    </div>
</template>

<script>
import { mapState, mapMutations } from 'vuex'
import moment from 'moment'
import BookTicket from '../components/BookTicket.vue'
import IssueTicket from '../components/IssueTicket.vue'

export default {
    name: "timetable",
    data: () => ({
        arr_station_name: null,
        dep_station_name: null,
        date: moment().add(1, 'day').format('YYYY-MM-DD'),
        time: moment().format('HH:mm:ss'),
        bookTicket: {
        },
    }),
    computed: {
        ...mapState({
            cities: state => state.timetable.cities,
            load: state => state.timetable.load,
            routes: state => state.timetable.routes,
            role: state => state.user.local.role,
        }),
        rDate() {
            return moment(this.date).add(this.time).format();
        },
        fields() {
            return [
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
                    key: "route_name",
                    label: "Маршрут"
                },
                {
                    key: "places",
                    label: "Места"
                },
                (this.role) ? {
                    key: "actions",
                    label: "Действия"
                } : {}
            ];
        }
    },
    methods: {
        search() {
            this.$store.dispatch('timetable/searchRoutes', {
                arrival_date: this.rDate,
                arrival_province_name: this.arr_station_name,
                departure_province_name: this.dep_station_name,
            });
        },
        ...mapMutations('bookTicket', [
            'showBookTicket',
            'showIssueTicket'
        ])
        // showBookTicket(data) {
        //     this.$store.commit('bookTicket/showBookTicket', data);
        // }
    },
    watch: {
        cities(val) {
            if (val.length < 2) return;

            this.arr_station_name = val[0];
            this.dep_station_name = val[1];
        },
    },
    components: {
        BookTicket,
        IssueTicket,
    },
    created() {
        this.$store.dispatch('timetable/getCitiesList');
    }
}
</script>

<style lang="css" scoped>
    .timetable {
        text-align: left;

    }

    .timetable .search {
        margin: 10px 30px;
    }

    .timetable .search .btn {
        margin: auto auto 0 0;
    }

    .timetable .routes {
        max-height: 70vh;
    }

</style>
