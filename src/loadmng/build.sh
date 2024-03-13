#!/bin/bash

docker build -t tiriyon/loadmanager:latest -f dockerfile .
docker push tiriyon/loadmanager:latest
