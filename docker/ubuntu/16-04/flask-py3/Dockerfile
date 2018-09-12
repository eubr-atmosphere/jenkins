FROM eubraatmosphere/eubraatmosphere_autobuild:ubuntu16
LABEL author = "serlophug"
LABEL description = "Python Flask app"

RUN pip install Flask
#WORKDIR /usr/src/app
#COPY ./data/myapp.py .

HEALTHCHECK --interval=5s \
            --timeout=5s \
            CMD curl -f http://127.0.0.1:80 || exit 1

EXPOSE 80 

RUN apt install curl -y
#CMD ["python", "./myapp.py"]
