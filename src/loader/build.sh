#!/bin/bash

TAG=$1

docker build -t tiriyon/loader:$TAG -f dockerfile .
docker tag tiriyon/loader:$TAG tiriyon/loader:latest
docker push tiriyon/loader:latest
docker push tiriyon/loader:$TAG
