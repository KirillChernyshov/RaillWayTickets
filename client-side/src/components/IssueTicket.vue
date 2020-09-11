<template lang="html">
    <b-modal id="book_ticket" title="Оформление билета"
        @hidden="hideIssueTicket"
        ok-only
        @ok="issueTicket"
    >
        <b-row>
            <b-col sm="2">
                <span>Имя:</span>
            </b-col>
            <b-col sm="8">
                <b-input size="sm" v-model="firstname" ></b-input>
            </b-col>
        </b-row>
        <b-row>
            <b-col sm="2">
                <span>Фамилия:</span>
            </b-col>
            <b-col sm="8">
                <b-input size="sm" v-model="lastname" ></b-input>
            </b-col>
        </b-row>
        <div v-for="(item, key) in dataList" :key="key">
            <span>{{ item.header }}:</span> {{ item.value }}
        </div>
        <div>
            <span>Цена:</span> {{ seat.cost }}
        </div>
        <b-row>
            <b-col sm="2">
                <span>Место:</span>
            </b-col>
            <b-col sm="8">
                <b-select size="sm" v-model="seat" :options="seats" ></b-select>
            </b-col>
        </b-row>
    </b-modal>
</template>

<script>
import { mapState, mapMutations } from 'vuex'

export default {
    name: "BookTicket",
    data: () => ({
        seat: {},
        firstname: '',
        lastname: '',
    }),
    computed: {
        ...mapState({
            show: state => state.bookTicket.showIssue,
            bookData: state => state.bookTicket.data,
            wagon_seats_info: state => state.bookTicket.wagon_seats_info,
        }),
        dataList() {
            return {
                // name: {
                //     header: 'Имя',
                //     value: `${this.firstname} ${this.lastname}`,
                // },
                route: {
                    header: 'Маршрут',
                    value: this.bookData.route_name,
                },
                trainNum: {
                    header: 'Номер поезда',
                    value: this.bookData.schedule_id,
                },
                dep: {
                    header: 'Станция и время отбытия',
                    value: `${this.bookData.dep_station_name} / ${this.bookData.departure_time}`,
                },
                arr: {
                    header: 'Станция и время прибытия',
                    value: `${this.bookData.arr_station_name} / ${this.bookData.arrival_time}`,
                },
                // price: {
                //     header: 'Стоимость',
                //     value: `${this.bookData.price}`,
                // },
            }
        },
        seats() {
            if (this.wagon_seats_info)
                if (!this.wagon_seats_info.length) return [];

            let seats = [];

            this.wagon_seats_info.forEach((wagon) => {
                wagon.empty_places.forEach((seat) => {
                    seats.push({
                        value: {
                            cost: wagon.cost,
                            wagon_id: wagon.wagon_num,
                            place: seat,
                        },
                        text: `Вагон: ${wagon.wagon_num} | Место: ${seat} | Тип: ${wagon.type_name}`,
                    });
                });

            });

            return seats;
        }
    },
    methods: {
        ...mapMutations('bookTicket', [
            'hideIssueTicket',
        ]),
        issueTicket() {
            this.$store.dispatch('bookTicket/issueTicket', {
                cost: this.seat.cost,
                place: this.seat.place,
                wagon_id: this.seat.wagon_id,
                schedule_id: this.bookData.schedule_id,
                arrival_stop_id: this.bookData.arr_stop_id,
                departure_stop_id: this.bookData.dep_stop_id,
            });

            this.$emit('search');
        }
    },
    watch: {
        show(val) {
            if (val) {
                this.$bvModal.show('book_ticket');
                // console.log(this.bookData);
                this.$store.dispatch('bookTicket/getRouteInfo', {
                    arr_stop_id: this.bookData.arr_stop_id,
                    dep_stop_id: this.bookData.dep_stop_id,
                    schedule_id: this.bookData.schedule_id,
                });
            }
            else
                this.$bvModal.hide('book_ticket');
        },
        seats(val) {
            if (val.length)
                this.seat = val[0].value;
        },
    }
}
</script>

<style lang="css" scoped>
    span {
        font-weight: bold;
    }
</style>
