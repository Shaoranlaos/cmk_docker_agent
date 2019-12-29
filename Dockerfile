FROM python:2-alpine

LABEL maintainer="shaoranlaos@shaoranlaos.de"

RUN apk add --no-cache bash
RUN pip install docker

COPY mk_docker.py /usr/lib/check_mk_agent/plugins/mk_docker.py
COPY docker.cfg /etc/check_mk/docker.cfg
COPY check_mk_agent.linux /usr/bin/check_mk_agent
COPY socket.py /usr/bin/socketServer
COPY start.sh /usr/bin/start

RUN chmod +x /usr/bin/socketServer

EXPOSE 6556

CMD socketServer

