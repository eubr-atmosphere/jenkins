FROM eubraatmosphere/eubraatmosphere_autobuild:ubuntu16gpu
LABEL description="Container with python 3 and python test libraries"
MAINTAINER Alfonso Pérez (alpegon3@upv.es)

RUN apt-get update
RUN apt-get install -y software-properties-common python-software-properties
RUN add-apt-repository -y ppa:jonathonf/python-3.6
RUN apt-get update
RUN apt-get install -y python3.6
RUN curl https://bootstrap.pypa.io/get-pip.py | python3.6
RUN pip install opencv-contrib-python
RUN pip install ipyparallel
RUN apt-get -y install libsm6 libxrender1 libxext6


#    python3-nose \
#    python3-mock \
#    python3-ply \
#    python-tox \
#    python3-coverage \
#RUN apt-get clean \
# && rm -rf /var/lib/apt/lists/*
