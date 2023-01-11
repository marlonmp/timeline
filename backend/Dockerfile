ARG TAG

FROM python:${TAG} AS builder

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r ./requirements
