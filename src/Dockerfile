FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive

# # set work directory
WORKDIR /usr/src/app

# set environment variables..j.
# Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONDONTWRITEBYTECODE 1
# PYTHONUNBUFFERED: Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    git \
    python3 \
    python3-pip \
    python3.9
    
RUN pip3 install pipenv gunicorn uvicorn[standard] requests eth-utils eth-hash[pycryptodome] curlify

# copy project
COPY . /usr/src 
