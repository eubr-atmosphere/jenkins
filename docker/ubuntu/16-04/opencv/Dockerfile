FROM eubraatmosphere/eubraatmosphere_autobuild:ub16_sshfspy-client
LABEL author = "Ignacio <iblanque@dsic.upv.es>"
LABEL description = "opencv support"
 
RUN apt-get update
RUN pip install opencv-python
COPY frameext.py /usr/local/bin

