# FROM nvidia/cuda:11.1-base-ubuntu20.04
# FROM pytorch/pytorch
FROM orai/pytorch_cuda


RUN apt update && DEBIAN_FRONTEND=noninteractive apt install git python3-pip python3-dev -y
RUN pip install Flask
RUN pip install Flask-Cors==1.10.3
RUN pip install gevent
RUN pip install googledrivedownloader

WORKDIR /app
COPY . /app

RUN python3 download_models.py

ENV PORT 80
HEALTHCHECK CMD curl --fail http://localhost:$PORT || exit 1

CMD python3 wsgi.py
