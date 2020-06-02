FROM python:3.8-slim
LABEL 'Maintainer'='oscargomez87'

ENV PYTHONUNBUFFERED 1
ENV DOCKERIZE_VERSION v0.6.1

COPY ./requirements.txt /requirements.txt
COPY ./app /app

ADD https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz .

RUN tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz; \
    pip install -r requirements.txt

WORKDIR /app

RUN adduser --disabled-password app
USER app
