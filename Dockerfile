FROM python:3.8.5-slim

RUN apt-get update; \
    apt-get install -y gettext mime-support build-essential

WORKDIR /web

COPY requirements.txt /requirements.txt

RUN pip install -r /requirements.txt;

CMD ["uwsgi", "uwsgi.ini"]