# Kubernetes-Artifacts-DevOps-Assignment
A simple dockerized webapp that can be deployed on a local Kubernetes cluster

# Clone the repository on your local machine
git clone

# Build the images using the Dockerfile. The image will be pulled from DockerHub.
docker build -t anubhavc9/docker-flask-test .

# Create deployment & service using Kubernetes artifacts
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

# Check the service NodePort
kubectl get svc

# Check the local minikube cluster ip
minikube ip

# Hit the following url on your browser
http://<Minikube IP>:<NodePort>
