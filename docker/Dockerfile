FROM python:3.8-slim-buster

WORKDIR /usr/src/app

COPY ./requirements.txt .

RUN apt-get update && \
    apt-get -y upgrade && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

ENV PYTHONUNBUFFERED=1

CMD ["python", "./startup.py"]