<template>
  <div>
    <b-container class="mt-4 pr-lg-5">
      <b-row align-h="center">
        <b-col sm="auto" lg="6">
          <b-form @submit.prevent="onSubmit" v-if="show">
            <b-form-group
              id="input-group-1"
              label="Email Address:"
              label-for="input-1"
              label-cols-md="4"
              label-align-md="right"
              label-align="left"
            >
              <b-form-input
                id="input-1"
                v-model="form.email"
                type="email"
                required
                placeholder="Enter email"
              ></b-form-input>
            </b-form-group>

            <b-form-group 
              id="input-group-2" 
              label="Username:" 
              label-for="input-2"
              label-cols-md="4"
              label-align-md="right"
              label-align="left">
              <b-form-input
                id="input-2"
                v-model="form.username"
                required
                placeholder="Enter username"
              ></b-form-input>
            </b-form-group>

            <b-form-group 
              id="input-group-3" 
              label="First Name:" 
              label-for="input-3"
              label-cols-md="4"
              label-align-md="right"
              label-align="left">
              <b-form-input
                id="input-3"
                v-model="form.fname"
                required
                placeholder="Enter first name"
              ></b-form-input>
            </b-form-group>

            <b-form-group 
              id="input-group-4" 
              label="Last Name:" 
              label-for="input-4"
              label-cols-md="4"
              label-align-md="right"
              label-align="left">
              <b-form-input
                id="input-4"
                v-model="form.lname"
                required
                placeholder="Enter last name"
              ></b-form-input>
            </b-form-group>

            <b-form-group 
              id="input-group-5"
              label="Password:"
              label-for="input-5"
              label-cols-md="4"
              label-align-md="right"
              label-align="left">
              <b-form-input
                id="input-5"
                v-model="form.password"
                type="password"
                required
                placeholder="Enter password"
                @input="checkPassword"
              ></b-form-input>
              <p v-if="errors.length">
                <b>Please correct the following error(s):</b>
                <ul  class="list-unstyled">
                  <li v-for="error in errors" :key="error.index">{{ error }}</li>
                </ul>
              </p>
            </b-form-group>

            <b-form-group class="d-flex justify-content-center">
              <router-link class="ml-lg-4 small text-secondary display-8" to="/login">Already have an account? Login now.</router-link>
            </b-form-group>
            <b-button class="float-right d-none d-md-block d-lg-block d-xl-block" variant="primary" type="submit">Submit</b-button>
            <b-button class="btn-block d-md-none d-lg-none d-xl-none py-2" size="lg" variant="primary" type="submit">Submit</b-button>

          </b-form>
        </b-col>
      </b-row>

    </b-container>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        errors: [],
        form: {
          fname: '',
          lname: '',
          email: '',
          username: '',
          password: ''
        },
        show: true,
        disabled: true,
      }
    },
    methods: {

      checkPassword: function (e) {
      this.errors = [];

      let password = this.form.password

      if (this.form.password.length < 8) {
        this.errors.push("Password should be at least 8 characters. ");
      } else if (this.form.password.length > 32) {
        this.errors.push("Password should be at most 32 characters. ");
      }
      if (!(this.form.password.match(/[a-z]/))) {
        this.errors.push('Please include a LOWER case character.');
      }
      if (!(this.form.password.match(/[A-Z]/))) {
        this.errors.push('Please include an UPPER case character.');
      }
      if (!(this.form.password.match(/[0-9]/))) {
        this.errors.push('Please include a NUMERICAL character.');
      }
    },

    onSubmit: function (evt) {
      let self = this
      this.$http.post(`${this.$api}/users`, this.form)
        .then(res => {
          self.$bvToast.toast(res.data.username + ' created successfully', {
          title: "Success!",
          autoHideDelay: 2000,
          toaster: "b-toaster-top-center",
          variant: "success",
          noCloseButton: true,
          })
          setTimeout(() => {
            self.$router.push('/login')
          }, 1500);
        })
        .catch(err => {
          self.$bvToast.toast(err.response.data.message, {
          title: "Error!",
          autoHideDelay: 5000,
          variant: "danger"
          })
        })
    }
  }
  }
</script>