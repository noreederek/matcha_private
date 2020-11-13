<template>
  <div v-if="!loggedIn">
    <b-navbar variant="light" class="shadow d-flex align-items-center justify-content-center my--4 px-lg-5" fixed="top">
      <b-navbar-brand href="/">
        <img src="../assets/logo-plum-and-orange.png" class="d-inline-block align-top" alt="Matcha" width="130">
      </b-navbar-brand>
    </b-navbar>
  </div>
  <div v-else>
  <div>
    <b-navbar variant="light" class="shadow d-flex align-items-center justify-content-between my--4 px-lg-5" fixed="top">
      <b-navbar-brand href="#">
        <img src="../assets/logo-plum-and-orange-right.png" class="d-inline-block align-top" alt="Matcha" width="130">
      </b-navbar-brand>
      <b-navbar-nav>
          <b-nav-item @click="logout"><b-icon icon="x-circle" class="mr-2 text-secondary" right></b-icon></b-nav-item>
          <b-nav-item v-if="isAdmin" to='/admin'><b-icon icon="shield-lock" class="mr-2 text-secondary" right></b-icon></b-nav-item>
      </b-navbar-nav>
    </b-navbar>
  </div>
  </div>
</template>

<script>
import {actions, state} from "@/store"

export default {
  data() {
    return {
      loggedIn: state.loggedIn,
      isAdmin: state.loggedIn && state.user.is_admin
    }
  },
  methods: {
    logout: function () {
      actions.logoutUser().then(() => this.$router.push("/login"))
    }
  },
}
</script>

<style scoped>
</style>