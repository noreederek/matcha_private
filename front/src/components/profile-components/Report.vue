<template>
  <div>
    <b-link style="text-decoration: underline" class="text-secondary" @click="showModal('report')">Block User</b-link>

    <b-modal ref="report" style="font-family: Montserrat" title="Block User" @ok="report">
      <div class="text-center my-3" style="font-family: Montserrat">
        Reporting on user will send a request to admin for review<br>
        The admin may choose to block the reported user
      </div>
      <div class="d-flex flex-column justify-content-center align-items-center text-center">
        <b-form-select
          class="ml-2 col-5 col-8"
          v-model="reason"
          :options="reasons"
        ></b-form-select>
        <b-form-group
          label="Provide Reason:"
          label-for="input-1"
          v-if="reason === 'other'"
          class="w-75 my-3 mb-2"
        >
          <b-form-textarea id="input-1" v-model="reason_text" class="my-3"></b-form-textarea>
        </b-form-group>
        <b-form-group
          label="Please Describe:"
          label-for="input-1"
          v-if="reason === 'harassment'"
          class="w-75 my-3 mb-2"
        >
          <b-form-textarea id="input-1" v-model="reason_text" class="my-3"></b-form-textarea>
        </b-form-group>
      </div>
    </b-modal>
  </div>
</template>

<script>
import {actions} from '@/store'

export default {
  props: ["user"],
  data() {
    return {
      reasons: [
        { value: null, text: 'Why are you reporting this user?' },
        { value: "fake profile", text: "Fake Profile." },
        { value: "inappropriate content", text: "Porn in Profile." },
        { value: "harassment", text: "Sends Me Dickpics." },
        { value: "too sexy", text: "Too Sexy." },
        { value: "other", text: "Other" }
      ],
      reason: null,
      reason_text: null,
      block_request: {
        reported_id: this.user.id,
        reason: null
      }
    }
  },
  methods: {
    report: function () {
      if (this.reason != 'other' && this.reason != 'harassment') {
        this.block_request.reason = this.reason
      } else {
        this.block_request.reason = this.reason + ": " + this.reason_text
      }

      if (this.reason) {        
        this.$http.post(`${this.$api}/block-requests`, this.block_request)
        .then(res => {
          actions.notify.info("You have successfully reported " + this.user.username + ". An admin will review your report.")
        })
        .catch(err => {
          actions.notify.error("Could not report " + this.user.username + ".")
        })
      }
    },

    showModal(ref) {
      this.$refs[ref].show()
    }
  }
}
</script>