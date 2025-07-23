# k8sapp Deployment Guide

This guide explains how to build the Docker image, deploy the application to Kubernetes, expose it via a Service, and access it locally using port forwarding.

## 1. Build the Docker Image

First, build the Docker image for your application:

```sh
docker build -t k8sapp:v1 .
```

## 2. Kubernetes Deployment

### Dry Run (Check Manifest)

Validate your deployment manifest before applying:

```sh
kubectl apply -f deployment.yaml --dry-run=client
```

### Apply Deployment

Create the deployment in your cluster:

```sh
kubectl apply -f deployment.yaml
```

## 3. Create a Service

Assuming you have a `service.yaml` manifest, validate and apply it:

### Dry Run

```sh
kubectl apply -f service.yaml --dry-run=client
```

### Apply Service

```sh
kubectl apply -f service.yaml
```

## 4. Port Forwarding

To access your application locally (assuming the container exposes port 5000):

```sh
kubectl port-forward deployment/k8sapp 5000:5000
```

Now you can access the app at `http://localhost:5000/api/hello`.

## Summary of Steps

1. **Build the Docker image**: Prepares your app for deployment.
2. **Dry run manifests**: Validates your YAML files before making changes.
3. **Apply deployment and service**: Creates resources in Kubernetes.
4. **Port forwarding**: Lets you access the app from your local machine.

> Make sure your Kubernetes cluster is running and `kubectl` is configured to use the correct context.
