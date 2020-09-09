<template lang="html">
    <!-- <div> -->
        <b-navbar toggleable="lg" type="dark" variant="info" fixed="top">
            <b-navbar-brand href="/">RWT</b-navbar-brand>

            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

            <b-collapse id="nav-collapse" is-nav>
                <b-navbar-nav>
                    <b-nav-item href="/timetable">Расписание</b-nav-item>
                    <!-- <b-nav-item href="#" disabled>Disabled</b-nav-item> -->
                </b-navbar-nav>

<!-- Right aligned nav items -->
                <b-navbar-nav class="ml-auto">

                    <b-nav-item v-if="!valid" href="/auth">Log In</b-nav-item>
                    <b-nav-item-dropdown v-else right>
                    <!-- Using 'button-content' slot -->
                        <template v-slot:button-content>
                            <em>{{ name }}</em>
                        </template>
                        <b-dropdown-item href="/profile">Profile</b-dropdown-item>
                        <b-dropdown-item @click="signOut" >Sign Out</b-dropdown-item>
                    </b-nav-item-dropdown>
                </b-navbar-nav>
            </b-collapse>
        </b-navbar>
    <!-- </div> -->
</template>

<script>
import { mapGetters, mapMutations } from 'vuex'

export default {
    name: "nav-bar",
    computed: {
        ...mapGetters('user', [
            'valid',
            'name',
        ])
    },
    methods: {
        ...mapMutations('user', [
            'clearUserData',
        ]),
        signOut() {
            this.$router.push('/');
            this.clearUserData();
        }
    }
}
</script>

<style lang="css" scoped>
</style>
