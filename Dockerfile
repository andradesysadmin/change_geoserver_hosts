FROM ubuntu:24.04

LABEL maintainer="gandradecortez50@gmail.com"
LABEL version="1.0"
LABEL description="Script to change hosts of images in geoserver"

RUN apt-get update && apt-get install -y python3.12 python3-pip && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir /app

WORKDIR /app

COPY . .

EXPOSE 8181

# a execussão do comando nao impedira o funcionamento do container
CMD python3 app.py || true
