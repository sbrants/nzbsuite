FROM python:2

RUN apt-get install -y git-core
RUN git clone https://github.com/RuudBurger/CouchPotatoServer.git /CouchPotatoServer

EXPOSE 5050

VOLUME ["/config", "/movies", "/data/complete"]

ENTRYPOINT ["python", "/CouchPotatoServer/CouchPotato.py", "--data_dir", "/config"]
