FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive

# # set work directory
WORKDIR /usr/src

# set environment variables...
# Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONDONTWRITEBYTECODE 1
# PYTHONUNBUFFERED: Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    git \
    python3 \
    python3-pip \
    python3.9
RUN pip3 install pipenv gunicorn uvicorn[standard] requests eth_utils

# copy project
COPY . /usr/src

# RUN mkdir -p /app
# COPY startup.py /startup.py
# RUN chmod u+x /startup.py
# VOLUME /app
# EXPOSE 8000
# WORKDIR /app
# CMD /startup.py
