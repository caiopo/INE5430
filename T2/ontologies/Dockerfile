FROM ubuntu:xenial

RUN apt-get update && apt-get install -y \
    openjdk-8-jdk \
    python3 \
    python3-pip


RUN pip3 install owlready

WORKDIR /home

ADD create_onto.py .

CMD bash
