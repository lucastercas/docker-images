FROM jenkins/jenkins:2.245

USER root

# Install dependencies packages
RUN apt-get -y update && \
  apt-get -y --no-install-recommends install \
  make \
  maven \
  sshpass \
  python3-pip \
  python3-setuptools

# Install docker client
RUN curl -fsSL https://get.docker.com -o get-docker.sh && \
  chmod a+x get-docker.sh && \
  ./get-docker.sh

# Install python modules
RUN pip3 install \
  docker \
  ansible

# Install jenkins plugins
RUN /usr/local/bin/install-plugins.sh \
  gitlab-plugin \
  sonar

ARG DOCKER_HOST
ENV DOCKER_HOST ${DOCKER_HOST}
ARG DOCKER_CERT_PATH
ENV DOCKER_CERT_PATH ${DOCKER_CERT_PATH}
ARG DOCKER_TLS_VERIFY
ENV DOCKER_TLS_VERIFY ${DOCKER_TLS_VERIFY}

USER jenkins:jenkins