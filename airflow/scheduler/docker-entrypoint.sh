#!/bin/bash

export AIRFLOW__CORE__SQL_ALCHEMY_CONN="postgres+psycopg2://${DB_USER}:${DB_PASSWORD}@${DB_HOST}:${DB_PORT}/${DB_NAME}"
echo "==> Start Airflow Database"
echo "--> Airflow SQL Alchemy Connection: ${AIRFLOW__CORE__SQL_ALCHEMY_CONN}"
airflow initdb

echo "==> Start Airflow Scheduler"
airflow scheduler