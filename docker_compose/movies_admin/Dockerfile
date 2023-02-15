FROM python:3.10

RUN apt-get update && apt-get install -y gettext && rm -rf /var/lib/apt/lists/*

SHELL ["/bin/bash", "-c"]

WORKDIR /opt/movies_admin

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV UWSGI_PROCESSES 1
ENV UWSGI_THREADS 16
ENV UWSGI_HARAKIRI 240
ENV DJANGO_SETTINGS_MODULE 'config.settings'

COPY run_uwsgi.sh run_uwsgi.sh
COPY requirements.txt requirements.txt
COPY uwsgi/uwsgi.ini uwsgi.ini
COPY manage.py manage.py


RUN  mkdir -p /opt/movies_admin/static/ \
     && mkdir -p /opt/movies_admin/media/ \
     && pip install --upgrade pip \
     && pip install -r requirements.txt

COPY . .


EXPOSE 8000

#ENTRYPOINT ["uwsgi", "--strict", "--ini", "uwsgi.ini"]
ENTRYPOINT['./run_uwsgi.sh']