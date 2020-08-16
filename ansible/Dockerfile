FROM debian

LABEL \
  org.ansible.lucastercas.image.autor="Lucas Terças <lucasmtercas@gmail.com>" \
  org.ansible.lucastercas.image.mantainer="Lucas Terças <lucasmtercas@gmail.com>"

RUN apt-get update -y && \
  apt-get install -y --no-install-recommends\
  python3 \
  sudo \
  ansible \
  sshpass \
  openssh-client && \
  apt-get purge -y --auto-remove && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists*
  

CMD [ "ansible-playbook", "--version" ]