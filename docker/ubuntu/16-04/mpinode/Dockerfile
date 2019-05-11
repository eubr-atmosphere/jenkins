FROM eubraatmosphere/eubraatmosphere_autobuild:ub16gpu_ssfstf13-client

RUN apt update -y 

RUN apt-get -yq install openssh-server; \
  mkdir -p /var/run/sshd; \
  mkdir /root/.ssh && chmod 700 /root/.ssh; \
  cat /dev/zero | ssh-keygen -q -N ""; \
  touch /root/.ssh/authorized_keys

RUN apt install -y openmpi-bin libopenmpi-dev

COPY bin/* /usr/local/bin/
COPY config /root/.ssh/
COPY sshd_config /etc/ssh/sshd_config

EXPOSE 22

#ENTRYPOINT ["ssh-start"]
#CMD ["ssh-server"]

ENTRYPOINT ["/usr/local/bin/ssh-start"]



