FROM ubuntu

#add  software-properties-common for add-apt-repository
RUN apt-get install -y software-properties-common
RUN apt-add-repository multiverse
RUN apt-get update
RUN apt-get install -y sabnzbdplus unrar

EXPOSE 8080 9090

VOLUME ["/config", "/data/complete", "/data/incomplete"]

ENTRYPOINT ["/usr/bin/sabnzbdplus", \
						"--server", "0.0.0.0:8080", \
						"--https", "9090", \
						"--browser", "0", \
						"--config-file", "/config"]
