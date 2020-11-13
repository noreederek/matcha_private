<template>
  <div>
    <div class="header"><Header /></div>
    <div class="content">
      <div class="mb-2">
        <router-link class="text-secondary" :to="`/profile/${$route.params.username}`">
        Receiver Profile
        </router-link>
      </div>
      <div class="max-w-90 d-flex justify-content-center">
        <b-col sm="auto" md="6" lg="4" class="rounded-lg shadow bg-light">
          <div class="message-container">
            <br>
            <template v-for="m in messages">

              <div :key="m.index" v-if="m.from_id == state.user.id" class="sent">
                <h5 class="hour">{{ m.timestamp }}</h5>
                <p class="sent-bubble">{{ m.message }}</p>
              </div>
              <div v-else :key="m.index" class="received">
                <h5 class="hour">{{ m.timestamp }}</h5>
                <p class="received-bubble">{{ m.message }}</p>
              </div>
            </template>
          </div>
          <div class="input-container">
            <input
              v-model="message" ref="message" type="text"
              placeholder="Enter your message"
            >
            <a @click="sendMessage()" class="btnsend">Send</a>
          </div>
        </b-col>
      </div>
    </div>

    <div class="footer"><NavBar/></div>
  </div>
</template>

<script>

import NavBar from '@/components/NavBar.vue'
import Header from '@/components/HeaderNav.vue'

// import {action, state} from '@/store'

import {actions, state, socket} from "@/store"

export default {
  components: { NavBar, Header },
  data: function () {
    return {
      message: null,
      state: state
    }
  },
  computed: {
    messages: function () {
      return state.messages
    }
  },
  watch: {
    messages: function (newVal, oldVal) {
      setTimeout(() => {
        this.$nextTick(() => this.$refs.message.scrollIntoView())
    }, 5);
    }
  },
  methods: {
    sendMessage: function () {
      socket.call.sendMessageTo(state.messaging_user, this.message)
      socket.refreshMessages()
    }
  },
  created: function () {
    socket.call.initiateChat(this.$route.params.username)
  },
  beforeDestroy: function () {
    socket.call.closeChat()
  }
}
</script>

<style>

:root {
  --background-color: #a5bfd4;
  --send-color: #c3dbfa;
  --received-color: #a8a8a8;
  --light-gray: #dfdfdf;
  --dark-gray: #858a91;
}

.btnsend {
  opacity: 0.7;
}

.btnsend:hover {
  opacity: 1;
}
.message-container h3 {
  color: var(--light-gray);
  border-bottom: 1px solid var(--light-gray);
  text-align: center;
  line-height: 0.1rem;
  margin: 10px 0 30px;
  text-transform: uppercase;
  font-size: 1rem;
}

.message-container h3 span {
  padding: 0 15px;
  background-color: #fff;
}

.message-container div.sent {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.message-container div:not(.sent) {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
}

.message-container div:last-child {
  border-bottom: 1px solid var(--light-gray);
}

.message-container .hour {
  color: var(--dark-gray);
  font-size: 10px;
}

.message-container p {
  position: relative;
}

/* BUBBLE ARROW SENT */
.sent p:before {
  content: "";
  position: absolute;
  top: 0;
  left: -6px;
  width: 0px;
  height: 0px;
  border-top: 0px solid transparent;
  border-bottom: 20px solid transparent;
  border-right: 10px solid var(--send-color);
}

/* BUBBLE ARROW RECEIVED */
.received p:before {
  content: "";
  position: absolute;
  top: 0;
  right: -6px;
  width: 0px;
  height: 0px;
  border-top: 0px solid transparent;
  border-bottom: 20px solid transparent;
  border-left: 10px solid var(--received-color);
}

.sent-bubble {
  background-color: var(--send-color);
}

.received-bubble {
  background-color: var(--received-color);
}

.blocked-bubble {
  background-color: var(--blocked-color);
}

.sent-bubble,
.received-bubble,
.blocked-bubble {
  max-width: 70%;
  padding: 10px;
  margin: 10px 0 20px;
  text-align: left;
}

.sent-bubble {
  border-bottom-left-radius: 3px;
  border-bottom-right-radius: 3px;
  border-top-right-radius: 3px;
}

.received-bubble {
  border-bottom-left-radius: 3px;
  border-bottom-right-radius: 3px;
  border-top-left-radius: 3px;
}

.blocked-bubble {
  border-radius: 3px;
}

.input-container {
  background-color: transparent;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 25px;
}

.input-container input {
  background-color: transparent;
  width: 100%;
  outline: none;
  border: none;
  font-size: 1rem;
}

.input-container a {
  text-decoration: none;
  cursor: pointer;
  font-weight: bold;
  letter-spacing: 1px;
  text-transform: uppercase;
  margin-left: 20px;
}

</style>