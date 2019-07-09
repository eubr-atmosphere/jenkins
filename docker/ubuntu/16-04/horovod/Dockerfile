FROM eubraatmosphere/eubraatmosphere_autobuild:ub16gputf13-mpi41

RUN apt-get update -y 

ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-10.0/compat

RUN apt-get -yq install python3.6-dev
RUN pip install horovod
RUN pip install scikit-learn
RUN pip install scikit-image
RUN apt install libcudnn7=7.6.0.64-1+cuda10.0

ENTRYPOINT ["/usr/local/bin/ssh-start"]



