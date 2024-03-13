# Kubernetes Pod Resource Management Demo

## Overview

This project is designed to demonstrate the concepts of pod resource management in Kubernetes. It is an educational tool that showcases how to monitor and manage CPU and memory resources for applications running in a Kubernetes cluster. The project includes two main components: a loader application that simulates resource usage and a load manager application with a web UI for controlling the load on the loader.

## Components

1. **Loader**: A simple Python Flask application that can be configured to consume CPU and memory resources. This app simulates a workload that can be scaled up or down based on user input.

2. **Load Manager**: A Python Flask application with a web UI that allows users to adjust the resource consumption of the loader application. It communicates with the Kubernetes API to manage the loader pods.

3. **Prometheus Stack**: A monitoring solution that collects and stores metrics from the loader application and the Kubernetes cluster. It includes Prometheus for metric collection, Grafana for visualization, and Alertmanager for alerting.


## Prerequisites

- A Kubernetes cluster (e.g., Kind)
- Docker
- kubectl
- Helm (for deploying the Prometheus stack)

## Setup

1. **Create a Kind Cluster**: Follow the instructions in the [Kind documentation](https://kind.sigs.k8s.io/docs/user/quick-start/) to create a local Kubernetes cluster.
  - Alternatively run the configuration from this repo: `kind create cluster --config ./cluster/kindCOnfig.yaml`

2. **Set up MetalLB:** for loadbalancing the applications locally. In `./network/KindLB/` dir you can find manifests for deploying metal-lb with an ip address pool. Apply metallb-native first, let the pods run and then apply the pool.

3. **Deploy the Loader and Load Manager Applications**: Use the provided Kubernetes YAML files to deploy the loader and load manager applications to your cluster.

```bash
kubectl apply -f ./src/loader/manifests/lowlevel/
kubectl apply -f ./src/loadmng/manifests/
```

4. **Deploy the Prometheus Stack**: Use Helm to deploy the Prometheus stack to your cluster.
  - Alternatively, I included a simple script to add the community prometheus to helm local repos and install the chart. From `./monitoring` run `./stackprom.sh` as follows:

```
./stackprom.sh addRepo
./stackprom.sh installProm -r <RELEASE NAME>
```

## Usage

1. **Access the Load Manager Web UI**: Use the external IP of the load manager service to access the web UI. If you're using Kind with MetalLB, you can find the IP with the following command:

   ```bash
   kubectl get service loadmanager
   ```

2. **Adjust the Load**: Use the web UI to increase or decrease the CPU and memory load on the loader application.

3. **Monitor Resource Usage**: Access the Grafana dashboard provided by the Prometheus stack to monitor the resource usage of the loader application and the Kubernetes cluster.

## Cleanup

Besides the prometheus helm repo on your helm, feel free to destroy the kind cluster.
