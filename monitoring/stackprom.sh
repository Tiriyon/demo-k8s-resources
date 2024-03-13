#!/bin/bash

addRepo() {
     helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
     helm repo update
}

installProm() {
    if [[ "$1" == "-r" ]] && [[ -n "$2" ]]; then
        RELEASE_NAME="$2"
        helm install $RELEASE_NAME prometheus-community/kube-prometheus-stack
    else
        echo "Usage: stackprom.sh -r <relese-name>"
        exit 1
    fi
}

main() {
    case "$1" in
        addRepo)
           addRepo 
            ;;
        delete)
            delete
            ;;
        installProm)
            installProm "$2" "$3"
            ;;
        *)
            echo "Usage: $0 {addRepo|intallProm -r <release name>}"
            exit 1
    esac
}

main "$@"

