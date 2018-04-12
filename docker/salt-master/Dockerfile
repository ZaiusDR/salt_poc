FROM ubuntu:16.04
MAINTAINER Eduardo Suarez <eduardosuarez@gmail.com>

RUN apt-get update && apt-get install -y curl

RUN curl -L https://bootstrap.saltstack.com | bash

RUN apt-get update && apt-get install -y salt-master

VOLUME /etc/salt /srv

EXPOSE 4505 4506

CMD salt-master
