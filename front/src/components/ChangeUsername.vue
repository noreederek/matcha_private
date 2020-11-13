<template>
  <div class="h-100 d-flex flex-column justify-content-center align-items-center my-5">
    <form @submit.prevent="changeUsername">
      <div>
        <b-input-group>
          <b-form-input v-model="user.username" placeholder="New username here..." required></b-form-input>

          <b-input-group-append>
            <b-button variant="outline-secondary" type="submit">Submit</b-button>
          </b-input-group-append>
        </b-input-group>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  props: ["user"],
  methods: {
    changeUsername: function () {
      this.$emit("sync")
    },
  },
  mounted: function () {
    this.user_id = this.$store.user.id
  }
}
</script>

<style>

</style>