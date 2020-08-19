FROM debian
WORKDIR /opt/app
RUN apt-get update -y && \
  apt-get install -y --no-install-recommends\
  python3 \
  python3-pip \
  sudo \
  ansible \
  sshpass \
  git \
  openssh-client && \
  rm -rf /var/lib/apt/lists*

RUN pip3 install docker

LABEL \
  org.lucastercas.ansible.image.authors="Lucas Terças <lucasmtercas@gmail.com>" \
  org.lucastercas.ansible.image.maintainers="Lucas Terças <lucasmtercas@gmail.com>" \
  org.lucastercas.ansible.image.title="lucastercas/ansible" \
  org.lucastercas.ansible.image.description="Ansible application" \
  org.lucastercas.ansible.image.licenses="" \
  org.lucastercas.ansible.image.source="" \
  org.lucastercas.ansible.image.url="https://github.com/lucastercas/docker-images/tree/master/ansible"
  
CMD [ "ansible-playbook", "--version" ]