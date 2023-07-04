#FROM ubuntu:latest
#LABEL authors="rahulprajapati"
#
#ENTRYPOINT ["top", "-b"]
FROM python:3.9.6-alpine
ARG workdir=/opt/app
ARG app=test_docker
RUN mkdir -p $workdir
ARG web=/opt/web
RUN mkdir -p $web/staticfiles
RUN mkdir -p $web/mediafiles

WORKDIR $workdir
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirement.txt .
RUN apk add --no-cache linux-headers g++
#RUN apk add libpq-dev
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
#RUN set -e; \
#	apk add --no-cache --virtual .build-deps \
#		gcc \
#		libc-dev \
#		linux-headers \
#	; \
#	pip install -r requirements.txt; \
#	apk del .build-deps;
# install dependency

RUN pip install --upgrade pip
RUN pip install -r requirement.txt


#COPY ./entrypoint.sh .
#RUN sed -i 's/\r$//g' $workdir/entrypoint.sh
#RUN chmod +x $workdir/entrypoint.sh

COPY . .
EXPOSE 8000
# run entrypoint.sh
#ENTRYPOINT ["$workdir/entrypoint.sh"]
RUN mkdir -p /var/www/dkr

#CMD ["uwsgi", "--ini", "/opt/app/test_docker/uwsgi.ini"]



