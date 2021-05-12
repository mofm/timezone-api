# pull official base image
FROM python:3.9.5-slim-buster

LABEL maintainer="emre.eryilmaz@piesso.com"
LABEL version="0.1"
LABEL description="Timezone-api wit Flask and \
TimezoneFinderL"

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_ENV=development
ENV FLASK_APP=app.py

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app/

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]