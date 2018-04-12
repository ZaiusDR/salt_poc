FROM ubuntu:16.04
MAINTAINER Eduardo Suarez <eduardosuarez@gmail.com>

RUN apt-get update && apt-get install -y curl

RUN curl -L https://bootstrap.saltstack.com | bash

RUN apt-get update && apt-get install -y salt-minion

VOLUME /etc/salt/

CMD salt-minion
