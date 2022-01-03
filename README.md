# Kubernetes-Artifacts-DevOps-Assignment
### A simple Dockerized Flask Web App that can be deployed on a local Kubernetes cluster

## Clone the repository on your local machine
git clone https://github.com/anubhavc9/Kubernetes-Artifacts-DevOps-Assignment.git

## Build the images using the Dockerfile. The image will be pulled from DockerHub.
`docker build -t anubhavc9/docker-flask-test .`

## Create deployment & service using Kubernetes artifacts
`kubectl apply -f deployment.yaml`
`kubectl apply -f service.yaml`

## Check the service NodePort
`kubectl get svc`

## Check the local minikube cluster IP
`minikube ip`

## You can access the Flask application on following 2 end-points:
- https://`Minikube IP:NodePort`
- https://`Minikube IP:NodePort`/pucsd
