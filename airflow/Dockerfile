FROM puckel/docker-airflow

USER root:root

RUN mkdir -p /usr/share/man/man1 && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
    freetds-dev \
    freetds-bin \
    unixodbc-dev \
    tdsodbc \
    unixodbc \
    gnupg \
    openjdk-11-jdk

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql17 

ENV POSTGRES_HOST "postgres"
ENV POSTGRES_PORT "5432"
ENV POSTGRES_USER "airflow"
ENV POSTGRES_PASSWORD "airflow"
ENV POSTGRES_DB "airflow"

ENV EXECUTOR "LocalExecutor"

# COPY ./files/dags /usr/local/airflow/dags
# COPY ./files/requirements.txt ./