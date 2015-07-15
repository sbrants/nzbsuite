FROM ubuntu

#add  software-properties-common for add-apt-repository
RUN apt-get install -y software-properties-common
#Needed for unrar
RUN apt-add-repository multiverse
#This line is optional but that repo has a more recent version than multiverse
RUN apt-add-repository ppa:jcfp/ppa
RUN apt-get update
RUN apt-get install -y sabnzbdplus unrar
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 8080 9090

VOLUME ["/config", "/data/complete", "/data/incomplete"]

ENTRYPOINT ["/usr/bin/sabnzbdplus", \
						"--server", "0.0.0.0:8080", \
						"--https", "9090", \
						"--browser", "0", \
						"--config-file", "/config"]
