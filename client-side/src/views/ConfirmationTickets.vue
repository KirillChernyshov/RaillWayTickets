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
    </div>
</template>

<script>
export default {
    name: 'confirmation',
    data: () => ({
        identificator: '',
    }),
    methods: {
        search() {
            if (!this.identificator) return;

            let data = {};

            if (this.identificator.indexOf('@') == -1)
                data.ticket_id = this.identificator;
            else
                data.usr_email = parseInt(this.identificator);

            this.$store.dispatch('confirmationTickets/searchTickets', data);
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
