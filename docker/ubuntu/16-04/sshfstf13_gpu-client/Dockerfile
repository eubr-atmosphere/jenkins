FROM eubraatmosphere/eubraatmosphere_autobuild:ub16gpu10_python3
LABEL description="nfsclient to be used with itsthenetwork/nfs-server-alpine:latest"
MAINTAINER Ignacio Blanquer (iblanque@dsic.upv.es)

# Update and install all the necessary packages
RUN apt-get update && apt-get install -y iputils-ping sshfs
RUN pip install tensorflow-gpu==1.13.1
RUN pip install keras
RUN pip install numpy --upgrade
RUN ln -sf /usr/bin/python3.6 /usr/bin/python3
RUN apt-get install -y libgomp1

# We need to download and install libcudnn7:
# sudo dpkg -i libcudnn7_7.5.0.56-1+cuda9.0_amd64.deb
RUN wget https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1604/x86_64/libcudnn7_7.5.0.56-1+cuda9.0_amd64.deb
RUN dpkg -i libcudnn7_7.5.0.56-1+cuda9.0_amd64.deb

COPY servers/mnist_psserver.py /usr/local/bin/
COPY servers/mnist_train.py /usr/local/bin/
COPY servers/mnist_worker.py /usr/local/bin/
COPY bin/mount.sh /usr/local/bin

ENTRYPOINT ["/usr/local/bin/mount.sh"]
