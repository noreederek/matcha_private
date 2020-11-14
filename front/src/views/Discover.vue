<template>
  <div class="discover">
    <div class="header">
      <Header/>
    </div>
    <div class="content">
      <div v-if="loading">
        <div class="mt-5 d-flex flex-column justify-content-center align-items-center">
          <b-spinner style="width: 5rem; height: 5rem;" type="grow" class="mt-5" variant="primary"></b-spinner>
          <div class="text-centered text-primary mt-4">Search your match...</div>
        </div>
      </div>
      <div v-else>
        <div class="d-flex flex-column align-items-center justify-content-center flex-md-row ml-md-4 my-2">

          <b-button-group text="Sort" block right class="my-2 col-md-3">
            <b-button @click="ageClick" :pressed.sync="age">
              Age
              <b-icon-arrow-up v-if="age && ageOrder === 'ascending'"></b-icon-arrow-up>
              <b-icon-arrow-down v-if="age && ageOrder === 'descending'"></b-icon-arrow-down>
            </b-button>
            <b-button @click="distanceClick" :pressed.sync="distance">
              Distance
              <b-icon-arrow-up v-if="distance && distanceOrder === 'ascending'"></b-icon-arrow-up>
              <b-icon-arrow-down v-if="distance && distanceOrder === 'descending'"></b-icon-arrow-down>
            </b-button>
            <b-button @click="heatClick" :pressed.sync="heat">
              Heat
              <b-icon-arrow-up v-if="heat && heatOrder === 'ascending'"></b-icon-arrow-up>
              <b-icon-arrow-down v-if="heat && heatOrder === 'descending'"></b-icon-arrow-down>
            </b-button>
            <b-button @click="tagsClick" :pressed.sync="tags">
              Tags
              <b-icon-arrow-up v-if="tags && tagsOrder === 'ascending'"></b-icon-arrow-up>
              <b-icon-arrow-down v-if="tags && tagsOrder === 'descending'"></b-icon-arrow-down>
            </b-button>
          </b-button-group>

        </div>
        <div class="d-flex flex-column flex-md-row justify-content-center align-items-center flex-wrap">
          <ProfileCard v-for="a in users" :key="a.index" :user="a"/>
        </div>
        <div v-if="!users.length > 0" class="d-flex justify-content-center">
          <b-card class="col-md-6">Seems you'll have to keep swimming alone for a bit.<br>Check back soon for new recommendations.</b-card>
        </div>
      </div>
    </div>
    <div class="footer">
      <NavBar/>
    </div>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import Header from '@/components/HeaderNav.vue'
import ProfileCard from '@/components/ProfileCardRachel.vue'

import {actions, state} from "@/store"
import axios from "axios"

