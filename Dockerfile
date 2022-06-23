FROM python:3.8.6-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y gcc g++ graphviz graphviz-dev swig build-essential python3-dev libssl-dev

WORKDIR /deploy/app

# Copy app dependencies
COPY ./requirements* /deploy/app/

# Install app dependencies
RUN pip3 install -r requirements.txt

COPY . /deploy/app

# app server
CMD ["bash", "/deploy/app/start_server.sh"]
