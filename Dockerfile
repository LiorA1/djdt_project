# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED=True

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

RUN apt-get -y upgrade

#RUN apt-get install memcached
RUN pip install django-debug-toolbar
RUN pip install coverage
RUN pip install selenium

COPY . /code/

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000" ]