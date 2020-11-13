<template>
  <div>
    <router-link :to="`/profile/${this.user.username}`">
      <b-form-rating class="bg-transparent mb-2" style="border: none" v-if="this.user" v-model="this.user.heat" readonly size="lg" color="#f7b0be"></b-form-rating>
    </router-link>
  </div>
</template>

<script>
export default {
  props: ["user"],
}
</script>