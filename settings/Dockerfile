FROM ubuntu

RUN apt-get install -y python
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD first_setup.py /

VOLUME ["/config", "/data/complete", "/tv", "/movies"]

ENTRYPOINT ["python", "/first_setup.py"]
