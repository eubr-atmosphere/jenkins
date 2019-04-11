FROM eubraatmosphere/eubraatmosphere_autobuild:ub16_python3
LABEL description="nfsclient to be used with itsthenetwork/nfs-server-alpine:latest"
MAINTAINER Ignacio Blanquer (iblanque@dsic.upv.es)

# Update and install all the necessary packages
RUN apt-get update && apt-get install -y iputils-ping sshfs
RUN pip install tensorflow
RUN pip install keras
RUN pip install numpy --upgrade
RUN ln -sf /usr/bin/python3.6 /usr/bin/python3
COPY servers/mnist_psserver.py /usr/local/bin/
COPY servers/mnist_train.py /usr/local/bin/
COPY servers/mnist_worker.py /usr/local/bin/
COPY bin/mount.sh /usr/local/bin

ENTRYPOINT ["/usr/local/bin/mount.sh"]
