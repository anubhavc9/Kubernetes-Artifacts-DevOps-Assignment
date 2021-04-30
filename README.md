# Kubernetes-Artifacts-DevOps-Assignment
A simple dockerized webapp that can be deployed on a local Kubernetes cluster

## Clone the repository on your local machine
git clone https://github.com/anubhavc9/Kubernetes-Artifacts-DevOps-Assignment.git

## Build the images using the Dockerfile. The image will be pulled from DockerHub.
docker build -t anubhavc9/docker-flask-test .

## Create deployment & service using Kubernetes artifacts
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

## Check the service NodePort
kubectl get svc

## Check the local minikube cluster ip
minikube ip

## Hit the following 2 urls on your browser
http://"Minikube IP":"NodePort"
http://"Minikube IP":"NodePort"/pucsd
