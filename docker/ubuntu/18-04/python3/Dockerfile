FROM eubraatmosphere/eubraatmosphere_autobuild:ubuntu18
LABEL description="Container with python 3 and python test libraries"
MAINTAINER Alfonso Pérez (alpegon3@upv.es)

# Update and install all the necessary packages
RUN apt-get update && apt-get install -y \
    python3 \
    python3-nose \
    python3-mock \
    python3-ply \
    python-tox \
    python3-coverage \
    python3-pip 
RUN pip3 install ipyparallel
RUN pip3 install opencv-python
RUN apt-get -y install libsm6 libxrender1 libxext6
RUN apt-get clean \
 && rm -rf /var/lib/apt/lists/*
