Running sabnzbd, sickbeard and couchpotato in containers.

All servers are hidden behind haproxy.

Settings are preconfigured so Sickbeard and Couchpotato can post process downloads.

To get started:
1. clone the repo ```git clone https://github.com/sbrants/nzbsuite.git```
1. __add your certificate__ in _reverseproxy/cert.pem_ so you can use https. You can get one for free from http://startssl.com.
1. edit _docker-compose.yml_ to map the _/tv_ and _/movies_ volumes of the _settings_ image to local folders.
1. bring the services up ```docker-compose up -d```
1. Connect with https to the reverse proxy.
