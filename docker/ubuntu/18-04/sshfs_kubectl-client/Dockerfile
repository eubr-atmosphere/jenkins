FROM eubraatmosphere/eubraatmosphere_autobuild:ub18_kubectl
LABEL description="nfsclient to be used with itsthenetwork/nfs-server-alpine:latest. It also installs a kubectl client"
MAINTAINER Ignacio Blanquer (iblanque@dsic.upv.es)

# Update and install all the necessary packages
RUN apt-get update && apt-get install -y iputils-ping sshfs
COPY bin/mount.sh /usr/local/bin

# Update and install all the necessary packages
RUN apt-get install -y \
    python3 \
    python3-nose \
    python3-mock \
    python3-ply \
    python-tox \
    python3-coverage \
    python3-pip 
RUN pip3 install ipyparallel
RUN pip3 install opencv-python
RUN apt-get -y install libsm6 libxrender1
RUN apt-get clean \
 && rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["/usr/local/bin/mount.sh"]
