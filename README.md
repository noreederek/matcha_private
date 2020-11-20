# Matcha

TINDER-LIKE APP WITH REAL-TIME CHAT, NOTIFICATION SYSTEM, SMART SELECTION AND SEARCH FOR MATCHES

![matcha_mobile.png](https://github.com/noreederek/matcha_private/blob/master/matcha_mobile.png)

Functionality: 
* User Profile (Gender, Preferences, Pictures, Rating etc)
* Match Profiles (Same Geo, Max Common Tags, etc)
* Everything must be secured (CSRF, SQL, etc)
* Real-time chat, notifications
* Documented API and Interactive Map of Users (Admin)
* GPS Location

![Matcha-video1.gif](https://github.com/noreederek/matcha_private/blob/master/Matcha-video1.gif)

# Stack

Flask - Backend
* FlaskREST (Doc API)
* FlaskSocket, SocketIO
* Twisted
* Flask-JWT
* MySQL
* Autobahn (WAMP)
* Docker (Deploy)

VueJS - Frontend
* Bootstrap Vue
* Vue.Observable (instead of Vuex)
* Swiper
* Croppie
* Axios

todo - add docker-compose file
