FROM python:3.7-buster

RUN apt-get update && \
  apt-get install -y \
  netcat \
  build-essential \
  gcc \
  libsasl2-dev \
  libssl-dev

RUN pip install apache-airflow[crypto,celery,postgres,hive,jdbc,mysql,ssh]

EXPOSE 8080

WORKDIR /usr/app/airflow
COPY docker-entrypoint.sh .

ENTRYPOINT [ "./docker-entrypoint.sh" ]