FROM eubraatmosphere/eubraatmosphere_autobuild:ubuntu16
LABEL description="nfsclient to be used with itsthenetwork/nfs-server-alpine:latest"
MAINTAINER Ignacio Blanquer (iblanque@dsic.upv.es)

# Update and install all the necessary packages
RUN apt-get update && apt-get install -y iputils-ping nfs-common
COPY bin/mount.sh /usr/local/bin

ENTRYPOINT ["/usr/local/bin/mount.sh"]
