#FROM ubuntu:16.04
FROM nvidia/cuda:9.0-runtime-ubuntu16.04
LABEL description="Base container image with the jenkins user configured"
MAINTAINER Alfonso Pérez (alpegon3@upv.es)

# Update and install all the necessary packages
# I have removed httpie & software-properties-common, as they install python2.7 and python3.5 respectively
RUN apt-get update && apt-get install -y \
    sudo \
    wget \
    curl \
    vim \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Add jenkins user/group
RUN groupadd -g 1001 jenkins \
 && useradd -m -d /home/jenkins -s /bin/bash -g jenkins -u 1001 jenkins

RUN groupadd -g 1000 atmosphere \
 && useradd -m -d /home/atmosphere -s /bin/bash -g atmosphere -u 1000 atmosphere

RUN adduser jenkins sudo
RUN adduser atmosphere sudo

# Enable passwordless sudo for users under the "sudo" group
RUN sed -i.bkp -e 's/%sudo\s\+ALL=(ALL\(:ALL\)\?)\s\+ALL/%sudo ALL=NOPASSWD:ALL/g' /etc/sudoers
