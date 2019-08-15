FROM python:3.4-slim

RUN apt-get update -y && apt-get install -y g++

ADD . /src
WORKDIR /src

RUN pip install -e .[dev]

RUN pip install twine
RUN python setup.py sdist
RUN twine check dist/*
