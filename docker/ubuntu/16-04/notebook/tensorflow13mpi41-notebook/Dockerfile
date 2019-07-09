# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
#FROM jupyter/scipy-notebook
FROM eubraatmosphere/eubraatmosphere_autobuild:ub16_scipy-notebook

LABEL maintainer="Jupyter Project <jupyter@googlegroups.com>"

USER root
ENV PATH /opt/conda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
COPY servers/mnist_psserver.py /usr/local/bin/
COPY servers/mnist_train.py /usr/local/bin/
COPY servers/mnist_worker.py /usr/local/bin/

# Install Tensorflow
RUN conda install --quiet --yes tensorflow==1.13.1 keras && \
    conda clean -tipsy && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER

RUN pip install numpy --upgrade

# Install SSHServer for MPI
RUN apt update -y 

RUN apt-get -yq install openssh-server; \
  mkdir -p /var/run/sshd; \
  mkdir /root/.ssh && chmod 700 /root/.ssh; \
  cat /dev/zero | ssh-keygen -q -N ""; \
  touch /root/.ssh/authorized_keys

#COPY bin/* /usr/local/bin/
#COPY config /root/.ssh/config
#COPY sshd_config /etc/ssh/sshd_config
COPY bin/fix-perms.sh /usr/local/bin
COPY start-notebook.sh /usr/local/bin/


EXPOSE 22

# Install OpenMPI 4.1
RUN apt-get install -yq make g++

ENV LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/local/lib

COPY installopenmpi.sh /root
RUN /root/installopenmpi.sh

ENTRYPOINT ["/usr/local/bin/fix-perms.sh"]





