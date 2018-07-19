FROM eubraatmosphere/eubraatmosphere_autobuild:ubuntu16

LABEL description="Container with kubectl"
MAINTAINER Ignacio Blanquer (iblanque@dsic.upv.es)

# Update and install all the necessary packages
RUN apt-get update &&  apt-get install -y apt-transport-https
RUN apt get -y install curl gnupg
RUN curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg |  apt-key add -
RUN touch /etc/apt/sources.list.d/kubernetes.list 
RUN echo "deb http://apt.kubernetes.io/ kubernetes-xenial main" |  tee -a /etc/apt/sources.list.d/kubernetes.list
RUN apt-get update
RUN apt-get install -y kubectl

