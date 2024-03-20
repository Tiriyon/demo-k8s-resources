#!/bin/bash

TAG=$1
docker build -t tiriyon/loadmanager:latest -f dockerfile .
docker tag tiriyon/loadmanager:latest tiriyon/loadmanager:$TAG 
docker push tiriyon/loadmanager:latest
docker push tiriyon/loadmanager:$TAG
