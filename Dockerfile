FROM ubuntu:latest

ENV LANG=C.UTF-8 DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/London

COPY ./apcupsdStuff/ /tmp

RUN echo Starting. \
# && cp /etc/apt/sources.list /etc/apt/sources.list.default \
# && mv /usr/local/bin/sources.list.localrepo /etc/apt/sources.list \
 && apt-get -q -y update \
 && apt-get -q -y install --no-install-recommends apcupsd dbus libapparmor1 libdbus-1-3 libexpat1 \
 && apt-get -q -y install python3 python3-pip \
 && pip3 install paho-mqtt \
 && apt-get -q -y full-upgrade \
 && rm -rif /var/lib/apt/lists/* \
 && mv /tmp/apcupsd      /etc/default/apcupsd \
 && mv /tmp/apcupsd.conf /etc/apcupsd/apcupsd.conf \
 && mv /tmp/hosts.conf   /etc/apcupsd/hosts.conf \
 && mv /tmp/doshutdown      /etc/apcupsd/doshutdown \
###  Revert to default repositories  ###
# && mv /etc/apt/sources.list.default /etc/apt/sources.list \
 && echo Finished.

#copy the app source 
COPY ./src/ /usr/local/bin

WORKDIR /usr/local/bin
RUN chmod +x startup.sh

#run the startup script
CMD ["./startup.sh"]
