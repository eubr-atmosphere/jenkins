FROM eubraatmosphere/eubraatmosphere_autobuild:ubuntu16
MAINTAINER Ignacio Blanquer <iblanque@dsic.upv.es> 

#EXAMPLE: docker run -dit --name mpinode -e SSHKEY="ssh-rsa AAA...." image bash

RUN apt-get update

RUN apt-get -yq install openssh-server; \
  mkdir -p /var/run/sshd; \
  mkdir /root/.ssh && chmod 700 /root/.ssh; \
  cat /dev/zero | ssh-keygen -q -N ""; \
  touch /root/.ssh/authorized_keys

COPY bin/* /usr/local/bin/
COPY sshd_config /etc/ssh/sshd_config

EXPOSE 22

#ENTRYPOINT ["ssh-start"]
#CMD ["ssh-server"]

ENTRYPOINT ["/usr/local/bin/ssh-start"]
