FROM ubuntu
MAINTAINER Ignacio Blanquer <iblanque@dsic.upv.es> 

RUN apt-get update

RUN apt-get -yq install openssh-server; \
  mkdir -p /var/run/sshd; \
  mkdir /root/.ssh && chmod 700 /root/.ssh; \
  cat /dev/zero | ssh-keygen -q -N "" \
  touch /root/.ssh/authorized_keys

COPY bin/* /usr/local/bin/
COPY sshd_config /etc/ssh/sshd_config

EXPOSE 22

#ENTRYPOINT ["ssh-start"]
#CMD ["ssh-server"]

CMD ["ssh-start"]
