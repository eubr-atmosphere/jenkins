FROM eubraatmosphere/eubraatmosphere_autobuild:ub16_python2
LABEL author = "Ignacio <iblanque@dsic.upv.es>"
LABEL description = "opencv support"
 
RUN apt-get update
RUN pip install opencv-python
RUN apt-get -y install libsm6 libxrender1
COPY frameext.py /usr/local/bin

