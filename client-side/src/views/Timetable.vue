<template lang="html">
    <div class="timetable">
        <b-form class="search" inline>
            <b-form-group
                label="Станция отбытия"
            >
                <b-input
                    class="mb-2 mr-sm-2 mb-sm-0"
                ></b-input>
            </b-form-group>

            <b-form-group
                label="Станция прибытия"
            >
                <b-input
                    class="mb-2 mr-sm-2 mb-sm-0"
                ></b-input>
            </b-form-group>
        </b-form>
        <div>{{ cities }}</div>
    </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
    name: "timetable",
    computed: {
        ...mapState({
            cities: state => state.timetable.cities,
        })
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

</style>
