<template>
  <div>
    <link href='https://fonts.googleapis.com/css?family=Montserrat' rel='stylesheet' type='text/css'>

    <div>
      <h6>
        <b-link class="text-white" style="font-size: 14px;" @click="showModal('terms')">
          Technology Stack</b-link>
        <br>
        <b-link class="text-white" style="font-size: 14px;" @click="showModal('privacy')">About</b-link>
      </h6>
    </div>


    <div class="d-flex justify-content-center">
      <img src="../assets/logo-plum-and-orange.png" class="d-inline-block align-top py-3" alt="Matcha" width="300">      
    </div>
    <div class="d-flex justify-content-center">
      <h2>MATCHA</h2>    
    </div>
    <div fixed="bottom" class="d-md-none d-lg-none d-xl-none px-4 mt-5 pt-5 d-flex flex-column justify-content-center">
      <b-button to="/login" class="btn-block" pill>Login</b-button>
      <b-button to="/signup" class="btn-block" pill>Sign Up</b-button>
    </div>
    <div fixed="bottom" class="d-none d-md-flex d-lg-flex d-xl-flex px-4 mt-5 pt-5 flex-row justify-content-center">
      <b-button to="/login" style="width: 200px; margin-top: 100px" class="mx-2" pill>Login</b-button>
      <b-button to="/signup" style="width: 200px; margin-top: 100px" class="mx-2" pill>Sign Up</b-button>
    </div>

    <b-modal ref="terms" hide-footer title="Terms of Use">
      <div class="d-block text-center">
        <TermsOfUse/>
      </div>
    </b-modal>

    <b-modal ref="privacy" hide-footer title="Privacy Policy">
      <div class="d-block text-center">
        <PrivacyPolicy/>
      </div>
    </b-modal>
      <video autoplay loop id="video-background" muted>
        <source src="https://media-us-westslateappcom.s3.us-west-1.amazonaws.com/madcowfilms/production/clips/514ebae1-ebbb-4477-addd-d52a30cd28c1-1280x720.2500.webm" type="video/webm">
      </video>
  </div>
</template>

<script>
import TermsOfUse from '@/components/TermsOfUse.vue'
import PrivacyPolicy from '@/components/PrivacyPolicy.vue'

export default {
  name: 'home',
  components: {
    TermsOfUse,
    PrivacyPolicy
  },
  methods: {
    showModal(ref) {
      this.$refs[ref].show()
    }
  }
}
</script>

<style>
@import '../assets/styles/ViewStyles.css';
body {
  margin: 0;
  padding: 0;
  background: #333;
  background-attachment: fixed;
  background-size: cover;
}

#video-background {
  position: fixed;
  right: 0; 
  bottom: 0;
  min-width: 100%; 
  min-height: 100%;
  width: auto; 
  height: auto;
  z-index: -100;
}

h6 {
  position: absolute;
  bottom: 3%;
  left:5%;
  width: 94%;
  font-size: 7px;
  letter-spacing: 3px;
  color: #fff;
  font-family: Montserrat, sans-serif;
  text-align: left;
}

h2 {
  font-size: 42px;
  color: #fff;
  font-family: Montserrat, sans-serif;
  text-align: left;
}
</style>
