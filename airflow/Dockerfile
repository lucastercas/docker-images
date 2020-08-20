FROM puckel/docker-airflow

ARG POSTGRES_HOST="postgres"
ARG POSTGRES_PORT=5432
ARG POSTGRES_USER="airflow"
ARG POSTGRES_PASSWORD
ARG POSTGRES_DB="airflow"

COPY ./files/dags /usr/local/airflow/dags
COPY ./files/requirements.txt ./