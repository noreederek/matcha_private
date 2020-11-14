<template>
  <div v-if="relationship" class="mb-3 p-md-2">
    <Report class="small mt-1 mb-3" :user="user"/>
    <div v-if="relationship.matched && relationship.liked">
      <b-card class="border-none shadow-sm rounded text-dark" >
        This user <span class="text-secondary"><strong>ALSO MATCH</strong></span> you<br><hr>
        <b-link>Go to chat</b-link><hr>
        <Rate :user="user" /><hr>
        <b-icon class="text-danger" icon="hand-thumbs-down"></b-icon><b-link @click="unmatch" class="text-danger"> UNMATCH</b-link>
      </b-card>
    </div>
    <div v-else-if="!relationship.matched && relationship.liked">
      <b-card class="border-none shadow-sm rounded text-dark" >
        Wait until this user also <span class="text-secondary" style="font-weight: 700px"><strong>MATCH</strong></span> you<br>OR<br><hr>
        <b-icon class="text-danger" icon="hand-thumbs-down"></b-icon><b-link @click="unmatch" class="text-danger"> UNLIKE</b-link>
      </b-card>
    </div>
    <div v-else-if="!relationship.matched && !relationship.liked">
      <b-card class="border-none shadow-sm rounded text-dark" >
        Wanna <span class="text-secondary"><strong>CHAT</strong></span> this user?<br><hr>
        <b-icon class="text-primary" icon="heart"></b-icon><b-link @click="likeUser" class=""> MATCH</b-link>
      </b-card>
    </div>
    <div v-else>
      Could not determine relationship. Please refresh.
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import {actions, state} from '@/store'
import Report from '@/components/profile-components/Report'
import Rate from '@/components/profile-components/Rate'

export default {
  props: ["user"],
  components: {
    Report,
    Rate
  },
  data() {
    return {
      relationship: null
    }
  },
  methods: {
    likeUser: function () {
      axios.post(`${this.$api}/matches`, {"matchee_id" : this.user.id})
      .then(res => {
        actions.notify.info(res.data.message)
        this.checkMatch()
      })
      .catch(err => {
        if (err.response.data.no_photo) {
          actions.notify.error(err.response.data.message)
        } else {
          actions.notify.error(err.response.data.message)
        }
      })
    },

    unmatch: function () {
      axios.delete(`${this.$api}/unmatch/${this.user.id}`)
      .then(res => {
        actions.notify.warning("User relationship removed. You will no longer see this user on the site.")
        setTimeout(() => {
          this.$router.go(-1)
        }, 1500)
      })
      .catch(err => {
        actions.notify.error("Could not remove user relationship. Please contact an admin. " + err)
      })
    },

    checkMatch: function () {
      axios.get(`${this.$api}/match/${this.user.id}`)
      .then(res => {
        this.relationship = res.data
      })
      .catch(err => {
        actions.notify.error("There was a problem loading some data. Notice of this error has been sent to admins.")
      })
    }
  },
  created: function () {
    this.checkMatch()
  }
}
</script>