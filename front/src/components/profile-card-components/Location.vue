<template>
  <div class="mb-4">
    <div class="d-flex flex-row flex-wrap justify-content-center my-2">
      <div v-if="locationName">
        {{ locationName }}
      <div class="small"><i><strong>{{user.distance}}</strong> km away</i></div>
      </div>
    </div>
  </div>
</template>

<script>

import {actions, state} from "@/store"

export default {
  props: ["user", "myprofile"],
  data() {
    return {
      permissionCheck: false,
      showLocation: false,
      locationName: '',
      loading: false,
      pos: null
    }
  },
  methods: {
    getLocation: async function () {
      this.locationName = await actions.location.name(this.pos)
    },
  },
  mounted: async function () {
    this.pos = {lat: this.user.latitude, long: this.user.longitude}
    this.getLocation()
  }
}
</script>