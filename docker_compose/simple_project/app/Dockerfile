FROM python:3.10

RUN apt-get update && apt-get install -y gettext && rm -rf /var/lib/apt/lists/*

SHELL ["/bin/bash", "-c"]

WORKDIR /opt/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV UWSGI_PROCESSES 1
ENV UWSGI_THREADS 16
ENV UWSGI_HARAKIRI 240
ENV DJANGO_SETTINGS_MODULE 'example.settings'

COPY run_uwsgi.sh run_uwsgi.sh
COPY requirements.txt requirements.txt
COPY uwsgi/uwsgi.ini uwsgi.ini
COPY example/manage.py manage.py


RUN  mkdir -p /opt/app/static/ \
     && mkdir -p /opt/app/media/ \
     && pip install --upgrade pip \
     && pip install -r requirements.txt \
     && apt-get update \
     && apt-get install -y gettext  \
     && rm -rf /var/lib/apt/lists/* \
     && apt-get install -y netcat

COPY . .

COPY ./run_uwsgi.sh .
RUN chmod +x /code/run_uwsgi.sh

EXPOSE 8000

ENTRYPOINT ["run_uwsgi.sh"]
