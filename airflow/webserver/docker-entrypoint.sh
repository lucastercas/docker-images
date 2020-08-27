#!/bin/bash

function check_db_connection() {
  # Check if database is open for connection
  echo "==> Check if database connection on $DB_HOST:$DB_PORT is open"
  until nc -z -v -w30 "$DB_HOST" "$DB_PORT"; do
    echo "--> Wait for database connection for 5 seconds... :("
    sleep 5
  done
  echo "--> Database on $DB_HOST:$DB_PORT is open for connection :)"
}

check_db_connection

export AIRFLOW__CORE__SQL_ALCHEMY_CONN="postgres+psycopg2://${DB_USER}:${DB_PASSWORD}@${DB_HOST}:${DB_PORT}/${DB_NAME}"
echo "==> Start Airflow Database"
echo "--> Airflow SQL Alchemy Connection: ${AIRFLOW__CORE__SQL_ALCHEMY_CONN}"
airflow initdb

echo "==> Start Airflow Webserver"
airflow webserver