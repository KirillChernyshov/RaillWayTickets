<template lang="html">
    <div class="timetable">
        <b-form class="search" inline>
            <b-form-group
                label="Станция отбытия"
            >
                <b-form-select
                    v-model="arr_station_name"
                    :options="cities"
                    class="mb-2 mr-sm-2 mb-sm-0"
                ></b-form-select>
            </b-form-group>

            <b-form-group
                label="Станция прибытия"
            >
                <b-form-select
                    v-model="dep_station_name"
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
        <div>{{ cities }}</div>
    </div>
</template>

<script>
import { mapState } from 'vuex'
import moment from 'moment'

export default {
    name: "timetable",
    data: () => ({
        arr_station_name: null,
        dep_station_name: null,
        date: moment().add(1, 'day').format('YYYY-MM-DD'),
        time: moment().format('hh:mm:ss'),
    }),
    computed: {
        ...mapState({
            cities: state => state.timetable.cities,
        }),
        rDate() {
            return moment(this.date).add(this.time).format();
        }
    },
    methods: {
        search() {
            this.$store.dispatch('timetable/searchRoutes', {
                arrival_date: this.rDate,
                arrival_province_name: this.arr_station_name,
                departure_province_name: this.dep_station_name,
            });
        }
    },
    watch: {
        cities(val) {
            if (val.length < 2) return;

            this.arr_station_name = val[0];
            this.dep_station_name = val[1];
        },
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

</style>
