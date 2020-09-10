<template lang="html">
    <b-modal id="book_ticket" title="Бронирование билета"
        @hidden="hideBookTicket"
    >
        <div v-for="(item, key) in dataList" :key="key">
            <span>{{ item.header }}:</span> {{ item.value }}
        </div>
        <div>
            <span>Цена:</span> 121
        </div>
        <b-row>
            <b-col sm="2">
                <span>Место:</span>
            </b-col>
            <b-col sm="4">
                <b-select size="sm" ></b-select>
            </b-col>
        </b-row>
        <b-form>

        </b-form>
    </b-modal>
</template>

<script>
import { mapState, mapMutations } from 'vuex'

export default {
    name: "BookTicket",
    computed: {
        ...mapState({
            firstname: state => state.user.local.firstname,
            lastname: state => state.user.local.lastname,
            show: state => state.bookTicket.show,
            bookData: state => state.bookTicket.data,
        }),
        dataList() {
            return {
                name: {
                    header: 'Имя',
                    value: `${this.firstname} ${this.lastname}`,
                },
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
        }
    },
    methods: {
        ...mapMutations('bookTicket', [
            'hideBookTicket',
        ]),
    },
    watch: {
        show(val) {
            if (val) {
                this.$bvModal.show('book_ticket');
                console.log(this.bookData);
                this.$store.dispatch('bookTicket/getRouteInfo', {

                });
            }
            else
                this.$bvModal.hide('book_ticket');
        }
    }
}
</script>

<style lang="css" scoped>
    span {
        font-weight: bold;
    }
</style>
