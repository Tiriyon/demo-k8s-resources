#!/bin/bash

docker build -t tiriyon/loader:latest -f dockerfile .
docker push tiriyon/loader:latest
