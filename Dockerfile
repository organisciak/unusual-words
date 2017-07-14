FROM jupyter/datascience-notebook:latest

MAINTAINER Peter Organisciak <organisciak@gmail.com>

USER root

RUN apt-get update -qq && \
    apt-get install -y \
	tesseract-ocr \
	libfreetype6-dev \
	libpng12-dev \
	libx11-dev \
	libmagickwand-dev \
	imagemagick

USER jovyan

RUN conda install -y \
	pytables \
	dask \
	bokeh

RUN conda install -y -c htrc htrc-feature-reader

RUN pip install \
	Pillow==2.9.0 \
	git+https://github.com/jflesch/pyocr.git

EXPOSE 8888

WORKDIR "/notebooks"
