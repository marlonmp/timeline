ARG TAG

FROM node:${TAG} AS builder

WORKDIR /app

COPY . .

RUN yarn install
