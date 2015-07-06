FROM ubuntu

#enable multiverse for unrar
RUN sed -i 's/^#\s*\(deb.*multiverse\)$/\1/g' /etc/apt/sources.list
#add  software-properties-common for add-apt-repository
RUN apt-get install -y software-properties-common
#ppa:jcfp/ppa contains sabnzbdplus
RUN add-apt-repository ppa:jcfp/ppa
RUN apt-get update
#c.f. http://forums.sabnzbd.org/index.php?topic=387.0
RUN apt-get -o APT::Install-Recommends=1 install -y sabnzbdplus unrar

EXPOSE 8080 9090

VOLUME ["/config", "/data/complete", "/data/incomplete"]

ENTRYPOINT ["/usr/bin/sabnzbdplus", \
						"--server", "0.0.0.0:8080", \
						"--https", "9090", \
						"--browser", "0", \
						"--config-file", "/config"]
