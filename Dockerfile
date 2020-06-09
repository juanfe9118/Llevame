FROM python:3.8-slim
LABEL 'Maintainer'='oscargomez87'

ENV PYTHONUNBUFFERED 1
ENV DOCKERIZE_VERSION v0.6.1

COPY ./requirements.txt /requirements.txt

ADD https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz .

RUN adduser --gecos "" --disabled-password app \
    && apt-get update && apt-get install git git-flow -y \
    && pip install -r requirements.txt; \
    tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && cd /home/app && git clone https://github.com/juanfe9118/Llevame.git \
	&& chown app:app -R /home/app/Llevame

USER app

WORKDIR /home/app/Llevame
