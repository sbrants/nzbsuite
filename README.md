Running sabnzbd, sonarr and couchpotato in containers.

All servers are hidden behind haproxy.

Settings are preconfigured so Sickbeard and Couchpotato can post process downloads.
There is ddclient running for people having DDNS needs and ganglia to monitor the performance of your machine(s).

To get started:

1. clone the repo ```git clone https://github.com/sbrants/nzbsuite.git```
1. __add your certificate__ in _reverseproxy/cert.pem_ so you can use https. You can get one for free from http://startssl.com.
1. edit gmetad.conf and replace _docker_ with the name of your host or its IP address. Copy that file to the folder where you store your ganglia settings.
1. edit _docker-compose.yml_ to map the volumes to local folders anywhere there is an _EDIT_HERE_ tag.
1. bring the services up with ```./start```. It will not recreate the containers that already exist.
1. Connect with https to the reverse proxy.

Things to know:

1. Plex
 - The volume you map for configuration need to allow for symlink and locking sqlite3. I had trouble mounting over a Samba share. I solved the issue by using a local folder on the host for the settings and used a shared folder on the network to store the database backups (scheduled tasks in Plex server configuration).
1. Ganglia
 - I Couldn't make Ganglia work the way I wanted (deaf gmond on the docker host and mute gmond + gmetad in the container). That's why there's the ugly need to tell the container the IP/hostname of the host until I can figure it out.
1. Reverse proxy
 - If you delete one of the container that is accessible (linked) via the reverse proxy you also need to delete the reverse proxy container, otherwise the link will not be recreated.
