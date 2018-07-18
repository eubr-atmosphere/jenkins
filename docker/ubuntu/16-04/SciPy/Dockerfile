FROM eubraatmosphere/eubraatmosphere_autobuild:ub16_python2
LABEL author = "Ignacio"
LABEL description = "opencv support"
 
RUN apt-get update
RUN apt-get install -y python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose
RUN pip install scikit-image
RUN pip install opencv-python