export default {
  name: 'discover',
  components: {
    Header,
    ProfileCard,
    NavBar
  },
  data() {
    return {
      loading: true,
      filterAge: false,
      minAge: 20,
      maxAge: 40,
      filterDistance: false,
      minDistance: 0,
      maxDistance: 20,
      filterHeat: false,
      minHeat: 1,
      maxHeat: 5,
      filterTags: false,
      minTags: 3,
      maxTags: 10,
      age: false,
      ageOrder: "descending",
      distance: true,
      distanceOrder: "ascending",
      heat: false,
      heatOrder: "descending",
      tags: false,
      tagsOrder: "descending",
      object: [],
      users: []
    }
  },
  computed: {
    profiles() {
      var temp = this.object;
      var minAge = this.minAge;
      var maxAge = this.maxAge;
      if (this.filterAge === true) {
        temp = temp.filter(function(n) {
          var date = new Date(n.dob);
          var diff_ms = Date.now() - date;
          var age_dt = new Date(diff_ms);
          var age = Math.abs(age_dt.getUTCFullYear() - 1970);
          return age >= minAge && age <= maxAge;
        });
      }
      var minDistance = this.minDistance;
      var maxDistance = this.maxDistance;
      if (this.filterDistance === true) {
        temp = temp.filter(function(n) {
          return n.distance >= minDistance && n.distance <= maxDistance;
        });
      }
      var minHeat = this.minHeat;
      var maxHeat = this.maxHeat;
      if (this.filterHeat === true) {
        temp = temp.filter(function(n) {
          return n.heat >= minHeat && n.heat <= maxHeat;
        });
      }
      var minTags = this.minTags;
      var maxTags = this.maxTags;
      if (this.filterTags === true) {
        temp = temp.filter(function(n) {
          return n.tags >= minTags && n.tags <= maxTags;
        });
      }
      return temp;
    }
  },
  methods: { 
    ageCalculation(dob) {
        if (dob) {
        var split_dob = dob.split("-");
        var year = split_dob[0];
        var month = split_dob[1];
        var day = split_dob[2];
        var dob_asdate = new Date(year, month, day);
        var today = new Date();
        var mili_dif = Math.abs(today.getTime() - dob_asdate.getTime());
        var age = mili_dif / (1000 * 3600 * 24 * 365.25);
        age = Math.floor(age);
      }
      return age;
    },
    checkSmaller(input, otherInput) {
      return input <= otherInput;
    },
    filterAgeClick() {},
    filterDistanceClick() {},
    filterHeatClick() {},
    filterTagsClick() {},
    distanceClick() {
      this.distance = true;
      this.age = false;
      this.ageOrder = "descending";
      this.heat = false;
      this.heatOrder = "descending";
      this.tags = false;
      this.tagsOrder = "descending";
      if (this.distanceOrder === "ascending") {
        this.distanceOrder = "descending";
      } else {
        this.distanceOrder = "ascending";
      }
      if (this.distanceOrder === "ascending") {
        this.users.sort((a, b) => parseFloat(a.distance) - parseFloat(b.distance));
      } else {
        this.users.sort((a, b) => parseFloat(b.distance) - parseFloat(a.distance));
      }
    },
    ageClick() {
      this.age = true;
      this.distance = false;
      this.distanceOrder = "descending";
      this.heat = false;
      this.heatOrder = "descending";
      this.tags = false;
      this.tagsOrder = "descending";
      if (this.ageOrder === "ascending") {
        this.ageOrder = "descending";
      } else {
        this.ageOrder = "ascending";
      }
      if (this.ageOrder === "ascending") {
        this.users.sort((a, b) => parseFloat(b.dob) - parseFloat(a.dob));
      } else {
        this.users.sort((a, b) => parseFloat(a.dob) - parseFloat(b.dob));
      }
    },
    heatClick() {
      this.heat = true;
      this.age = false;
      this.ageOrder = "descending";
      this.distance = false;
      this.distanceOrder = "descending";
      this.tags = false;
      this.tagsOrder = "descending";
      if (this.heatOrder === "ascending") {
        this.heatOrder = "descending";
      } else {
        this.heatOrder = "ascending";
      }
      if (this.heatOrder === "ascending") {
        this.users.sort((a, b) => parseFloat(a.heat) - parseFloat(b.heat));
      } else {
        this.users.sort((a, b) => parseFloat(b.heat) - parseFloat(a.heat));
      }
    },
    tagsClick() {
      this.tags = true;
      this.age = false;
      this.ageOrder = "descending";
      this.distance = false;
      this.distanceOrder = "descending";
      this.heat = false;
      this.heatOrder = "descending";
      if (this.tagsOrder === "ascending") {
        this.tagsOrder = "descending";
      } else {
        this.tagsOrder = "ascending";
      }
      if (this.tagsOrder === "ascending") {
        this.users.sort((a, b) => parseFloat(a.tags) - parseFloat(b.tags));
      } else {
        this.users.sort((a, b) => parseFloat(b.tags) - parseFloat(a.tags));
      }
    }
  },
  mounted: function () {
    axios.get(`${actions.api}/discover?skip=0&take=20&distance=20`)
    .then(resp => {
      this.object = resp.data,
      this.users = resp.data
      this.loading = false
    })
  }
}
</script>

<style>
@import '../assets/styles/ViewStyles.css';
</style>
