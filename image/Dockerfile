FROM ubuntu:22.04
RUN apt update && apt install -y python3-pip git libpq-dev && rm -rf /var/lib/apt/lists/*
COPY image/requirements.txt /server/
RUN pip3 install -r /server/requirements.txt
