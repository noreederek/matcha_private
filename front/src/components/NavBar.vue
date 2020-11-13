<template>
  <div v-if="!loggedIn">
  </div>
  <div v-else>
    <div>
      <b-navbar variant="light" type="gray" class="shadow d-flex align-items-center justify-content-center px-lg-5 py-lg-4 text-dark" fixed="bottom">
        <b-navbar-nav class="d-flex align-items-center justify-content-around justify-content-lg-center">
          <b-nav-item :to="{ name: 'profile', params: { username: username } }" :key="username" class="d-flex flex-column mx-2"><b-icon icon="person-fill"></b-icon></b-nav-item>
          <b-nav-item to="/discover" class="d-flex flex-column mx-2"><b-icon icon="layers"></b-icon></b-nav-item>
          <b-nav-item to="/search" class="d-flex flex-column mx-2"><b-icon icon="search"></b-icon></b-nav-item>
          <b-nav-item to="/matches" class="d-flex flex-column mx-2"><b-icon icon="heart-half"></b-icon></b-nav-item>
          <b-nav-item to='/stats' class="d-flex flex-column mx-2"><b-icon icon="bar-chart"></b-icon></b-nav-item>
          <b-nav-item to='/settings' class="d-flex flex-column mx-2"><b-icon icon="gear-wide"></b-icon></b-nav-item>
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
      username: state.user.username
    }
  },
}
</script>