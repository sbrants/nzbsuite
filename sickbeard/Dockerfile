FROM ubuntu

#Need python-openssl for HTTPS
RUN apt-get install -y git python-cheetah python-openssl
RUN git clone git://github.com/midgetspy/Sick-Beard.git /sickbeard

EXPOSE 8081

VOLUME ["/config", "/tv", "/data/complete"]

ENTRYPOINT ["python", "/sickbeard/SickBeard.py", "--datadir", "/config"]
