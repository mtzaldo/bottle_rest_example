FROM python:3.8-slim-buster

WORKDIR /usr/src/

COPY ./docker/startup.sh .

COPY ./requirements.txt .

RUN apt-get update && \
    apt-get -y upgrade && \
    chmod +x ./startup.sh

ENV PYTHONUNBUFFERED=1

ENTRYPOINT [ "./startup.sh" ]