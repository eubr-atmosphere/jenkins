# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
#FROM jupyter/scipy-notebook
FROM eubraatmosphere/eubraatmosphere_autobuild:ub16_scipy-notebook

LABEL maintainer="Jupyter Project <jupyter@googlegroups.com>"

USER root
ENV PATH /opt/conda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

# Install Tensorflow
RUN conda install --quiet --yes \
    'tensorflow=1.5.0' \
    'keras=2.1*' && \
    conda clean -tipsy && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER

RUN pip install numpy --upgrade
