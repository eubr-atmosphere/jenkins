#FROM python:2.7-alpine as pip_build
FROM eubraatmosphere/eubraatmosphere_autobuild:ub16_sshfspy-client as pip_build
RUN apt-get update && apt-get install -y g++ python2.7 sshfs
#RUN apk add --no-cache g++
COPY requirements.txt /
COPY mount.sh /usr/local/bin
RUN pip install -r /requirements.txt
RUN pip install Babel

#FROM openjdk:8-jre-alpine
#FROM openjdk:8-jre
RUN apt install -y openjdk-8-jre
LABEL maintainer="Vinicius Dias <viniciusvdias@dcc.ufmg.br>, Guilherme Maluf \
<guimalufb@gmail.com>, Gabriel Barbutti <gabrielbarbutti@gmail.com>"

ENV LIMONERO_HOME=/usr/local/limonero
ENV LIMONERO_CONFIG=${LIMONERO_HOME}/conf/limonero-config.yaml \
    PYTHONPATH=${PYTHONPATH}:${JUICER_HOME}

#COPY --from=pip_build /usr/local /usr/local

WORKDIR $LIMONERO_HOME

# Java dependencies
ARG IVY_VERSION=2.3.0
ARG IVY_PKG=ivy-${IVY_VERSION}.jar
ARG IVY_URL=http://search.maven.org/remotecontent?filepath=org/apache/ivy/ivy/${IVY_VERSION}/${IVY_PKG}

COPY ivy.xml ./
RUN  wget --quiet $IVY_URL -O  /tmp/${IVY_PKG} \ 
  && java -jar /tmp/${IVY_PKG} -retrieve "${LIMONERO_HOME}/jars/[artifact]-[revision](-[classifier]).[ext]" \
  && rm /tmp/${IVY_PKG}

COPY . $LIMONERO_HOME
RUN pybabel compile -d $LIMONERO_HOME/limonero/i18n/locales
ENTRYPOINT ["/usr/local/bin/mount.sh"]
CMD ["/usr/local/limonero/sbin/limonero-daemon.sh", "docker"]
