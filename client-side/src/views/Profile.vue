<template lang="html">
    <div class="profile">
        <b-avatar variant="primary" :text="avatar" size="100px"></b-avatar>
        <div class="info">
            <div class="name">{{ firstname}} {{ lastname }}</div>
            <div>{{ dRole }}</div>
        </div>
    </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
    name: "profile",
    computed: {
        ...mapState({
            firstname: state => state.user.local.firstname,
            lastname: state => state.user.local.lastname,
            role: state => state.user.local.role,
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
    created() {
        this.$store.dispatch('user/getUserTickets');
    }
}
</script>

<style lang="css" scoped>
    .profile {
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
</style>
