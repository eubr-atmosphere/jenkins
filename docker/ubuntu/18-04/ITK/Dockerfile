FROM grycap/jenkins:ubuntu18.04-git
LABEL description="Container with python 2.7 and python test libraries"
MAINTAINER Alfonso Pérez (alpegon3@upv.es)

# Update and install all the necessary packages
RUN apt-get update 
RUN apt-get install -y cmake \
                       insighttoolkit3-examples \
                       libfftw3-dev \
                       libinsighttoolkit3-dev \
                       libinsighttoolkit3.6 \
                       python-insighttoolkit3 \
                       tcl8.4 \
                       tcl8.4-insighttoolkit3 \
                       tk8.4
RUN apt-get clean 
