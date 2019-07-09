# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
FROM eubraatmosphere/eubraatmosphere_autobuild:ub16_tensorflow13mpi41-notebook

LABEL maintainer="Jupyter Project <jupyter@googlegroups.com>"

USER root

RUN apt-get update -y 

ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-10.0/compat

RUN apt-get -yq install python3.6-dev
RUN pip install horovod
RUN pip install scikit-learn
RUN pip install scikit-image

RUN add-apt-repository ppa:graphics-drivers/ppa
RUN apt-key adv --fetch-keys  http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub

RUN echo "deb http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64 /" > /etc/apt/sources.list.d/cuda.list
RUN echo "deb http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64 /" > /etc/apt/sources.list.d/cuda_learn.list
RUN apt update -y


RUN apt install libcudnn7=7.6.0.64-1+cuda10.0

#ENTRYPOINT ["/usr/local/bin/ssh-start"]

ENTRYPOINT ["/usr/local/bin/fix-perms.sh"]
