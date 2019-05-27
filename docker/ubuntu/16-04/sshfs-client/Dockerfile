FROM eubraatmosphere/eubraatmosphere_autobuild:ubuntu16
MAINTAINER Ignacio Blanquer (iblanque@dsic.upv.es)

# Update and install all the necessary packages
RUN apt-get update && apt-get install -y iputils-ping sshfs
COPY bin/mount.sh /usr/local/bin
COPY bin/entrypoint.sh /usr/local/bin

ENTRYPOINT ["/usr/local/bin/mount.sh"]
