FROM eubraatmosphere/eubraatmosphere_autobuild:ubuntu18
LABEL author = "Ignacio"
LABEL description = "support of Keras, Tensorflow and opencv"
 
RUN apt-get update 
RUN apt-get install -y software-properties-common python-software-properties
RUN add-apt-repository -y ppa:jonathonf/python-3.6
RUN apt-get update
RUN apt-get install -y python3.6
RUN curl https://bootstrap.pypa.io/get-pip.py | python3.6
RUN pip install opencv-contrib-python
RUN pip install keras --upgrade
RUN pip install tensorflow

