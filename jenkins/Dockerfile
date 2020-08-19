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

# Variables to connect to docker engine on another machine
ARG DOCKER_HOST
ENV DOCKER_HOST ${DOCKER_HOST}
ARG DOCKER_CERT_PATH
ENV DOCKER_CERT_PATH ${DOCKER_CERT_PATH}
ARG DOCKER_TLS_VERIFY
ENV DOCKER_TLS_VERIFY ${DOCKER_TLS_VERIFY}

LABEL \
  org.lucastercas.jenkins.image.authors="Lucas de Macedo Terças <lucasmtercas@gmail.com>" \
  org.lucastercas.jenkins.image.maintainers="Lucas de Macedo Terças <lucasmtercas@gmail.com>" \
  org.lucastercas.jenkins.image.version=${jenkins_vesion} \
  org.lucastercas.jenkins.image.title="lucastercas/jenkins" \
  org.lucastercas.jenkins.image.description="Helm application" \
  org.lucastercas.jenkins.image.licenses="" \
  org.lucastercas.jenkins.image.source="" \
  org.lucastercas.jenkins.image.url="" \
  org.lucastercas.jenkins.image.documentation="htps://github.com/lucastercas/docker-images"

EXPOSE 8080 50000
USER jenkins:jenkins